import random
import json

from webargs.flaskparser import use_args
from tweepy.error import TweepError

from flask import Blueprint
from flask import jsonify
from flask.ext.cors import cross_origin

from gifter import utils

from gifter.api.ebay_api import EbayApi
from gifter.models import GifterStats

from core import config
from core import errors

from crawlers.user_tweets import get_users_tweets

from ml.entities import get_hashtags_info
from ml.gifts.process import get_ebay_categories


gifter_api = Blueprint('gifter_api', __name__)


@gifter_api.route('/api/items/<screen_name>/', methods=['POST'])
@cross_origin()
@use_args(config.ITEMS_ARGS_PARSER)
def items_handler(args, screen_name):
    """Retrives items from eBay.

    :param screen_name: Twitter @nick of user to whom we'd like to make a gift.
    :param min_price: Minimum price of a searched items (Integer)
    :param max_price: Maximum price of a searched items (Integer)
    :param limit: Limit of items in response (default 6) (Integer)

    Returns a json data with items.

    ..Example usage:
        /api/items/rivinek/?min_price=0&max_price=100&limit=1

    .. Example response:

        {u'gifts': [{u'galleryURL': u'www.image.140.jpg',
                     u'sellingStatus':
                        {u'convertedCurrentPrice': {u'_currencyId': u'USD',
                                                    u'value': u'3.89'},
                         u'currentPrice': {u'_currencyId': u'USD',
                                           u'value': u'3.89'},
                         u'sellingState': u'Active',
                         u'timeLeft': u'P24DT3H52M23S'},
                     u'title': u'ObamaCare Survival Guide'}],
         u'hashtags': [{u'count': 181, u'name': u'raisethewage'},
                       {u'count': 159, u'name': u'actonclimate'},
                       {u'count': 138, u'name': u'getcovered'},
                       {u'count': 113, u'name': u'opportunityforall'}]}
    """
    try:
        df = get_users_tweets([screen_name])
    except TweepError as e:
        something_wrong = {'error': 'something_went_wrong'}
        try:
            response = json.loads(e.reason)
        except ValueError:
            return jsonify(something_wrong)
        else:
            for error in response['errors']:
                if error['code'] == 34:
                    return jsonify({'error': 'user_not_found'})
        return jsonify(something_wrong)

    if df.empty:
        return jsonify({'error': 'no_tweets'})

    hashtags = get_hashtags_info(df)
    ebay_categories, interest_class = get_ebay_categories(df)
    random.shuffle(ebay_categories)
    ebay_api = EbayApi()
    response = {'category': interest_class}
    items = []
    limit = args['limit']
    for ebay_category in ebay_categories:
        try:
            args.update({'keywords': hashtags.keys(),
                         'category_name': ebay_category,
                         'limit': max(limit-len(items), 0), })
            items += ebay_api.get_items(**args)
        except errors.ItemsNotFoundError:
            pass

    if len(items) < limit:
        try:
            args.update({'keywords': hashtags.keys(), 'category_name': 'Books',
                         'limit': max(limit-len(items), 0), })
            items += ebay_api.get_items(**args)
        except errors.ItemsNotFoundError:
            response = {
                'error': 'presents_not_found'
            }

    response['gifts'] = items[:limit]

    response.update(utils.convert_hashtag_response(hashtags))
    return jsonify(response)


@gifter_api.route('/api/save/', methods=['POST'])
@cross_origin()
@use_args(config.SAVE_GITER_ARGS_PARSER)
def save_category(args):
    """
    /api/save/
    POST arguments:
        gift_category
        interest_category
        screen_name
    """
    GifterStats(
        screen_name=args.get('screen_name'),
        gift_category=args.get('gift_category'),
        interest_category=args.get('interest_category'),
    ).save()
    return jsonify({'status': 200, 'message': 'Entity saved'})

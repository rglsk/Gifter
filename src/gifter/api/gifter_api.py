from webargs.flaskparser import use_args

from flask import Blueprint
from flask import jsonify
from flask.ext.cors import cross_origin

from gifter import utils
from gifter.api.ebay_api import EbayApi
from gifter.models import CounterModel

from core import config
from ml.entities import get_hashtags_info


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

    hashtags = get_hashtags_info(screen_name)
    args.update({'keywords': hashtags.keys(), 'category_name': 'Books'})

    ebay_api = EbayApi()
    response = ebay_api.get_items(**args)
    response.update(utils.convert_hashtag_response(hashtags))

    return jsonify(response)


@gifter_api.route('/api/counter/', methods=['POST'])
@cross_origin()
@use_args(config.COUNTER_ARGS_PARSER)
def counter(args):
    _filter = CounterModel.url == args.get('url')
    model = CounterModel.query.filter(_filter).first()
    if not model:
        model = CounterModel(**args)
    model.counter = int(model.counter or 0) + 1
    model.save()

    return jsonify({'status': 200, 'message': 'Counter increased'})

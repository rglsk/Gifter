from webargs.flaskparser import use_args
from tweepy.error import TweepError

from flask import Blueprint
from flask import jsonify
from flask.ext.cors import cross_origin

from gifter.models import FunStats

from core import config

from crawlers.user_tweets import get_users_tweets
from ml.people.process import get_character


whoami_api = Blueprint('whoami_api', __name__)


@whoami_api.route('/api/person/<screen_name>/', methods=['POST'])
@cross_origin()
def person_handler(screen_name):
    try:
        df = get_users_tweets([screen_name])
    except TweepError:
        return jsonify({'error': 'user_not_found'})

    if df.empty:
        return jsonify({'error': 'no_tweets'})

    return jsonify(get_character(df))


@whoami_api.route('/api/save/person/', methods=['POST'])
@cross_origin()
@use_args(config.SAVE_WHOAMI_ARGS_PARSER)
def save_category(args):
    """
    /api/save/person/
    POST arguments:
        interest_category
        screen_name
    """
    FunStats(
        screen_name=args.get('screen_name'),
        interest_category=args.get('interest_category'),
    ).save()
    return jsonify({'status': 200, 'message': 'Entity saved'})

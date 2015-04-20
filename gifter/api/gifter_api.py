from webargs.flaskparser import use_args

from flask import Blueprint
from flask import jsonify

from gifter import config
from gifter.api.ebay_api import EbayApi

gifter_api = Blueprint('gifter_api', __name__)


@gifter_api.route('/items/<query_name>/',
                  methods=['POST'])
@use_args(config.ITEMS_ARGS_PARSER)
def get_items(args, query_name):
    """Retrives items from eBay.

    :param query_name: Twitter @nick of user to whom we'd like to make a gift.
    :param min_price: Minimum price of a searched items.
    :param max_price: Maximum price of a searched items.

    Returns a json data with items.
    """
    ebay_api = EbayApi()
    items = ebay_api.get_items(**args)

    return jsonify(items)

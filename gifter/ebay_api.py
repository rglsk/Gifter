from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as finding
from ebaysdk.trading import Connection as trading

import config
import pandas as pd


class EbayApi(object):

    def __init__(self):
        config_file = '../ebay.yaml'
        self.finding_api = finding(domain=config.EBAY_SANDBOX_DOMAIN,
                                   appid=config.EBAY_SANDBOX_APP_ID,
                                   config_file=config_file)

        self.trading_api = trading(appid=config.EBAY_SANDBOX_APP_ID,
                                   certid=config.EBAY_SANDBOX_CERT_ID,
                                   devid=config.EBAY_SANDBOX_DEVID,
                                   config_file=config_file)

    @classmethod
    def add_filter(cls, name, value):
        return {'name': name, 'value': value}

    def generate_category_hierarchy(self, level_limit=1):
        """Generate latest category hierarchy for the eBay site.
        (Retrieving the full set of eBay categories can be time-consuming
        and the result sets can be quite large.)
        :param level_limit: Specifies the maximum depth of the category
        hierarchy to retrieve, where the top-level categories (meta-categories)
        are at level 1
        """
        call_data = {
            'DetailLevel': 'ReturnAll',
            'LevelLimit': level_limit,
        }
        resp = self.trading_api.execute('GetCategories', call_data)
        df = pd.DataFrame(resp.dict()['CategoryArray']['Category'])
        df.to_json('category_hierarchy.json')

    def get_products(self, keywords, category_id=None, min_price=None,
                     max_price=None):
        try:
            item_filters = []
            if min_price:
                item_filters.append(self.add_filter('MinPrice', min_price))
            if max_price:
                item_filters.append(self.add_filter('MaxPrice', max_price))

            api_request = {
                'keywords': ','.join(keywords),
                'itemFilter': item_filters,
                'categoryId': category_id,
            }
            response = self.finding_api.execute('findItemsAdvanced',
                                                api_request)
            return response.dict()['searchResult']['item']
        except ConnectionError as e:
            return e

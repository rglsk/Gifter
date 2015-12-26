import json

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as finding
from ebaysdk.trading import Connection as trading

from core import errors
from core import config


class EbayApi(object):

    """EbayApi provides connection with eBay API."""
    _category_hierarchy_file = '{}/{}'.format(config.PROJECT_DIRECTORY,
                                              'gifter/category_hierarchy.json')

    def __init__(self):
        config_file = '{}/{}'.format(config.PROJECT_DIRECTORY, 'ebay.yaml')
        self.finding_api = finding(domain='svcs.ebay.com',
                                   appid=config.EBAY_PRODUCTION_APP_ID,
                                   config_file=config_file)

        self.trading_api = trading(appid=config.EBAY_PRODUCTION_APP_ID,
                                   certid=config.EBAY_PRODUCTION_CERT_ID,
                                   devid=config.EBAY_PRODUCTION_DEVID,
                                   config_file=config_file)

    def setup_params(func):
        def wrapper(self, **kwargs):
            params = {
                'keywords': self.create_search_query,
                'min_price': lambda x: self.add_filter('MinPrice', x),
                'max_price': lambda x: self.add_filter('MaxPrice', x),
            }
            if (
                kwargs.get('keywords') is not None and
                not isinstance(kwargs['keywords'], list)
            ):
                kwargs['keywords'] = list(kwargs['keywords'])
            for key, foo in params.iteritems():
                if kwargs.get(key):
                    kwargs[key] = foo(kwargs[key])
            kwargs['category_id'] = self.get_category_id(
                kwargs['category_name'])
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def add_filter(name, value):
        return {'name': name, 'value': value}

    @staticmethod
    def create_search_query(keywords):
        return ','.join(keywords)

    @staticmethod
    def _parse_items(items, limit):
        gifts = []
        for item in items:
            if set(config.ITEM_DETAILS) < set(item.keys()):
                gifts.append({key: item[key] for key in config.ITEM_DETAILS})
            if len(gifts) == limit:
                break
        return gifts

    def get_category_id(self, category_name):
        """Gets a category id from given name.

        :param category_name: Category name (String)

        Returns an ID of category (Integer). Otherwise, this method should
        raise CategoryNotFoundError.
        """
        with open(self._category_hierarchy_file, 'r') as data_file:
            category_data = json.load(data_file)

        for category in category_data:
            if category_name == category['CategoryName']:
                return int(category['CategoryID'])

        raise errors.CategoryNotFoundError(
            'Category: {} not found.'.format(category_name))

    def generate_category_hierarchy(self, level_limit=1):
        """Generate latest category hierarchy for the eBay site.
        (Retrieving the full set of eBay categories can be time-consuming
        and the result sets can be quite large.)

        :param level_limit: Specifies the maximum depth of the category
                            hierarchy to retrieve, where the top-level
                            categories (meta-categories) are at level 1
        """
        call_data = {
            'DetailLevel': 'ReturnAll',
            'LevelLimit': level_limit,
        }
        resp = self.trading_api.execute('GetCategories', call_data)
        with open(self._category_hierarchy_file, 'w') as json_file:
            json_file.write(
                json.dumps(resp.dict()['CategoryArray']['Category'], indent=4)
            )

    @setup_params
    def get_items(self, keywords=None, category_id=None, category_name=None,
                  min_price=None, max_price=None, sort_order='BestMatch',
                  limit=config.ITEMS_LIMIT):
        """Retrieves items from eBay by given keywords (applies OR logic to
            multiple keywords) or/and category name.

        :param keywords: List of item keywords to search
        :param category_name: Category name (String)
        :param min_price: The minimum price of item (Integer)
        :param max_price: The maximum price of item (Integer)
        :param sort_order: Sort the returned items according to a single
                           specified sort order:
                           - BestMatch: based on community buying activity and
                                        other relevance-based factors
                           - StartTimeNewest: the most recently listed (newest)
                                              items appear first
        :param limit: Limit of items to get (default 6) (Integer)

        Returns a list of items.

        .. Example usage:

            EbayApi().ebay_api.get_items(
                keywords=['baseball', 'card'],
                min_price=0,
                category_name='Sports Mem, Cards & Fan Shop'
            )
        """
        api_request = {
            'itemFilter': [min_price, max_price],
            'categoryId': category_id,
            'sortOrder': sort_order,
            'outputSelector': 'PictureURLSuperSize',
        }
        if keywords is not None:
            api_request.update({
                'keywords': '({})'.format(keywords),
            })
        try:
            response = self.finding_api.execute('findItemsAdvanced',
                                                api_request)
            items = response.dict()['searchResult']['item']
            result = self._parse_items(items, limit)
            return result
        except ConnectionError as e:
            return e
        except KeyError:
            raise errors.ItemsNotFoundError('Items not found.')

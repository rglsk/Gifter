import unittest

from core import config
from gifter.testing import BaseApiTest


class TestViews(BaseApiTest):

    def setUp(self):
        super(TestViews, self).setUp()

    @unittest.skip("Live test skipping")
    def test_items_handler_live(self):
        """Live test for retrieval items from eBay by gifter_api.

        ..Note:
            Live means that this test connect with eBay API without any mock.
        """
        params = {
            'min_price': 0,
            'max_price': 100,
        }
        screen_name = 'BarackObama'
        result = self.post_json('/api/items/{}/'.format(screen_name),
                                data=params)
        self.assertTrue(result['gifts'])
        self.assertEqual(len(result['gifts']), config.ITEMS_LIMIT)
        self.assertEqual(result['gifts'][0].keys(), config.ITEM_DETAILS)


if __name__ == '__main__':
    unittest.main()

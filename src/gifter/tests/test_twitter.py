import unittest

from gifter.crawlers.user_friends import get_user_friends


class TestTwitter(unittest.TestCase):

    @unittest.skip("Live test skipping")
    def test_get_user_friends_live(self):
        friends = get_user_friends('PiotrRogulski')
        self.assertEqual(['screen_name', 'id', 'name'], friends[1].keys())

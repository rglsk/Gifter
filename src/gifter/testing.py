import json
import unittest

from manage import app


class BaseApiTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.get = self.app.get
        self.post = self.app.post

    def get_json(self, url):
        params = self.get(url).data
        return json.loads(params)

    def post_json(self, url, data=None):
        params = self.post(url, data=data).data
        return json.loads(params)

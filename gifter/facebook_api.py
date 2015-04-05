#!/usr/bin/python
import facebook
import urlparse
import requests

from errors import (
    FacebookApiError,
    NoAccesTokenError
)
from gifter.config import (
    FACEBOOK_APP_ID,
    FACEBOOK_APP_SECRET,
    # FACEBOOK_PROFILE_ID,
)


def get_fb_access_token():
    params = {'grant_type': 'client_credentials',
              'client_id': FACEBOOK_APP_ID,
              'client_secret': FACEBOOK_APP_SECRET}
    oauth_response = requests.post(
        'https://graph.facebook.com/oauth/access_token?', params=params)
    try:
        return urlparse.parse_qs(
            str(oauth_response.text)
        )['access_token'][0]
    except KeyError:
        raise NoAccesTokenError('Unable to grab an access token!')


if __name__ == '__main__':
    """Only for testing"""
    oauth_access_token = get_fb_access_token()
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    try:
        print facebook_graph.get_object("me")
    except facebook.GraphAPIError as e:
        raise FacebookApiError('Type error: {}, message: {}'.format(e.type,
                                                                    e.message))

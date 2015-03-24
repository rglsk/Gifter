#!/usr/bin/python
import facebook
import urllib
import urlparse
import subprocess

from errors import (
    FacebookApiError,
    NoAccesTokenError
)
from config import (
    FACEBOOK_APP_ID,
    FACEBOOK_APP_SECRET,
    FACEBOOK_PROFILE_ID,
    FB_ACCESS_TOKEN_URL,
)


def get_fb_access_token():
    # Trying to get an access token. Very awkward.
    oauth_args = dict(
        client_id=FACEBOOK_APP_ID,
        client_secret=FACEBOOK_APP_SECRET,
        grant_type='client_credentials'
    )
    oauth_url = FB_ACCESS_TOKEN_URL.format(urllib.urlencode(oauth_args))
    oauth_curl_cmd = ['curl', oauth_url]
    oauth_response = subprocess.Popen(
        oauth_curl_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()[0]

    try:
        return urlparse.parse_qs(
            str(oauth_response)
        )['access_token'][0]
    except KeyError:
        raise NoAccesTokenError('Unable to grab an access token!')


if __name__ == '__main__':
    """Only for testing"""
    oauth_access_token = get_fb_access_token()
    facebook_graph = facebook.GraphAPI(oauth_access_token)

    try:
        # Try to post something on the wall.
        fb_response = facebook_graph.put_wall_post(
            'Test wall', profile_id=FACEBOOK_PROFILE_ID
        )
        print fb_response
    except facebook.GraphAPIError as e:
        raise FacebookApiError(
            'Type error: {}, message: {}'.format(e.type, e.message)
        )

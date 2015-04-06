#!/usr/bin/env python
from rauth.service import OAuth2Service
try:
    from gifter.local_settings import *
except ImportError:
    raise ImportError(
        'Please create file local_settings.py and set basic settings.'
    )


# FB_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?{}'
DEBUG = True

FB_GRAPH_URL = 'https://graph.facebook.com/'
FB_AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth'

access_token_url = FB_GRAPH_URL + 'oauth/access_token'
FACEBOOK_AUTH = OAuth2Service(name='facebook',
                              authorize_url=FB_AUTHORIZE_URL,
                              access_token_url=access_token_url,
                              client_id=FACEBOOK_APP_ID,
                              client_secret=FACEBOOK_APP_SECRET,
                              base_url=FB_GRAPH_URL)

#!/usr/bin/env python
try:
    from locale_settings import *
except ImportError:
    raise ImportError(
        'Please create file locale_settings.py and set basic settings.'
    )


FB_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?{}'

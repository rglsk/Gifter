#!/usr/bin/env python
try:
    from gifter.local_settings import *
except ImportError:
    raise ImportError(
        'Please create file local_settings.py and set basic settings.'
    )


FB_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?{}'

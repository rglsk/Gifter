#!/usr/bin/env python
import os

from webargs import Arg

from rauth.service import OAuth2Service
import tweepy

try:
    from core.local_settings import *
except ImportError:
    raise ImportError(
        'Please create file local_settings.py and set basic settings.'
    )

# General
DEBUG = True

# Facebook
FB_GRAPH_URL = 'https://graph.facebook.com/'
FB_AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth'

access_token_url = FB_GRAPH_URL + 'oauth/access_token'
FACEBOOK_AUTH = OAuth2Service(name='facebook',
                              authorize_url=FB_AUTHORIZE_URL,
                              access_token_url=access_token_url,
                              client_id=FACEBOOK_APP_ID,
                              client_secret=FACEBOOK_APP_SECRET,
                              base_url=FB_GRAPH_URL)
FB_PERMISSIONS = ['public_profile', 'user_friends', 'email', 'user_about_me',
                  'user_actions.books', 'user_actions.fitness', 'user_events',
                  'user_actions.music', 'user_actions.news', 'user_groups',
                  'user_actions.video', 'user_actions:rivinek-app',
                  'user_activities', 'user_birthday', 'user_education_history',
                  'user_interests', 'user_likes', 'user_relationship_details',
                  'user_relationships', 'read_custom_friendlists',
                  'read_insights', 'publish_actions']

# Twitter
TWITTER_AUTH = tweepy.OAuthHandler(
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET
)
TWITTER_AUTH.set_access_token(
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)


def setup_twitter_api():
    return tweepy.API(
        TWITTER_AUTH,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
    )

# eBay
EBAY_SANDBOX_DOMAIN = 'svcs.sandbox.ebay.com'
EBAY_PRODUCTION_DOMAIN = 'ebay.com'


# gifter API
ITEMS_LIMIT = 6
ITEM_DETAILS = ['title', 'sellingStatus', 'galleryURL']
ITEMS_ARGS_PARSER = {
    'min_price': Arg(int, default=None),
    'max_price': Arg(int, default=None),
    'limit': Arg(int, default=ITEMS_LIMIT)
}


# Data directory
DATA_DIRECTORY = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '..',
    'ml',
    'data'
)

# Suggested
SUGGESTED_DIRECTORY = os.path.join(
    DATA_DIRECTORY,
    'labeled_twitter'
)

SUGGESTED_CATEGORIES = os.path.join(
    SUGGESTED_DIRECTORY,
    'categories.json'
)

LLDA_TRAIN_DIRECTORY = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'modeling',
    'llda',
    'train_set')
LLDA_RESULTS_DIRECTORY = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'modeling',
    'llda')

TOPIC_NUMBER = 24

#!/usr/bin/env python
import os

from webargs import Arg

import tweepy

try:
    from core.local_settings import *
except ImportError:
    raise ImportError(
        'Please create file local_settings.py and set basic settings.'
    )

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
ITEM_DETAILS = ['title', 'sellingStatus', 'pictureURLSuperSize']
ITEMS_ARGS_PARSER = {
    'min_price': Arg(int, default=None),
    'max_price': Arg(int, default=None),
    'limit': Arg(int, default=ITEMS_LIMIT)
}

COUNTER_ARGS_PARSER = {
    'url': Arg(str, default=None),
    'category_name': Arg(str, default=None),
    'item_title': Arg(str, default=None)
}

# Project dir
PROJECT_DIRECTORY = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '..'
)

# Data directory
DATA_DIRECTORY = os.path.join(
    PROJECT_DIRECTORY,
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


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = TrueCSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

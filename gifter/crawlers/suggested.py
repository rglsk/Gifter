import json
import os

from gifter.config import (
    setup_twitter_api,
    DATA_DIRECTORY
)
from gifter.crawlers.user_tweets import get_users_tweets
from gifter.modeling.data import lemmatized_frame


ROOT_DIR = os.path.join(
    DATA_DIRECTORY,
    "labeled_twitter",
)

CATEGORIES_FILENAME = os.path.join(
    ROOT_DIR,
    "categories.json"
)


def get_suggested_topics():
    """
    Creates file with suggested categories from twitter as a dict {name: slug}
    """
    if not os.path.exists(CATEGORIES_FILENAME):
        api = setup_twitter_api()
        categories = {}
        for category in api.suggested_categories():
            categories[category.name] = category.slug
        with open(CATEGORIES_FILENAME, 'w') as f:
            json.dump(categories, f, indent=4)


def get_categories():
    with open(CATEGORIES_FILENAME, 'r') as f:
        return json.load(f)


def categories_dirnames(categories):
    for slug in categories.values():
        yield (
            slug,
            os.path.join(ROOT_DIR, slug)
        )


def get_suggested_nicknames():
    api = setup_twitter_api()
    for slug, dirname in categories_dirnames(get_categories()):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = os.path.join(
            dirname,
            'screen_names.json'
        )
        if not os.path.exists(filename):
            screen_names = [
                user.screen_name for user in api.suggested_users(slug)
            ]
            with open(filename, 'w') as f:
                json.dump(screen_names, f, indent=4)


def get_screen_names_from_cat(slug):
    filename = os.path.join(ROOT_DIR, slug, 'screen_names.json')
    with open(filename) as f:
        return json.load(f)


def get_suggested_tweets():
    for slug, dirname in categories_dirnames(get_categories()):
        for screen_name in get_screen_names_from_cat(slug):
            filename = os.path.join(dirname, "{}.json".format(screen_name))
            if not os.path.exists(filename):
                print "Saving: {}".format(filename)
                df = get_users_tweets([screen_name])
                df.to_json(filename)


def crawl_all():
    get_suggested_topics()
    get_suggested_nicknames()
    get_suggested_tweets()


def preprocess_all():
    for slug, dirname in categories_dirnames(get_categories()):
        for screen_name in get_screen_names_from_cat(slug):
            filename = os.path.join(dirname, "{}.json".format(screen_name))
            preprocess_filename = os.path.join(
                dirname,
                "pre_{}.json".format(screen_name)
            )
            if os.path.exists(filename) and not os.path.exists(preprocess_filename):
                print 'Preprocessing: {}'.format(preprocess_filename)
                df = lemmatized_frame(filename, with_tags=False)
                df[['text', 'lemmas']].to_json(preprocess_filename)

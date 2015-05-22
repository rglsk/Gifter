import json
import os

from gifter.config import (
    setup_twitter_api,
    DATA_DIRECTORY
)
from gifter.crawlers.user_tweets import get_users_tweets


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
            print "Saving: {}".format(filename)
            df = get_users_tweets([screen_name])
            df.to_json(filename)

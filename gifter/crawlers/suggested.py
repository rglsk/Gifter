import json
import os

from gifter.config import (
    setup_twitter_api,
    SUGGESTED_DIRECTORY,
    SUGGESTED_CATEGORIES
)
from gifter.crawlers.user_tweets import get_users_tweets
from gifter.modeling.data import lemmatized_frame


SCREEN_NAMES_FILENAME = 'screen_names.json'


def get_suggested_topics():
    """
    Creates file with suggested categories from twitter as a dict {name: slug}
    """
    if not os.path.exists(SUGGESTED_CATEGORIES):
        api = setup_twitter_api()
        categories = {}
        for category in api.suggested_categories():
            categories[category.name] = category.slug
        with open(SUGGESTED_CATEGORIES, 'w') as f:
            json.dump(categories, f, indent=4)


def get_categories():
    with open(SUGGESTED_CATEGORIES, 'r') as f:
        return json.load(f)


def categories_dirnames(categories):
    for slug in categories.values():
        yield (
            slug,
            os.path.join(SUGGESTED_DIRECTORY, slug)
        )


def get_suggested_nicknames():
    api = setup_twitter_api()
    for slug, dirname in categories_dirnames(get_categories()):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = os.path.join(
            dirname,
            SCREEN_NAMES_FILENAME
        )
        if not os.path.exists(filename):
            screen_names = [
                user.screen_name for user in api.suggested_users(slug)
            ]
            with open(filename, 'w') as f:
                json.dump(screen_names, f, indent=4)


def get_screen_names_from_cat(slug):
    filename = os.path.join(SUGGESTED_DIRECTORY, slug, SCREEN_NAMES_FILENAME)
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


def files_by_categories():
    for slug, dirname in categories_dirnames(get_categories()):
        for screen_name in get_screen_names_from_cat(slug):
            filename = os.path.join(dirname, "{}.json".format(screen_name))
            preprocess_filename = os.path.join(
                dirname,
                "pre_{}.json".format(screen_name)
            )
            yield slug, filename, preprocess_filename


def preprocess_all():
    for slug, filename, preprocess_filename in files_by_categories():
        if os.path.exists(filename) and not os.path.exists(preprocess_filename):
            print 'Preprocessing: {}'.format(preprocess_filename)
            df = lemmatized_frame(filename, with_tags=False)
            df[['text', 'lemmas']].to_json(preprocess_filename)


def remove_preprocessed():
    for slug, filename, preprocess_filename in files_by_categories():
        if os.path.exists(preprocess_filename):
            os.remove(preprocess_filename)

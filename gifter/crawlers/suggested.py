import json
import os

from gifter.config import (
    setup_twitter_api,
    DATA_DIRECTORY
)


def get_suggested_topics():
    """
    Creates file with suggested categories from twitter as a dict {name: slug}
    """
    api = setup_twitter_api()
    categories = {}
    for category in api.suggested_categories():
        categories[category.name] = category.slug
    filename = os.path.join(
        DATA_DIRECTORY,
        "labeled_twitter",
        "categories.json"
    )
    with open(filename, 'w') as f:
        json.dump(categories, f, indent=4)

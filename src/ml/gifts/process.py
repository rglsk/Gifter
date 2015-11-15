from os import path

import pandas as pd


from core.config import DATA_DIRECTORY
from crawlers.user_tweets import get_users_tweets
from ml.data import lemmatize_dataframe
from ml.skmodels.models import LinearSVCModel


def get_ebay_categories_mapping():
    df = pd.read_json(path.join(DATA_DIRECTORY, 'category_mapping.json'))

    ebay_categories = df[['CategoryID', 'CategoryID2']].values.tolist()
    return dict(
        zip(df['OurCategoryName'],
            map(lambda cats:
                [cat for cat in cats if not pd.isnull(cat)], ebay_categories))
    )


def prepare_dataframe(screen_name):
    df = get_users_tweets([screen_name])
    df = lemmatize_dataframe(df)
    return df


def interest_class(df):
    clf = LinearSVCModel()
    return clf.predict_one(df)


def get_ebay_category_ids(screen_name):
    mappings = get_ebay_categories_mapping()
    df = prepare_dataframe(screen_name)
    return mappings[interest_class(df)]

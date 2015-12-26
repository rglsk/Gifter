from os import path

import pandas as pd


from core.config import DATA_DIRECTORY
from ml.data import lemmatize_dataframe
from ml.skmodels.models import interest_class


def get_ebay_categories_mapping():
    df = pd.read_json(path.join(DATA_DIRECTORY, 'category_mapping.json'))

    ebay_categories = df[['CategoryName', 'CategoryName2']].values.tolist()
    return dict(
        zip(df['OurCategoryName'],
            map(lambda categories:
                [category for category in categories
                 if not pd.isnull(category)], ebay_categories))
    )


def get_ebay_categories(df):
    mappings = get_ebay_categories_mapping()
    df = lemmatize_dataframe(df)
    if not df.empty:
        interest = interest_class(df)
        return mappings.get(interest, []), interest
    return [], None

from os import path

import pandas as pd

from core.config import DATA_DIRECTORY
from ml.data import lemmatize_dataframe
from ml.skmodels.models import interest_class


def get_people_mapping():
    return pd.read_csv(path.join(DATA_DIRECTORY, 'whoami.csv'))


def get_character(df):
    mappings = get_people_mapping()
    mappings = mappings.where(pd.notnull(mappings), '')
    df = lemmatize_dataframe(df)
    interest = interest_class(df)
    row = mappings[mappings['category'] == interest].squeeze()
    return {
        'category': interest,
        'person': row[['name', 'desc', 'imgUrl']].to_dict()
    }

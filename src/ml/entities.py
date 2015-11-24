from collections import OrderedDict
from unidecode import unidecode

import pandas as pd


def get_entitie(obj, key, name):
    return [unidecode(entity.get(key, u'').lower()) for entity in obj[name]]


def get_series(df_tweets, key, name):
    return pd.Series(df_tweets.entities.apply(
        lambda obj: get_entitie(obj, 'text', 'hashtags')).dropna().sum())


def get_hashtags_info(df):
    hashtags = get_series(df, 'text', 'hashtags')
    hashtag_counts = hashtags.value_counts().head(10)
    hashtags_dict = hashtag_counts.to_dict()
    return OrderedDict(reversed(sorted(hashtags_dict.items(),
                                       key=lambda x: x[1])))

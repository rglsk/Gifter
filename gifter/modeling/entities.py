from collections import OrderedDict
from unidecode import unidecode

import pandas as pd


def get_entitie(obj, key, name):
    return [unidecode(entity.get(key, u'').lower()) for entity in obj[name]]


def get_series(key, name):
    df = pd.io.json.read_json("gifter/modeling/data.json")
    return pd.Series(df.entities.apply(
        lambda obj: get_entitie(obj, 'text', 'hashtags')).dropna().sum())


def get_hashtags_info():
    hashtags = get_series('text', 'hashtags')
    hashtag_counts = hashtags.value_counts().head(10)
    hashtags_dict = hashtag_counts.to_dict()
    return OrderedDict(reversed(sorted(hashtags_dict.items(),
                                       key=lambda x: x[1])))

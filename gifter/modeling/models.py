"""
Base Model class
"""
import abc
import pandas as pd
from gifter.crawlers.suggested import get_categories
from gifter.modeling.tokenizer import lemmatize


def classes():
    df = pd.DataFrame(
        get_categories().values(),
        columns=['name']
    )
    df['lemmatized'] = df.name.map(lambda name: lemmatize(name, with_tags=False))
    return df


class BaseModel(object):
    __metaclass__ = abc.ABCMeta

    CLASSES = classes()

    def __init__(self, name, storage_name):
        self.name = name
        self.storage_name = storage_name
        self.clf = self._get_storage()

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def train(self, inputs, outputs):
        return

    @abc.abstractmethod
    def _get_storage(self):
        return

    @abc.abstractmethod
    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        return

    @abc.abstractmethod
    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return


class MergingBaseModel(BaseModel):

    @staticmethod
    def _merge(df):
        return df.lemmas.map(" ".join).sum()

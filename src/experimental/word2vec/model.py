import numpy as np
from gensim.models import Word2Vec

from ml.models import BaseModel
from experimental.word2vec.pretrained_models import MODELS


class Word2VecModel(BaseModel):

    def __init__(self):
        super(Word2VecModel, self).__init__('Word2Vec', MODELS['google'])

    def _get_storage(self):
        return Word2Vec.load_word2vec_format(self.storage_name, binary=True)

    def train(self, inputs, outputs):
        """
        This model does not need training on tweets
        """
        self.clf = self._get_storage()

    def _similarity(self, w1, w2):
        try:
            return self.clf.similarity(w1, w2)
        except KeyError:
            return 0

    def _membership(self, words, tweet_lemmas):
        return np.max([
            [self._similarity(word, tweet_lemma) for word in words]
            for tweet_lemma in tweet_lemmas
        ])

    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        df = self.CLASSES.copy()
        df['values'] = df.lemmatized.apply(
            lambda categories: one.lemmas.apply(
                lambda tweet_lemmas:
                    self._membership(categories, tweet_lemmas)
            ).sum()
        )
        return df.loc[df['values'].argmax()]['name']

    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return [self.predict_one(i) for i in inputs]

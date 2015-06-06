import os

from sklearn.externals import joblib
from sklearn.feature_extraction.text import (
    CountVectorizer,
)
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from gifter.modeling.models import MergingBaseModel
from gifter.errors import UntrainedModelError
from gifter.config import DATA_DIRECTORY


class BayesModel(MergingBaseModel):

    def __init__(self):
        super(BayesModel, self).__init__(
            'BayesModel',
            os.path.join(DATA_DIRECTORY, 'bayes', 'bayes.pkl')
        )

    def _get_storage(self):
        return joblib.load(self.storage_name)

    def train(self, inputs, outputs):
        merged = [self._merge(i) for i in inputs]
        self.clf = Pipeline(
            [('vect', CountVectorizer()),
             ('clf', MultinomialNB())]
        )
        self.clf.fit(merged, outputs)
        joblib.dump(self.clf, self.storage_name)

    def _check_clf(self):
        if self.clf is None:
            try:
                self.clf = self._get_storage()
            except IOError:
                raise UntrainedModelError

    def predict_one(self, one):
        self._check_clf()
        return self.clf.predict(self._merge(one))

    def predict_many(self, inputs):
        self._check_clf()
        return self.clf.predict([self._merge(i) for i in inputs])

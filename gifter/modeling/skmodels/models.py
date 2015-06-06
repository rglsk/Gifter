import os

from sklearn.externals import joblib
from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfTransformer
)
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV

from gifter.modeling.models import MergingBaseModel
from gifter.errors import UntrainedModelError
from gifter.config import DATA_DIRECTORY


class BaseSkModel(MergingBaseModel):

    def _get_storage(self):
        return joblib.load(self.storage_name)

    def _check_clf(self):
        if self.clf is None:
            try:
                self.clf = self._get_storage()
            except IOError:
                raise UntrainedModelError

    def train(self, inputs, outputs):
        merged = [self._merge(i) for i in inputs]
        self.clf.fit(merged, outputs)
        joblib.dump(self.clf, self.storage_name)

    def predict_one(self, one):
        self._check_clf()
        return self.clf.predict(self._merge(one))

    def predict_many(self, inputs):
        self._check_clf()
        return self.clf.predict([self._merge(i) for i in inputs])


class BayesModel(BaseSkModel):

    def __init__(self):
        super(BayesModel, self).__init__(
            'BayesModel',
            os.path.join(DATA_DIRECTORY, 'skmodels', 'bayes.pkl')
        )

    def train(self, inputs, outputs):
        self.clf = Pipeline(
            [('vect', CountVectorizer()),
             ('clf', MultinomialNB())]
        )
        super(BayesModel, self).train(inputs, outputs)


class SGDModel(BaseSkModel):

    def __init__(self):
        super(SGDModel, self).__init__(
            'SGDModel',
            os.path.join(DATA_DIRECTORY, 'skmodels', 'sgd.pkl')
        )

    def train(self, inputs, outputs):
        self.clf = Pipeline(
            [('vect', CountVectorizer()),
             ('tfidf', TfidfTransformer()),
             ('clf', SGDClassifier(alpha=0.001))]
        )
        super(SGDModel, self).train(inputs, outputs)

    def search_parameters(self, inputs, outputs):
        merged = [self._merge(i) for i in inputs]
        parameters = {
            'vect__ngram_range': [(1, 1), (1, 2), (1, 3)],
            'tfidf__use_idf': (True, False),
            'clf__alpha': (1e-1, 1e-2, 1e-3, 1e-4, 1e-5),
        }
        self.clf = Pipeline(
            [('vect', CountVectorizer()),
             ('tfidf', TfidfTransformer()),
             ('clf', SGDClassifier())]
        )
        gs_clf = GridSearchCV(self.clf, parameters, n_jobs=-1)
        gs_clf = gs_clf.fit(merged[:400], outputs[:400])
        best_parameters, score, _ = max(
            gs_clf.grid_scores_,
            key=lambda x: x[1]
        )
        for param_name in sorted(parameters.keys()):
            print("%s: %r" % (param_name, best_parameters[param_name]))
        print score

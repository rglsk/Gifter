import sys
from itertools import izip
import json

import numpy as np
import pandas as pd

from gifter.utils import get_data_file_path
from gifter.modeling.models import BaseModel
from gifter.modeling.evaluation.separate import separeted_data
from gifter.config import TOPIC_NUMBER
from gifter.modeling.llda.llda_usage import count_words
from gifter.modeling.llda.llda import LLDA


class LldaModel(BaseModel):

    def __init__(self, alpha=0.001, beta=0.001):
        super(LldaModel, self).__init__('LLDA', 'storage_name')
        (self.inputs_train, self.inputs_test, self.output_train,
            self.output_test) = separeted_data(test_size=0.7)
        self.inputs_test.to_json('inputs_test.json')
        self.output_train.to_json('inputs_train.json')

        self.llda = LLDA(TOPIC_NUMBER, alpha, beta)

    def _get_storage(self):
        return

    def save_model(self, labelset):
        phi = self.llda.phi()
        results = {}
        for k, label in enumerate(labelset):
            results[label] = {}
            for w in np.argsort(-phi[k])[:20]:
                results[label][self.llda.vocas[w]] = phi[k, w]
        with open(get_data_file_path('train_results.json'), 'w+') as outfile:
            json.dump(results, outfile)

    def train(self):
        corpus = []
        zipped_data = izip(self.inputs_train.preprocessed_filename,
                           self.output_train)
        for train_path, category in zipped_data:
            tweets_df = pd.read_json(train_path)
            corpus.append(tweets_df.lemmas.sum())

        labels = [[key] for key in self.output_train]
        labelset = list(set(reduce(list.__add__, labels)))

        self.llda.set_corpus(labelset,
                             corpus,
                             labels)
        print "M={}, V={}, L={}, K={}".format(len(corpus),
                                              len(self.llda.vocas),
                                              len(labelset),
                                              TOPIC_NUMBER)

        for i in range(50):
            sys.stderr.write("-- %d : %.4f\n" % (i, self.llda.perplexity()))
            self.llda.inference()
        print "perplexity : %.4f" % self.llda.perplexity()

        self.save_model(labelset)

    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        with open(get_data_file_path('train_results.json'), 'r') as jj:
            results = json.load(jj)

        lemmatized_words = one.lemmas.sum()
        counted_words = count_words(lemmatized_words)
        counted_words.sort(ascending=False)
        category_results = {i.lower(): 0 for i in results.keys()}

        for ww, count in counted_words.iteritems():
            for category, result in results.iteritems():
                for word, weight in result.iteritems():
                    if ww == word:
                        category_results[category] += count * weight
        return pd.Series(category_results).idxmax()

    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return [self.predict_one(_input) for _input in inputs]

import sys
from itertools import izip

import numpy as np
import pandas as pd

from gifter.modeling.models import BaseModel
from gifter.modeling.evaluation.separate import separeted_data
from gifter.config import TOPIC_NUMBER
from gifter.modeling.llda.llda import LLDA


class LldaModel(BaseModel):

    def __init__(self, alpha, beta):
        super(LldaModel, self).__init__('LLDA', 'storage_name')
        (self.inputs_train, self.inputs_test, self.output_train,
            self.output_test) = separeted_data()

        self.llda = LLDA(TOPIC_NUMBER, alpha, beta)

    def _get_storage(self):
        return

    def train(self):
        training_set = {category: [] for category in self.output_train}
        zipped_data = izip(self.inputs_train.preprocessed_filename,
                           self.output_train)
        for train_path, category in zipped_data:
            tweets_df = pd.read_json(train_path)
            training_set[category] += (tweets_df.lemmas.sum())

        corpus = training_set.values()
        labels = [[key] for key in training_set.keys()]
        labelset = list(set(reduce(list.__add__, labels)))
        print 'poszlo'
        self.llda.set_corpus(labelset,
                             corpus,
                             labels)
        print "M={}, V={}, L={}, K={}".format(len(corpus),
                                              len(self.llda.vocas),
                                              len(labelset),
                                              TOPIC_NUMBER)

        for i in range(TOPIC_NUMBER):
            sys.stderr.write("-- %d : %.4f\n" % (i, self.llda.perplexity()))
            self.llda.inference()
        print "perplexity : %.4f" % self.llda.perplexity()

        phi = self.llda.phi()
        for k, label in enumerate(labelset):
            print "\n-- label %d : %s" % (k, label)
            for w in np.argsort(-phi[k])[:20]:
                print "%s: %.4f" % (self.llda.vocas[w], phi[k, w])

    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        return

    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return



if __name__ == '__main__':
    llda = LldaModel(alpha=0.001, beta=0.001)
    llda.train()
    import ipdb; ipdb.set_trace()
from itertools import izip

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

    def train(self):
        training_set = {category: [] for category in self.output_train}
        for train_path, category in izip(self.inputs_train, self.output_train):
            tweets_df = pd.read_json(train_path)
            training_set[category] += (tweets_df.lemmas.sum())

        labelset = set(training_set.keys())
        self.llda.set_corpus(labelset,
                             training_set.values(),
                             training_set.keys())

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

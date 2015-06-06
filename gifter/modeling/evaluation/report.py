import pandas as pd
from sklearn.metrics import classification_report

from gifter.modeling.evaluation.separate import separeted_data
from gifter.modeling.word2vec.model import Word2VecModel
from gifter.modeling.skmodels.models import (
    BayesModel,
    SGDModel,
)

# Insert here classes
METHODS = [SGDModel]


def create_report():
    inputs_train, inputs_test, output_train, output_test = separeted_data()
    for method in METHODS:
        # training
        model = method()
        model.train(
            map(pd.read_json, inputs_train.preprocessed_filename),
            output_train
        )

        predicted = model.predict_many(
            map(pd.read_json, inputs_test.preprocessed_filename)
        )
        print model.name
        print classification_report(
            output_test,
            predicted,
        )

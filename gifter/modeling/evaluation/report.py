import random

import pandas as pd
from sklearn.metrics import classification_report

from gifter.utils import get_category_from_filepath
from gifter.modeling.llda.model import LldaModel
from gifter.modeling.evaluation.separate import separeted_data
from gifter.modeling.word2vec.model import Word2VecModel
from gifter.modeling.skmodels.models import (
    BayesModel,
    LinearSVCModel,
)

# Insert here classes
METHODS = [LinearSVCModel]


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


def llda_report():
    inputs_test = pd.read_json('trol.json')
    llda = LldaModel()
    preprocessed = random.sample(inputs_test.preprocessed_filename.tolist(),
                                 494)
    output_test = map(get_category_from_filepath, preprocessed)

    predicted = llda.predict_many(
        [pd.read_json(filename) for filename in preprocessed]
    )
    print llda.name
    print classification_report(
        output_test,
        predicted,
    )

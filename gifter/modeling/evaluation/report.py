from collections import OrderedDict
import pandas as pd
from sklearn.metrics import classification_report

from gifter.modeling.evaluation.separate import separeted_data
from gifter.modeling.word2vec.model import Word2VecModel
from gifter.modeling.models import BaseModel


# Insert here classes
METHODS = [Word2VecModel]


def class_mapper():
    return OrderedDict(
        [(key, value) for value, key in enumerate(BaseModel.CLASSES.name.ravel())]
    )


def create_report():
    inputs_train, inputs_test, output_train, output_test = separeted_data()
    for method in METHODS:
        # training
        model = method()
        model.train(inputs_train, output_train)

        # get outputs
        preprocessed = inputs_test.preprocessed_filename.tolist()
        predicted = model.predict_many(
            [pd.read_json(filename) for filename in preprocessed]
        )
        print model.name
        print classification_report(
            output_test,
            predicted,
        )

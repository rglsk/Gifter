import random

import pandas as pd
from sklearn.metrics import classification_report

from gifter.utils import get_category_from_filepath
from gifter.utils import get_data_file_path
from expermiental.llda.model import LldaModel


def llda_report():
    inputs_test = pd.read_json(get_data_file_path('inputs_test.json'))
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

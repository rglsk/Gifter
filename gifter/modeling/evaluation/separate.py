from sklearn import cross_validation
import pandas as pd

from gifter.crawlers.suggested import files_by_categories


def separeted_data(test_size=0.3):
    df = pd.DataFrame(
        list(files_by_categories()),
        columns=['slug', 'filename', 'preprocessed_filename']
    )
    inputs = df[['filename', 'preprocessed_filename']]
    outputs = df['slug'].ravel()

    return cross_validation.train_test_split(
        inputs,
        outputs,
        test_size=test_size
    )

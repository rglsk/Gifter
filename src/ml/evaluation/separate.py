from sklearn import cross_validation
import pandas as pd

from crawlers.suggested import files_by_categories


def get_evaluation_df():
    return pd.DataFrame(
        list(files_by_categories()),
        columns=['slug', 'filename', 'preprocessed_filename']
    )


def separeted_data(test_size=0.25):
    df = get_evaluation_df()
    inputs = df[['filename', 'preprocessed_filename']]
    outputs = df['slug'].ravel()

    return cross_validation.train_test_split(
        inputs,
        outputs,
        test_size=test_size,
        random_state=0
    )

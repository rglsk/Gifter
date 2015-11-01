from itertools import izip
import pandas as pd

from gifter.modeling.models import MergingBaseModel
from gifter.config import LLDA_TRAIN_DIRECTORY


def create_train_documents(train_paths, train_category):

    for train_path, category in izip(train_paths, train_category):
        with open('/'.join([LLDA_TRAIN_DIRECTORY,
                            train_category]), 'a+') as tf:
            tweets_df = pd.read_json(train_path)
            if train_category.upper() not in tf.read(20):
                tf.write(train_category.upper()+'\n')

            tf.write(MergingBaseModel._merge(tweets_df)+' ')


def train(train_paths, train_category):
    for train_path, category in izip(train_paths, train_category):
        pass

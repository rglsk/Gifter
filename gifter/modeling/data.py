from gifter.modeling.tokenizer import (
    lemmatize,
    preprocess
)
import pandas as pd


def lemmatize_by_row(row):
    return lemmatize(preprocess(*row))


def lemmatized_frame(filename="./data.json"):
    df = pd.io.json.read_json(filename)
    df['lemmas'] = df[['text', 'entities']].apply(lemmatize_by_row, axis=1)
    return df

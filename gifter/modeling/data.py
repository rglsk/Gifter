from gifter.modeling.tokenizer import (
    lemmatize,
    preprocess
)
import pandas as pd


def lemmatize_by_row(row, with_tags=True):
    return lemmatize(preprocess(*row), with_tags)


def lemmatized_frame(filename="../data/data.json", last_rows=300, with_tags=True):
    df = pd.io.json.read_json(filename)
    df = df[df.lang == 'en']  # only en
    df.sort('created_at', ascending=False, inplace=True)
    df = df[:last_rows]
    df['lemmas'] = df[['text', 'entities']].apply(
        lambda row: lemmatize_by_row(row, with_tags),
        axis=1
    )
    return df[df['lemmas'].apply(len) > 0]

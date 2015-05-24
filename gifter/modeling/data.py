from gifter.modeling.tokenizer import (
    lemmatize,
    preprocess
)
import pandas as pd


def lemmatize_by_row(row, with_tags=True):
    return lemmatize(preprocess(*row), with_tags)


def lemmatized_frame(filename="../data/data.json", last_rows=300, with_tags=True):
    df = pd.read_json(filename)
    df.sort('created_at', ascending=False, inplace=True)
    df = df[df.lang == 'en']  # only en
    df = df[:last_rows]

    # bug in pandas it's a hack
    df['text_len'] = df.text.map(len)
    df.sort('text_len', ascending=False, inplace=True)

    df['lemmas'] = df[['text', 'entities']].apply(
        lambda row: lemmatize_by_row(row, with_tags),
        axis=1
    )
    return df[df['lemmas'].apply(len) > 0]

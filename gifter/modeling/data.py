import pandas as pd

from gifter.modeling.tokenizer import (
    lemmatize,
    preprocess
)


def lemmatize_by_row(row, with_tags=True):
    return lemmatize(preprocess(*row), with_tags)


def lemmatized_frame(filename="../data/data.json", last_rows=300, with_tags=True):
    df = pd.read_json(filename)
    df = df[df.lang == 'en']  # only en

    df.sort('created_at', ascending=False, inplace=True)
    df.reset_index(inplace=True)
    df = df[:last_rows+10]

    # bug in pandas it's a hack
    df['text_len'] = df.text.map(lambda text: len(text.split()))
    df.sort('text_len', ascending=False, inplace=True)
    df.reset_index(inplace=True)
    df['lemmas'] = df[['text', 'entities']].apply(
        lambda row: lemmatize_by_row(row, with_tags),
        axis=1
    )

    df = df[:last_rows]
    return df[df['lemmas'].apply(len) > 0]

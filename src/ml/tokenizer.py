import re
from itertools import chain

import gensim
from unidecode import unidecode

from gensim.parsing.preprocessing import STOPWORDS

CAMMEL_CASE_PATTERN = re.compile("([a-z])([A-Z])")


def mentions(entities):
    return [
        "@{}".format(user.get('screen_name', ''))
        for user in entities.get('user_mentions', [])
    ]


def links(entities):
    urls = {
        'media': [media.get('url', '',) for media in entities.get('media', [])],
        'other': [obj.get('url', '') for obj in entities.get('urls', [])],
    }
    return chain(*urls.values())


def hashtags(entities):
    return [
        tag['text'] for tag in entities.get('hashtags', [])
    ]


def camel_case_to_text(camel):
    return CAMMEL_CASE_PATTERN.sub(
        "\g<1> \g<2>",
        camel
    )


def preprocess(text, entities):
    """
    * text to unicode
    * remove rt
    * remove hashtags and replace them with text
    * remove mentions (@)
    * remove links
    """
    text = unidecode(text.strip())
    hashtag_list = hashtags(entities)
    ignored = chain(
        mentions(entities),
        links(entities),
        hashtag_list,
    )
    to_remove = "|".join(ignored)
    pattern = re.compile("(#|RT |{})".format(unidecode(to_remove)), re.I)
    hashtag_text = " ".join(map(camel_case_to_text, hashtag_list))
    return " ".join([
        pattern.sub("", text),
        hashtag_text
    ])


def lemmatize(text, with_tags=True):
    lemmas = gensim.utils.lemmatize(text)
    if with_tags:
        return [lemma for lemma in lemmas if lemma[:-3] not in STOPWORDS]
    return [lemma[:-3] for lemma in lemmas if lemma[:-3] not in STOPWORDS]


if __name__ == '__main__':
    # example usage
    import pandas as pd
    tweets = pd.io.json.read_json("./data.json")
    for i in range(20):
        row = tweets.ix[i]
        print "-"*40
        print "Original: ", row['text']
        print "Preprocessed: ", preprocess(row['text'], row['entities'])
        print "Lemmatized: ", lemmatize(
            preprocess(row['text'], row['entities'])
        )

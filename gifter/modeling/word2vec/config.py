import os

from nltk.corpus import (
    brown,
    movie_reviews,
    treebank
)
from gensim.models.word2vec import Text8Corpus
from gifter.config import DATA_DIRECTORY

CORPUS_DIR = os.path.join(DATA_DIRECTORY, 'word2vec', 'corpus')
MODELS_DIR = os.path.join(DATA_DIRECTORY, 'word2vec', 'model')


MODELS = {
    'brown': {
        'corpus': brown.sents(),
        'model': os.path.join(MODELS_DIR, 'brown.bin')
    },
    'movie_reviews': {
        'corpus': movie_reviews.sents(),
        'model': os.path.join(MODELS_DIR, 'movie_reviews.bin')
    },
    'treebank': {
        'corpus': treebank.sents(),
        'model': os.path.join(MODELS_DIR, 'treebank.bin')
    },
    'text8': {
        'corpus': Text8Corpus(os.path.join(CORPUS_DIR, 'text8')),
        'model': os.path.join(MODELS_DIR, 'text8.bin')
    },
    'enwiki': {
        'corpus': Text8Corpus(os.path.join(CORPUS_DIR, 'enwiki_corpus')),
        'model': os.path.join(MODELS_DIR, 'enwiki.bin')
    },
    'google': {
        'corpus': None,
        'model': os.path.join(MODELS_DIR, 'google.bin.gz')
    }
}

import os

from nltk.corpus import (
    brown,
    movie_reviews,
    treebank
)
from gensim.models.word2vec import Text8Corpus
from gensim.models import Word2Vec

from core.config import DATA_DIRECTORY
from experimental.word2vec.pretrained_models import MODELS

CORPUS_DIR = os.path.join(DATA_DIRECTORY, 'word2vec', 'corpus')

CORPUS = {
    'brown': brown.sents(),
    'movie_reviews': movie_reviews.sents(),
    'treebank': treebank.sents(),
    'text8': Text8Corpus(os.path.join(CORPUS_DIR, 'text8')),
    'enwiki': Text8Corpus(os.path.join(CORPUS_DIR, 'enwiki_corpus')),
}


def train_word2vec():
    for name, corpus in CORPUS.iteritems():
        model = Word2Vec(corpus, size=200, workers=4)
        model.save_word2vec_format(MODELS[name], binary=True)

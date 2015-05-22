import os
from gensim.models import Word2Vec
from gifter.config import DATA_DIRECTORY


MODELS_DIR = os.path.join(DATA_DIRECTORY, 'word2vec', 'model')
MODELS = {
    'brown': os.path.join(MODELS_DIR, 'brown.bin'),
    'movie_reviews': os.path.join(MODELS_DIR, 'movie_reviews.bin'),
    'treebank': os.path.join(MODELS_DIR, 'treebank.bin'),
    'text8': os.path.join(MODELS_DIR, 'text8.bin'),
    'enwiki': os.path.join(MODELS_DIR, 'enwiki.bin'),
    'google': os.path.join(MODELS_DIR, 'google.bin.gz')
}


def get_by_name(name):
    path = MODELS.get(name)
    if path:
        return Word2Vec.load_word2vec_format(path, binary=True)

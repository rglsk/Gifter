from gensim.models import Word2Vec
from gifter.modeling.word2vec.config import MODELS


def train_word2vec():
    for name, config in MODELS.iteritems():
        if config['corpus']:
            model = Word2Vec(config['corpus'], size=200, workers=4)
            model.save_word2vec_format(config['model'], binary=True)


def get_by_name(name):
    config = MODELS.get(name)
    if config:
        return Word2Vec.load_word2vec_format(config['model'], binary=True)

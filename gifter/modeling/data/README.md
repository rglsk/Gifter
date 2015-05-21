# Downloading Data

NLTK:
```
$ ipython
In [1]: import nltk; nltk.download()
```

Preprocess wikipedia example::
```
perl wikifil.pl ./word2vec/corpus/enwik9 > ./word2vec/corpus/enwiki_corpus
```

## Word2Vec
NLTK:
Choose `corpora` and download:
* brown
* movie_reviews
* treebank

External corpses:
* [text8](http://mattmahoney.net/dc/text8.zip)
* [enwiki](https://code.google.com/p/word2vec/#Where_to_obtain_the_training_data)

After downloading move files into `./word2vec/corpus/`

Ready pretrained (100 billion words) corpus from Google:
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing

Move it into `./word2vec/model/`

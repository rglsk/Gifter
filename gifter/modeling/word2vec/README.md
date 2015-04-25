## HOWTO

### Running locally

```
$ ipython
In [1]: import nltk; nltk.download()
```

Choose `corpora` and download:
* brown
* movie_reviews
* treebank

External corpses:
* [text8](http://mattmahoney.net/dc/text8.zip).
* [enwiki](https://code.google.com/p/word2vec/#Where_to_obtain_the_training_data)
After downloading move file into this directory.

To preprocess wikipedia:
```
perl wikifil.pl enwik9 > enwiki_corpus
```

Run notebooks :)

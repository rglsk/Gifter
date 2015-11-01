#!/usr/bin/env python
import itertools
import gensim
from gensim import corpora, models
from ml.tokenizer import lemmatize
import pandas as pd


def lda(
    list_of_json=["../data/data.json", "../data/data2.json"],
    documents_list=[],
    num=24,
    passes=100,
    save_model_as='lda.model',
    save_dic_as='dictionary.dic'
):
    texts2 = []
    if not documents_list:
        texts2 = list_of_json
    else:
        texts2 = []
        for d in documents_list:
            texts2 = texts2 + [lemmatize(text=d, with_tags=False)]
    dictionary = corpora.Dictionary(texts2)
    print "Made dictionary"
    dictionary.save(save_dic_as)
    corpus = [dictionary.doc2bow(text) for text in texts2]
    corpora.MmCorpus.serialize('../lda/corpus.mm', corpus)
    mm_corpus = corpora.MmCorpus('../lda/corpus.mm')
    print "mm_corpus: " + str(mm_corpus)
    id2word = {}
    for word in dictionary.token2id:
        id2word[dictionary.token2id[word]] = word
    print "Made id2word"
    lda = gensim.models.ldamulticore.LdaMulticore(
        corpus=mm_corpus,
        num_topics=num,
        id2word=id2word,
        passes=passes,
        workers=1
    )
    lda.save(save_model_as)
    for i in range(0, lda.num_topics):
        print(
            "Topic number " +
            str(i) + " consists of words : " + lda.print_topic(i)
        )
    return lda, dictionary


def count_words(lemmatized_words):
    return {word: lemmatized_words.count(word) for word in lemmatized_words}


def learned_categories(
    train=[],
    out=[],
    dictionary='dictionary.dic',
    lda='lda.model'
):
    res = {i: [] for i in xrange(0, 24)}
    result = []
    for document, output in zip(train, out):
        t = find_topic(
            frame=document,
            dictionary='dictionary.dic',
            lda='lda.model'
        )
        if (t[0][0]):
            res[t[0][0]].append(output)
    for i in res.keys():
        if len(res[i]) > 0:
            a = sorted(
                count_words(res[i]).values(), reverse=True
            )[0]
            for key, value in count_words(res[i]).iteritems():
                if (value == a):
                    result.append(key)
                    a = a + 1
        else:
            result.append(u'science')
    return result


def find_topic(
    frame=pd.io.json.read_json("../data/data.json"),
    dictionary='../lda/dictionary2.dic',
    lda='../lda/lda2.model'
):
    df = frame
    new_doc = list(
        itertools.chain(
            *[df['lemmas'].irow(i) for i in range(df.shape[0])]
        )
    )
    l2 = models.LdaModel.load(lda)
    dic2 = corpora.Dictionary.load(dictionary)
    new_vec = dic2.doc2bow(new_doc)
    vec_lda = sorted(l2[new_vec], key=lambda vec: vec[1], reverse=True)
    return vec_lda

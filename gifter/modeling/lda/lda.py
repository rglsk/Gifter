# coding: utf-8

import itertools
import gensim
from gifter.modeling.data import lemmatized_frame
from gifter.modeling.tokenizer import lemmatize
from gensim import corpora


def LDA(texts=["default"], num=2, passes=100):
    if (texts == ["default"]):
        df = lemmatized_frame("../data.json", with_tags=False)
        texts = [df['lemmas'].irow(i) for i in range(df.shape[0])]
    else:
        texts2 = []
        for d in texts:
            texts2 = texts2 + [lemmatize(d, with_tags=False)]
            texts = texts2
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('./corpus.mm', corpus)
    mm_corpus = corpora.MmCorpus('./corpus.mm')
    id2word = {}
    for word in dictionary.token2id:
        id2word[dictionary.token2id[word]] = word
    lda = gensim.models.ldamulticore.LdaMulticore(
        corpus=mm_corpus,
        num_topics=num,
        id2word=id2word,
        eval_every=1,
        passes=passes,
        workers=1
    )
    for i in range(0, lda.num_topics):
        print "Topic number " + str(
            i
        ) + " consists of words : " + lda.print_topic(i)
    return lda, dictionary

l, dic = LDA()

documents = [
    "Apple is releasing a new product",
    "I love apple",
    "Amazon sells many things",
    "Microsoft announces Nokia acquisition",
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey"
]

D = [
    "I like to eat broccoli and bananas.",
    "I ate a banana and spinach smoothie for breakfast.",
    "Chinchillas and kittens are cute.",
    "My sister adopted a kitten yesterday.",
    "Look at this cute hamster munching on a piece of broccoli."
]

l, dic = LDA(texts=D, num=2)

l, dic = LDA(texts=documents, num=2)


def find_topic(new_doc="User", dictionary=dic, lda=l):
    if (new_doc == "User"):
        df = lemmatized_frame("../data.json", with_tags=False)
        new_doc = list(
            itertools.chain(
                *[df['lemmas'].irow(i) for i in range(df.shape[0])]
            )
        )
    else:
        new_doc = new_doc.lower().split()
    new_vec = dictionary.doc2bow(new_doc)
    vec_lda = sorted(lda[new_vec], key=lambda vec: vec[1], reverse=True)
    print str(vec_lda)
    print "Top topic is topic number " + str(
        vec_lda[0][0]
    ) + " consists of words : " + lda.print_topic(vec_lda[0][0])
    return vec_lda


find_topic()

find_topic(
    "I love watching films with my family and friends. I will write review of the film we watched yesterday"
)

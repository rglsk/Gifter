# coding: utf-8
import pandas as pd
import matplotlib.pylab as plt
from gifter.modeling.evaluation.separate import get_evaluation_df


def all_tweets_stats(all_df):
    overall_sum = 0
    hashtag_sum = 0
    users = 0
    for filename in all_df.filename:
        users += 1
        df = pd.read_json(filename)
        overall_sum += len(df)
        hashtag_sum += df.entities.map(lambda e: len(e.get('hashtags'))).sum()

    print "Tweets: {}\nHashtags: {}\nUsers: {}".format(
        overall_sum,
        hashtag_sum,
        users
    )


def stats():
    df = get_evaluation_df()
    all_tweets_stats(df)
    print "User distribution:"
    counts = df.groupby('slug')['filename'].count()
    print counts
    plt.figure(figsize=(20, 19.5))
    counts.plot(kind='bar', lw=2)
    plt.title(u"Rozkład tweetów", fontsize=36)
    plt.xlabel(u"Kategorie", fontsize=36)
    plt.ylabel(u"Liczba użytkowników", fontsize=36)
    plt.ylim(0, 105)
    plt.savefig("distribution.jpg")

    print "Processed tweets (new):"
    print df.preprocessed_filename.map(pd.read_json).map(len).sum()

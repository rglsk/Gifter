import tweepy
import pandas as pd

from gifter.config import TWITTER_AUTH


def setup_twitter_api():
    return tweepy.API(
        TWITTER_AUTH,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
    )


def timeline(api, screen_name):
    cur = tweepy.Cursor(
        api.user_timeline,
        screen_name=screen_name,
        count=200,

    )
    for tweet in cur.items():
        yield tweet._json


def main():
    api = setup_twitter_api()
    tweets = list(timeline(api, "fk_lx"))
    df = pd.DataFrame(tweets)
    df.to_json("gifter/modeling/data.json")

import tweepy
import pandas as pd

from gifter.config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)


def setup_twitter_api():
    twitter_auth = tweepy.OAuthHandler(
        TWITTER_CONSUMER_KEY,
        TWITTER_CONSUMER_SECRET
    )
    twitter_auth.set_access_token(
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )

    return tweepy.API(
        twitter_auth,
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
    df = pd.DataFrame(list(timeline(api, "fk_lx")))
    df.to_json("gifter/modeling/data.json")

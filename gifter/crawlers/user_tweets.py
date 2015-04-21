import tweepy
import pandas as pd
import argparse
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


def get_user_tweets(screen_name):
    api = setup_twitter_api()
    tweets = list(timeline(api, screen_name))
    return pd.DataFrame(tweets)


def main():
    parser = argparse.ArgumentParser(prog="Twitter crawler")
    parser.add_argument("screen_name", type=str)

    args = parser.parse_args()
    df = get_user_tweets(args.screen_name)
    df.to_json("gifter/modeling/data.json")

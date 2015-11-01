import tweepy

from core.config import setup_twitter_api


def parse_friend(friend):
    """Cuts unneeded friend info.

    :param friend: Friend data (Dict)

    Returns parsed friend data (Dict)
    """
    friend_data = ['id', 'name', 'screen_name']
    return {key: friend[key] for key in friend_data}


def iter_friends(api, screen_name):
    """Creates iterator for user friends."""
    cur = tweepy.Cursor(api.friends,
                        screen_name=screen_name,
                        count=200)
    for tweet in cur.items():
        yield parse_friend(tweet._json)


def get_user_friends(screen_name):
    """Get friends of the user by his screen name

    :param screen_name: Twitter screen name (String)

    Returns list of friends. Each friend contain only id, name and screen_name.
    """
    api = setup_twitter_api()
    return list(iter_friends(api, screen_name))

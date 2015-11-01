import tweepy
from gifter.config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Searching for the recipent
search_user = raw_input('Enter a name of  recipient: ')
list_of_finded_users = api.search_users(search_user)

if api.search_users(search_user) == []:
    print("We can not find such person on Twitter.")
else:
    # Printing all fitting users
    for user in list_of_finded_users:
        if user.location:
            print("Location of user: " + user.screen_name + " is " +
                  user.location)
        print(api.get_user(user.screen_name).profile_image_url)
        print "User screen name is: " + user.screen_name
    recipient = list_of_finded_users[0]
    print(api.get_user(recipient.screen_name))
    print(api.get_user(recipient.screen_name).profile_image_url)

    # Saving status of recipent in a text file
    with open("document_with_status.txt", 'w') as document_with_status:
        for status in tweepy.Cursor(api.user_timeline,
                                    id=recipient.id,
                                    page=1).items(20):
            print(status)
            print >> document_with_status, status

    # Print all people that recipient is following
        for friend in recipient.friends():
            print(friend.screen_name)

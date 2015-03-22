import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'gHWOQbi5Yu2CDhFQV115gDeBx'
consumer_secret = 'zrL9nqFiMBiTRPnCSwroFwLHBejoPJ22T5U1hamTYR4AzWIQq3'
access_token = '3102685905-pHHlMPIFkyRKJ7cF0OOaYqAyXNy6kwjoUyQqq2R'
access_token_secret = 'osREvPUPuQPtZPMADHzLpPLQ0zaE1crw5HTCGUJCZGSoJ'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

search_user = raw_input('Enter a name of  recipient: ')
list = api.search_users(search_user)
    
for user in list:
    if bool(user.location):
        print "Location of user: " + user.screen_name + " is " + user.location
    print user.screen_name

recipient = list[0]
recipient.screen_name
out = open("a.txt", 'w')

for status in tweepy.Cursor(api.user_timeline,id=recipient.id,page=1).items(20):
    print(status)
    print >> out,status

out.close()

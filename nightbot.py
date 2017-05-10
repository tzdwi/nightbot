import os
import time

from markovbot35 import MarkovBot

# Initialise a MarkovBot instance
nightbot = MarkovBot() # Fighter of the day bot

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the phrases
nighttext = os.path.join(dirname, u'nightlunch.txt')
# Make the bot read the file!
nightbot.read(nighttext)

# Make a file to write some sample tweets to
trial_tweets = open('tweet_samples.txt','w+')

#Generate 100 tweets
for i in range(100):
    
    tweet = nightbot._construct_tweet(suffix = '#NightLunch')
    trial_tweets.write(tweet+'\n')

trial_tweets.close()

# The MarkovBot uses @sixohsix' Python Twitter Tools, which is a Python wrapper
# for the Twitter API. Find it on GitHub: https://github.com/sixohsix/twitter

# ALL YOUR SECRET STUFF!
# Make sure to replace the ''s below with your own values, or try to find
# a more secure way of dealing with your keys and access tokens. Be warned
# that it is NOT SAFE to put your keys and tokens in a plain-text script!

# Consumer Key (API Key)
# cons_key = ''
# Consumer Secret (API Secret)
# cons_secret = ''
# Access Token
# access_token = ''
# Access Token Secret
# access_token_secret = ''

# Log in to Twitter
# nightbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start periodically tweeting. This will post a tweet once every day
# nightbot.twitter_tweeting_start(days=1, hours = 0, minutes = 0, keywords=None, prefix='We are Nightlunch and', suffix='#NightLunch')

# DO SOMETHING HERE TO ALLOW YOUR BOT TO BE ACTIVE IN THE BACKGROUND
# You could, for example, wait for a week:
# isecsinweek = 7 * 24 * 60 * 60
# time.sleep(secsinweek)

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
# nightbot.twitter_tweeting_stop()

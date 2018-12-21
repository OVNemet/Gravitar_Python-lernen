# Import libraries
import tweepy
from twitter_credentials import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot

# Authentification
auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecretKey)

api = tweepy.API(auth)
tweets = api.user_timeline(screen_name = 'antena3', count = 500, include_rts = False, tweet_mode = 'extended')

text = ''

for tweet in tweets:
    text = text + ' ' + tweet.full_text

# Set up the wordcloud variable
wordcloud = WordCloud(width=1920, height=1200)

# Ignore words
STOPWORDS.update(['https', 'co', 'de', 'la', 'din', 'în', 'și' , 'să' ,'pe', 'pentru', 'ce', 'care', 'cu', 'se', 'mai', 'despre', 'un', 'nu', 'că'])

# Generate the wordcloud text
wordcloud.generate(text)

# Use matplotlib to visualize the words
pyplot.imshow(wordcloud, interpolation='bilinear')
pyplot.axis('off')
pyplot.show()
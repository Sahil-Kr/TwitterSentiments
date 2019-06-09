import tweepy
from textblob import TextBlob
import csv

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_sentiment(analysis, threshold=0):
	if analysis.sentiment.polarity>threshold:
		return 'positive'
	else:
		return 'negative'

csvClmn=[['Tweet', 'Sentiment']]

public_tweets = api.search('Game of Thrones', count=100)

with open('sentiment.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvClmn)

    for tweet in public_tweets:
    	analysis = TextBlob(tweet.text)
    	writer.writerows([[tweet.text.encode('ascii', errors="ignore"), get_sentiment(analysis)]])
    	
csvFile.close()
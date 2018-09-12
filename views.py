from django.shortcuts import render
import tweepy
from textblob import TextBlob
from main.forms import TweetTag

def tweet_by_word(request):

    MyTweetForm =  TweetTag(request.POST)
    tweet_tag = request.POST.get("tweet_tag")


    consumer_key = "DIbCUqzmiIn0Uhvfa70eOngYs"
    consumer_secret = "LlpBf9pdTy5Sa8N9cij6LB9EgRXp5W3JPzQg2UkrXdr2AtO9U8"

    access_token = "1038681516245569536-5sfNR7ezc8wSST92Aq7zU4jRt29n97"
    access_token_secret = "rNUstvTLSeH1eoNqd4elTDalXUFvbA4hNNLgulPmONnge"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.search(tweet_tag,count=20,tweet_mode="extended")
    tweet_list = []
    analysis_list = []
    tweet_info = []
    for tweet in public_tweets:
        tweet_list.append(tweet.full_text)
        analysis = TextBlob(tweet.full_text)
        analysis_list.append(analysis.sentiment)
        tweet_info = zip(tweet_list,analysis_list)
    return render(request, 'tweet_by_word_print.html', {'tweet_info': tweet_info})

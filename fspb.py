# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 00:23:34 2018

@author: Denis
"""
    
from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy        
import time
import json
import keys

# Authenticate
CONSUMER_KEY = keys.CONSUMER_KEY
CONSUMER_SECRET = keys.CONSUMER_SECRET
ACCESS_KEY = keys.ACCESS_KEY
ACCESS_SECRET = keys.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
myBot = api.get_user(screen_name = "@freespeechbot")

"""
#search = ("#internetBeerdigung OR #internetFuneral OR #RetteDeinInternet since:2018-11-20")
search = "#internetBeerdigung OR #internetFuneral OR #RetteDeinInternet -filter:retweets" 

for tweet in tweepy.Cursor(api.search, q=search).items():
    print('\nTweet by: @' + tweet.user.screen_name)
    print("Tweet message: " + str(tweet.text.encode('utf-8', 'ignore')))
    print("Tweet retweeted: " + str(tweet.retweeted))
    print("Tweet favorited: " + str(tweet.favorited))
    print("User followed: " + str(tweet.user.following))
""" 



class StdOutListener(StreamListener):
    """ #A listener handles tweets that are received from the stream.
    #This is a basic listener that just prints received tweets to stdout.
"""
    def on_data(self, data):
        
        python_obj = json.loads(data)
        print(python_obj["id"])
        print(python_obj["user"]["screen_name"])
        print(python_obj["text"])
        
        try:
            if python_obj["favorited"] == False:
                api.create_favorite(python_obj["id"])
                print("liked")
        except tweepy.TweepError:
            print("already liked")
            time.sleep(2)
            pass
        
        
        try:
            if python_obj["retweeted"] == False:
                api.retweet(python_obj["id"])
                print("retweeted")
        except tweepy.TweepError:
            print("already retweeted")
            time.sleep(2)
            pass
            
        try:
            if python_obj["user"]["following"] == None:
                api.create_friendship(python_obj["user"]["id"])
                print("followed")
        except tweepy.TweepError:
            print("already followed")
            time.sleep(2)
            pass
        
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    stream = Stream(auth, l)
    stream.filter(track=["#internetBeerdigung", "#internetFuneral", "#RetteDeinInternet"])
    
    time.sleep(2)
    

"""
while True:
    for tweet in tweepy.Cursor(api.search, q=search).items():
        print('\nTweet by: @' + tweet.user.screen_name)
    
        try:
            print "Trying to rt"
            tweet.retweet()
            print "retweeted successfully"
        except tweepy.TweepError as e:
            print "already retweeted"
            time.sleep(10)
            try:
                print "Trying to fave"
                tweet.favorite()
                print "faved successfully"
            except tweepy.TweepError as e:
                print "already faved"
                time.sleep(10)
                try:
                    print "Trying to follow"
                    tweet.user.follow()
                    print "followed successfully"
                except tweepy.TweepError as e:
                    print "already followed"
                    time.sleep(10)
        
        except StopIteration:
            break
            """
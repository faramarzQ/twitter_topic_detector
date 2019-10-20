import os
import Tweet
import json

#
#    User
#


class User:
    def __init__(self):
        self.name = ''
        self.tweets = {}
        self.id = ''
        self.tweets_count = 0
        self.urls_count = 0

    # initialises the object with the filtered data (user_tweets.json file)
    def initWithRawData(self, data):
        self.id = data[0]['id']
        self.name = data[0]['name']
        for i in range(len(data)):
            if(i not in [0, 1, 2]):
                tweetObj = Tweet.Tweet(data[i])
                self.tweets[data[i]['id']] = tweetObj
                self.tweets_count += 1
                self.urls_count += self.tweets[data[i]['id']].getAttr('urls_count')

    # initialises the object with the raw data ([user name].json file)
    def initWithFilteredData(self, data):
        self.id = data['id']
        self.name = data['name']
        for tweetID in data['tweets']:
            tweetObj = Tweet.Tweet(data['tweets'][str(tweetID)])
            self.tweets[data['tweets'][str(tweetID)]['id']] = tweetObj
            self.tweets_count += 1
            self.urls_count += self.tweets[data['tweets'][str(tweetID)]['id']].getAttr('urls_count')

    # reutrns tweets of object
    def getTweets(self):
        return self.tweets

    # reutrns attribute of object
    def getAttr(self, attrName):
        return getattr(self, attrName)

    # returns object as an dictionary
    def getAsDict(self):
        dic = {}
        dic['id'] = self.id
        dic['name'] = self.name
        dic['tweets'] = {}
        dic['urls_count'] = 0
        for index in self.tweets:
            dic['tweets'][str(index)] = self.tweets[index].getAsDict()
            dic['urls_count'] += self.tweets[index].getAttr('urls_count')
        return dic

    # def calculateURLsSimilarityInSelf(self, entireURLsCount):
    #     tweets = self.tweets
    #     for tweet in tweets:
    #         for targetTweet in tweets:


    def calculateTweetsURLsSimilarity(self, targetUserObj, entireURLsCount):
        for tweetID in self.getAttr('tweets'):
            for targetTweetID in targetUserObj.getAttr('tweets'):
                if self.getAttr('tweets')[tweetID].getAttr('urls') and targetUserObj.getAttr('tweets')[targetTweetID].getAttr('urls'):
                    self.getAttr('tweets')[tweetID].calculateURLsSimilarity(targetUserObj.getAttr('tweets')[targetTweetID], entireURLsCount)

    def calculateTweetURLsIDF(self, entireURLsCount):
        for tweetID in self.getAttr('tweets'):
            self.getAttr('tweets')[tweetID].calculateURLsIDF(entireURLsCount)

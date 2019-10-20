import os
import math

"""
    Tweet Class
"""

class Tweet:
    def __init__(self, tweet):
        self.id = ''
        # in_reply_to_user_id = None
        self.text = ''
        self.text_array = []
        self.hastags = []
        self.urls = []
        self.urls_count = 0
        self.created_at = ''
        self.initAttrs(tweet)

    def initAttrs(self, tweet):
        # self.in_reply_to_user_id = tweet['in_reply_to_user_id']
        # self.created_at = tweet['created_at']
        # self.hashtags = tweet['hashtags']

        self.id = tweet['id']
        self.setText(tweet['text'])
        if 'urls' in tweet:
            self.urls = tweet['urls']
            urlCount = 0
            for url in tweet['urls']:
                if 'duplicate_number' not in url:
                    url['duplicate_number'] = 1
                urlCount += 1
            self.urls_count += urlCount

    def setText(self, text):
        self.text = text
        textArray = text.split()
        self.text_array = textArray
        # remove stop and non-english words here

    def getAttr(self, attrName):
        return getattr(self, attrName)

    def setAttr(self, attrName, value):
        return getattr(self, attrName, value)

    def getAsDict(self):
        dic = {}
        dic['id'] = self.id
        dic['text'] = self.text
        # dic['created_at'] = self.created_at
        # dic['hastags'] = self.hastags

        # if urls's array is empty, don't set it
        urls = []
        if self.urls:
            dic['urls'] = self.urls

        return dic

    def calculateURLsSimilarity(self, targetTweetObj, entireURLsCount):
        for URL in self.getAttr('urls'):
            for targetURL in targetTweetObj.getAttr('urls'):
                if targetURL['expanded_url'] == URL['expanded_url']:
                    targetURL['duplicate_number'] += 1
                    URL['duplicate_number'] += 1

    def calculateURLsIDF(self, entireURLsCount):
        for URL in self.getAttr('urls'):
            if 'duplicate_number' in URL:
                URL['IDF'] = math.log((entireURLsCount / URL['duplicate_number']), 2)

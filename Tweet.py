import os
import math
import nltk
import numpy as np
import StopWordsSingleton
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""
    Tweet Class
"""
#TODO: add vectorizedText to output dict
class Tweet:
    def __init__(self, tweet):
        self.id = ''
        # in_reply_to_user_id = None
        self.stoppedText = []
        self.POSedText = []
        self.vectorizedText = {}
        self.topic = ''
        self.text = ''
        self.hastags = []
        self.urls = []
        self.urls_count = 0
        self.created_at = ''
        self.initAttrs(tweet)

    # initialises object using raw data
    def initAttrs(self, tweet):
        self.in_reply_to_user_id = tweet['in_reply_to_user_id']
        self.created_at = tweet['created_at']
        self.hashtags = tweet['hashtags']
        self.id = tweet['id']
        self.filterAndSetText(tweet['text'])
        if 'urls' in tweet:
            self.urls = tweet['urls']
            urlCount = 0
            for url in tweet['urls']:
                if 'duplicate_number' not in url:
                    url['duplicate_number'] = 1
                urlCount += 1
            self.urls_count += urlCount

    # filters tweet's text from stop words, vectorizes it, detects it's topic, and POS tags it
    def filterAndSetText(self, text):
        self.rawText = text
        self.stoppedText = self.removeStopWordsFromText(text)
        self.vectorizedText = self.textToVector(self.stoppedText)
        self.topic = self.detectTopic(self.vectorizedText)
        self.POSedText = self.POSTagText(self.stoppedText)

    # removes stop words from Raw
    def removeStopWordsFromText(self, text):
        stopWords = StopWordsSingleton.StopWords.getStopWords()
        wordTokens = word_tokenize(text)
        stoppedText = [w for w in wordTokens if not w in stopWords]
        return stoppedText

    # pos tags text
    def POSTagText(self, text):
        return nltk.pos_tag(text)

    # gets attribute's value
    def getAttr(self, attrName):
        return getattr(self, attrName)

    # sets attribute's value
    def setAttr(self, attrName, value):
        return getattr(self, attrName, value)

    # link: https://spacy.io/api/token#vector
    # this method converts a tokenized word array into vectors,
    # vectorization is done using a triained model by spaCy module
    # model is downloaded using this command: $ python -m spacy download en_core_web_sm
    def textToVector(self, text):
        vectorizedText = {}
        nlp = spacy.load('en_core_web_sm')
        for word in text:
            vectorizedText[word] = nlp(word).vector
            # print(vectorizedText[word])
        return vectorizedText

    # calculates topic of each tweet
    def detectTopic(self, vectors):
        topic = []
        for index in range(0,96):
            sum = 0
            for word in vectors:
                sum += vectors[word][index]
            avg = sum / 96
            topic.append(avg)
        return topic

    # returns objet as dictionary
    def getAsDict(self):
        dic = {}
        dic['id'] = self.id
        dic['stoppedText'] = self.stoppedText
        dic['POSedText'] = self.POSedText
        dic['rawText'] = self.rawText
        # dic['created_at'] = self.created_at
        # dic['hastags'] = self.hastags

        # if urls's array is empty, don't set it
        urls = []
        if self.urls:
            dic['urls'] = self.urls
        return dic

    # calculates similarity of URLs of two different tweets
    def calculateURLsSimilarity(self, targetTweetObj, entireURLsCount):
        for URL in self.getAttr('urls'):
            for targetURL in targetTweetObj.getAttr('urls'):
                if targetURL['expanded_url'] == URL['expanded_url']:
                    targetURL['duplicate_number'] += 1
                    URL['duplicate_number'] += 1

    # calculates IDFs of each tweet
    def calculateURLsIDF(self, entireURLsCount):
        for URL in self.getAttr('urls'):
            if 'duplicate_number' in URL:
                URL['IDF'] = math.log((entireURLsCount / URL['duplicate_number']), 2)

#!/usr/bin/python3

import os
import json
import User

#
#    calculates the IDF of each Tweet's URL in the entire Tweets
#


class TweetURLIDF:
    def __init__(self):
        with open("user_tweets.json", "r") as file:
            filteredData = json.load(file)

        DataWithURLsIDF = {}
        entireURLsCount = filteredData['urls_count']
        users = filteredData['users']

        for userID in list(users):
            userObj = User.User()
            userObj.initWithFilteredData(users[userID])
            # userObj.calculateURLsSimilarityInSelf(entireURLsCount)
            del users[userID]

            if not users:
                # userObj.calculateTweetsURLsSimilarity(userObj, entireURLsCount)
                userObj.calculateTweetURLsIDF(entireURLsCount)
                DataWithURLsIDF[userObj.getAttr('id')] = userObj.getAsDict()
                break

            for targetUserID in list(users):
                targetUserObj = User.User()
                targetUserObj.initWithFilteredData(users[targetUserID])
                userObj.calculateTweetsURLsSimilarity(targetUserObj, entireURLsCount)
                userObj.calculateTweetURLsIDF(entireURLsCount)

            DataWithURLsIDF[userObj.getAttr('id')] = userObj.getAsDict()
            del userObj

        with open("user_tweets_urls_idf.json", "w") as file:
            json.dump(DataWithURLsIDF, file)


TweetURLIDF()

#!/usr/bin/python3

import json
import os
import User

#
#    this Class indexes all user's tweets
#

class UsersTweets:
    def __init__(self):

        # index files in a specific directory
        filesPaths = []
        path = './test'
        for r, d, f in os.walk(path):
            for file in f:
                    if '.json' in file:
                        filesPaths.append(os.path.join(r, file))

        data = {}
        data['urls_count'] = 0
        data['users'] = {}

        # attach all tweets of each user in a seperate file as a json format
        for file in filesPaths:
            with open(file) as jsonFile:
                tempFile = json.load(jsonFile)
                userObj = User.User()
                userObj.initWithRawData(tempFile)
                data['users'][userObj.getAttr('id')] = userObj.getAsDict()
                data['urls_count'] += userObj.getAttr('urls_count')
                del userObj

        with open("user_tweets.json", "w") as file:
            json.dump(data, file)


# app start point
UsersTweets()

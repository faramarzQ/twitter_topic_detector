#!/usr/bin/python3

import json
import os


#
#    this Class indexes all tweets of users
#

class UsersTweets:
    def __init__(self):
        
        # index files in one dir
        filesPaths = []
        path = './test'
        # path = './final_project-data/twitter/data'
        for r, d, f in os.walk(path):
            for file in f:
                    if '.json' in file:
                        filesPaths.append(os.path.join(r, file))

        data = {}

        # attach all tweets of each user in each file to a dict
        for file in filesPaths:
            with open(file) as jsonFile:

                tempFile = json.load(jsonFile)

                userID = tempFile[0]['id']
                data[userID] = {}
                data[userID]['id'] = tempFile[0]['id']
                data[userID]['name'] = tempFile[0]['name']
                data[userID]['tweets'] = []
                data[userID]['tweets_count'] = 0

                for i in range(len(tempFile)):
                    if(i not in [0, 1, 2]):
                        data[userID]['tweets'].append(tempFile[i])
                        data[userID]['tweets_count'] += 1

                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile)

UsersTweets()

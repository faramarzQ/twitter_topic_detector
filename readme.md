# Topic detection

### SUBJECT:
finds topic of Tweets on Twitter social media

---

#### Programming Language:
This project/software is written in python, which is a proper choice for such a project with data analysis goal. software's paradigm is object oriented which helps to define and separates each definition on it's own and create related modules to interact with each other, on the other hand it also decreases the amount of code for each part and the project's execution time. also design patterns like Singleton pattern has been used so that objects can be optimised.

---

### Data:
this project's data is Twitter's User, their Tweets, profile info. each tweet has all the data which twitter is shows on it's application. an example of this data is on the project.

---

### descriptions:
Software has two starting points, **UserTweets.py** and **TweetURLIDF.py** which both are classes.

- **Clean raw tweets in UsersTweets.py**:    

 this is the main start point of the projects. this module which has been created as a Class is where we convert raw and dirty data into neat and filtered data. this is done by:
 1. reading data on every file from a specific directory.    
 2. on the raw data what we have is an array of objects, containing user's personal info, followers, and tweets. in this project what we need is user's info and tweets.
what we need is a clean data and each part needs to be cleaned, so i've put every part's cleaning stuff on the shoulder of it's class.there is an User.py and Tweet.py class which defines user's and their tweets. so UsersTweets calls User class to cleans User data, and User Class Calls Tweet Class to clean User's Tweets.    
in UserTweet Class, inside a for loop which walks through raw file, we create a raw object from User class we send each file's data to it, UserClass initialises itself inside initWithRawData() method. this method also creates object from Tweet class and sends tweets to it. similarly Tweet class initialises itself inside initWithRawData().    
this metod filters and clean Tweets. this cleaning process contains removing stop words from Tweet's text, vectorizing each text's word, POS tagging text(using nltk), and finally calculating it's topic by averaging vectors.(this method is not complete yet.)
 3. and finally we store this clean data into a json file (code is commented so you can read learn more about it.)     

  **Execution**:
  run `./UserTweet.py` in your terminal to execute the software. a 'user_tweets.json' file is the result.

- **Calculate URL's IDF in TweetURLIDF.py:**    
this class processes cleaned data we created from UserTweets.py class, it calculates IDF of each url. process is exactly like above except that here we dont want to do process on the URL not the text.    
first it creates object from each user and their tweet to make the process easy, then compares each URLs with each other to calculate their similarity. this similarity is being used when calculates the IDF of Tweets.it stores processed data in a json file.(this method is also not complete yet).   
  **Execution**:
  run `./TweetURLIDF.py` in your terminal to execute the software. a 'user_tweets.json' file is the result.

---
### Note:
1. input of this section needs to be compatable with what we created on the last part.    
1. if you call for an attribute which you didn't attach to cleaned json file, it gives an error.
1.this project is not complete, but it will be.

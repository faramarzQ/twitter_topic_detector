from nltk.corpus import stopwords

#
#   StopWords class
#

class StopWords:
   __instance = None

   # creates an object from this class for the first time,
   # after that, new objects won't be created,
   # ony returns the created object,
   # this is becouse it takes time to crate object it for every URL in every tweet
   def __init__(self):
       if StopWords.__instance != None:
           raise Exception("This class is a singleton!")
       else:
           stopWords = set(stopwords.words("english"))
           stopWords.update(['.', ':', ',', '?', ')', '(', '[', ']', '}', '{', '!', '@', '#', '$', '%', '%', '&' ,'*', '_', '+', '=', '/', '-', '\'\'', '``', '""', 'n\'t', 'http', 'https', '\'s'])
           StopWords.stopWords = stopWords
           StopWords.__instance = self

   def getStopWords():
      if StopWords.__instance == None:
         StopWords()
      return StopWords.stopWords

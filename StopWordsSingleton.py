from nltk.corpus import stopwords

class StopWords:
   __instance = None

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

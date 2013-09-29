# base class for searches


class SearchObject():
   # constructor - require key and search id
   def __init__(self, apiKey, searchID):
      # set apiKey and searchID members
      self.apiKey = apiKey
      self.searchID = searchID
      self.urls = []
      self.results = []

   # method to show the URLs found in
   # the last search
   def ShowFoundURLs(self):
      for url in self.urls:
         print url

   # method to search for a string and
   # return a list of URLs
   def FindURLs(self, searchString):
      pass

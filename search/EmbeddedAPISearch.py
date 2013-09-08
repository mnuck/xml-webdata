# class to search for URLs given a search string
# using the google API embedded in the program

from SearchObject import SearchObject

from apiclient.discovery import build

class EmbeddedAPISearch(SearchObject):
   # Simple class constructor.
   def __init__(self, apiKey, searchID):
      # Call the base class constructor
      SearchObject.__init__(self, apiKey, searchID);

   # implement FindURLs method using embedded API calls call
   def FindURLs(self, searchString):
      # Build a service object for interacting with the API.
      service = build("customsearch", "v1",
                developerKey=self.apiKey)

      #perform search
      self.results = service.cse().list(
          q=searchString,
          cx=self.searchID,
        ).execute()

      #construct list of URLs
      del self.urls[:];
      for url in self.results['items']:
         self.urls.append(url['link']);
      return self.urls;

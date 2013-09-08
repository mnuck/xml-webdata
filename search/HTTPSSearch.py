# class to search for URLs given a search string
# using the google API via a standard HTTPS search

from SearchInterface import SearchInterface

import json
import urllib2

class HTTPSSearch(SearchInterface):
   # Simple class constructor.
   def __init__(self, apiKey, searchID):
      # Call the base class constructor
      SearchInterface.__init__(self, apiKey, searchID);

   # implement FindURLs method using HTTPS call
   def FindURLs(self, searchString):
      #build search URL
      queryUrl = 'https://www.googleapis.com/customsearch/v1';
      queryUrl = queryUrl + '?key=' + self.apiKey;
      queryUrl = queryUrl + '&cx=' + self.searchID;
      queryUrl = queryUrl + '&q=' + searchString;

      #perform search
      self.results = urllib2.urlopen(queryUrl)
      self.results = json.load(self.results)

      # print "Title: ", i['title'];
      # print "    Display Link: ", i['displayLink'];
      # print "   Formatted URL: ", i['formattedUrl'];
      # print "            Link: ", i['link'];

      #construct list of URLs
      del self.urls[:];
      for url in self.results['items']:
         self.urls.append(url['link']);
      return self.urls;

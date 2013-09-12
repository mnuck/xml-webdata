#!/usr/bin/env python
# Put your own Google API developer data in a file called custom_key.py.
# The file should contain the statements:
#    myKey      = 'yourGoogleApiDeveloperKey';
#    mySearchId = 'yourSearchEngineID';
# If you don't have this file, don't expect this line to work!
#
# The first line of main can be switched between HTTPSSearch and EmbeddedAPISearch
# with no functional changes, one class searches using the embedded API approach
# and the other does it via a standard HTTPS search.

import custom_key
import urllib2
import argparse

import html_parser.extract_anchor as Extractor
import search.HTTPSSearch as HTTPSSearch
import search.EmbeddedAPISearch as EmbeddedAPISearch

def main():

   argParser = argparse.ArgumentParser()
   argParser.add_argument("query",
                          help="The query string. This string will be passed to the Google API.")
   args = argParser.parse_args()

   queryString = args.query;

   searchObj = HTTPSSearch.HTTPSSearch(custom_key.myKey, custom_key.mySearchId);
   urls      = searchObj.FindURLs(queryString);

   print "List of Found URLs:\n";
   searchObj.ShowFoundURLs();
   
   print "\nAttributes of URLs with .html in name:\n";
   for url in urls:
      
      if url.find('.html') != -1:
         request = urllib2.urlopen(url);
         htmlPage = request.read();

         # Simple little test driver for our Anchor Extractor:
         anchorParser = Extractor.HTMLAnchorExtractor();

         # Feed the extractor a simple test string.
         anchorParser.feed(htmlPage);

         # 'attributes' is a list of tuples.
         attributes = anchorParser.GetAnchorAttributes();

         print attributes;

if __name__ == "__main__":
   main();

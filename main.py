
# Put your own Google API developer key in a file called custom_key.py.
# The file should contain the statement:
#    myKey      = 'yourGoogleApiDeveloperKey';
#    mySearchId = 'yourSearchEngineID';
# If you don't have it, don't expect this line to work:
import custom_key

import html_parser.extract_anchor as Extractor

import json
import urllib2

def main():
   queryText = 'Secure+XML';
   queryUrl = 'https://www.googleapis.com/customsearch/v1';
   queryUrl = queryUrl + '?key=' + custom_key.myKey;
   queryUrl = queryUrl + '&cx=' + custom_key.mySearchId;
   queryUrl = queryUrl + '&q=' + queryText;
   data = urllib2.urlopen(queryUrl)
   data = json.load(data)

   for i in data['items']:
      # print "Title: ", i['title'];
      # print "    Display Link: ", i['displayLink'];
      # print "   Formatted URL: ", i['formattedUrl'];
      # print "            Link: ", i['link'];

      link = i['link'];

      if link.find('.html') != -1:
         request = urllib2.urlopen(link);
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


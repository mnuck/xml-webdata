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
import urllib2
import argparse
import sqlite3

from BeautifulSoup import BeautifulSoup
#import search.EmbeddedAPISearch as EmbeddedAPISearch
#import personal_data as custom_key


def parse_from_url(url):
  req = urllib2.urlopen(url)
  contents = req.read()
  url = req.url
  length = len(contents)
  content_type = ""
  if 'content-type' in req.info().keys():
    content_type = req.info()['content-type']
  modified = ""
  if 'last-modified' in req.info().keys():
    modified = req.info()['last-modified']

  soup = BeautifulSoup(contents)
  title = soup.title.string
  potential_anchors = soup.findAll('a')
  anchors = []
  for anchor in potential_anchors:
    attrs = dict(anchor.attrs)
    if 'href' in attrs:
      href = attrs['href']
      base = req.url
      label = anchor.text
      anchors.append((base, label, href))
  return {'url': url, 'title': title,
          'contents': contents, 'content-type': content_type,
          'length': length, 'modified': modified,
          'anchors': anchors}


def main():
   argParser = argparse.ArgumentParser()
   argParser.add_argument("query",
                          help="The query string. This string will be passed to the Google API.")
   args = argParser.parse_args()

   queryString = args.query

   conn = sqlite3.connect(":memory:")
   cur = conn.cursor()
   cur.execute("CREATE TABLE Documents (url text, title text, contents text, content_type text, length integer, modified text)")
   cur.execute("CREATE TABLE Anchors (base text, href text, label text)")

   #searchObj = EmbeddedAPISearch.EmbeddedAPISearch(custom_key.myKey, custom_key.mySearchId)
   #urls = searchObj.FindURLs(queryString)

   # Starting from the Department of Computer Science home page
   # (you can use any), find all documents that are linked through
   # paths of length two or less containing only local links.
   # Keep only the documents containing the string 'faculty' in their title.
   print parse_from_url(queryString)['title']


if __name__ == "__main__":
   main()

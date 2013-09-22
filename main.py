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
from urlparse import urlparse, urlunparse

from BeautifulSoup import BeautifulSoup
import search.EmbeddedAPISearch as EmbeddedAPISearch
import personal_data as custom_key


def parse_from_url(url):
  print "visiting", url
  try:
    req = urllib2.urlopen(url)
    contents = req.read()
  except:
    return None  # a bad link? that never happens! except for all the time.
  url = req.url
  length = len(contents)
  content_type = ""
  if 'content-type' in req.info().keys():
    content_type = req.info()['content-type']
  modified = ""
  if 'last-modified' in req.info().keys():
    modified = req.info()['last-modified']

  try:
    soup = BeautifulSoup(contents)
    title = soup.title.string
  except:
    return None  # some pages are not really pages
  potential_anchors = soup.findAll('a')
  anchors = []
  for anchor in potential_anchors:
    attrs = dict(anchor.attrs)
    if 'href' in attrs:
      href = attrs['href']
      if urlparse(href).scheme == '':
        href = urlunparse(urlparse(url)[:2] + urlparse(href)[2:])

      base = req.url
      label = anchor.text
      anchors.append((base, href, label))
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
  if not (queryString.startswith("http://") or queryString.startswith("https://")):
    queryString = "http://" + queryString

  conn = sqlite3.connect("question1.db")
  cur = conn.cursor()
  cur.execute("CREATE TABLE Documents (url text, title text, contents text, content_type text, length integer, modified text, primary key (url))")
  cur.execute("CREATE TABLE Anchors (base text, href text, label text, primary key (base, href, label))")

  # Starting from the Department of Computer Science home page (you can use
  # any), find all documents that are linked through paths of length two or
  # less containing only local links. Keep only the documents containing the
  # string 'faculty' in their title.
  start = "http://cs.mst.edu"
  what_is_local = "cs.mst.edu"

  visited = set([queryString])
  result = parse_from_url(start)
  for anchor in result['anchors']:
    try:
      cur.execute("INSERT INTO Anchors VALUES (?,?,?)", anchor)
    except sqlite3.IntegrityError:
      pass
  if "faculty" in result['title']:
      data = (result['url'], result['title'], result['contents'],
              result['content-type'], result['length'], result['modified'])
      try:
        cur.execute("INSERT INTO Documents VALUES (?,?,?,?,?,?)", data)
      except sqlite3.IntegrityError:
        pass

  def grab_all_links():
    cur.execute('SELECT href FROM Anchors')
    rows = cur.fetchall()
    for row in rows:
      url = row[0]
      if urlparse(url).scheme not in ['http', 'https']:
        continue
      if what_is_local not in urlparse(url).netloc:
        continue
      if not url in visited:
        visited.add(url)
        result = parse_from_url(url)
        if result is None:
          continue
        for anchor in result['anchors']:
          try:
            cur.execute("INSERT INTO Anchors VALUES (?,?,?)", anchor)
          except sqlite3.IntegrityError:
            pass
        if "faculty" in result['title']:
            data = (result['url'], result['title'], result['contents'],
                    result['content-type'], result['length'], result['modified'])
            try:
              cur.execute("INSERT INTO Documents VALUES (?,?,?,?,?,?)", data)
            except sqlite3.IntegrityError:
              pass

  grab_all_links()
  grab_all_links()

  #searchObj = EmbeddedAPISearch.EmbeddedAPISearch(custom_key.myKey, custom_key.mySearchId)
  #urls = searchObj.FindURLs(queryString)

  # Starting from the Department of Computer Science home page
  # (you can use any), find all documents that are linked through
  # paths of length two or less containing only local links.
  # Keep only the documents containing the string 'faculty' in their title.
  #derp = parse_from_url(queryString)
  #pprint(derp)


if __name__ == "__main__":
  main()

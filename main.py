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
import sqlite3
from urlparse import urlparse, urlunparse

from BeautifulSoup import BeautifulSoup
from apiclient.discovery import build
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

  anchors = []
  potential_anchors = []
  title = ""
  try:
    soup = BeautifulSoup(contents)
    title = soup.title.string
    potential_anchors = soup.findAll('a')
  except:  # not html
    pass

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


def startDB(filename):
  conn = sqlite3.connect(filename)
  cur = conn.cursor()
  cur.execute("DROP TABLE IF EXISTS Documents")
  cur.execute("DROP TABLE IF EXISTS Anchors")
  cur.execute("CREATE TABLE Documents (url text, title text, contents text, content_type text, length integer, modified text, primary key (url))")
  cur.execute("CREATE TABLE Anchors (base text, href text, label text, primary key (base, href, label))")
  return conn, cur


def load_anchors_and_page_from_result_q1(result, cur, filter_string):
  for anchor in result['anchors']:
    try:
      cur.execute("INSERT INTO Anchors VALUES (?,?,?)", anchor)
    except sqlite3.IntegrityError:
      pass
  if filter_string in result['title'].lower():
      data = (result['url'], result['title'], result['contents'],
              result['content-type'], result['length'], result['modified'])
      try:
        cur.execute("INSERT INTO Documents VALUES (?,?,?,?,?,?)", data)
      except sqlite3.IntegrityError:
        pass


def load_anchors_and_page_from_result_q2(result, cur, filter_length):
  for anchor in result['anchors']:
    try:
      cur.execute("INSERT INTO Anchors VALUES (?,?,?)", anchor)
    except sqlite3.IntegrityError:
      pass
  if result['length'] > filter_length:
      data = (result['url'], result['title'], result['contents'],
              result['content-type'], result['length'], result['modified'])
      try:
        cur.execute("INSERT INTO Documents VALUES (?,?,?,?,?,?)", data)
      except sqlite3.IntegrityError:
        pass


def question1():
  # Starting from the Department of Computer Science home page (you can use
  # any), find all documents that are linked through paths of length two or
  # less containing only local links. Keep only the documents containing the
  # string 'faculty' in their title.
  conn, cur = startDB("question1.db")

  start = "http://cs.mst.edu"
  what_is_local = urlparse(start).netloc
  visited = set([start])

  result = parse_from_url(start)
  load_anchors_and_page_from_result_q1(result, cur, "faculty")

  for i in xrange(2):
    cur.execute('SELECT href FROM Anchors')
    rows = cur.fetchall()
    for row in rows:
      url = row[0]
      if urlparse(url).scheme not in ['http', 'https']:
        continue
      if what_is_local != urlparse(url).netloc:
        continue
      if not url in visited:
        visited.add(url)
        result = parse_from_url(url)
        if result is None:
          continue
        load_anchors_and_page_from_result_q1(result, cur, "faculty")

  print "Results for Question 1:"
  for row in cur.execute("SELECT * from Documents"):
    print row
  print "Question 1 COMPLETE\n"

  conn.commit()
  conn.close()


def question2():
  # "SELECT d2.base, d2.label
  #   FROM document d1 anchor d2
  #   SUCH THAT d1 MENTIONS XML
  #   WHERE d1.length > 100";
  # plain english: give me the referer and link label for every link on the web
  # that points to a page that mentions XML, so long as that page length > 100
  conn, cur = startDB("question2.db")
  conn.text_factory = str
  search_string = "XML"

  service = build("customsearch", "v1", developerKey=custom_key.myKey)
  result = service.cse().list(q=search_string, cx=custom_key.mySearchId).execute()

  for item in result['items']:
    url = item['link']
    result = parse_from_url(url)
    load_anchors_and_page_from_result_q2(result, cur, 100)

  print "Results for Question 2:"
  for row in cur.execute("SELECT base, label FROM Anchors"):
    print row
  print "Question 2 COMPLETE\n"

  #urls = searchObj.FindURLs(queryString)
  conn.commit()
  conn.close()


def question3():
  # SELECT d.url
  # FROM document d SUCH THAT "http://the.starting.doc" ->* d,
  #     document d1 SUCH THAT d=>|->=>d1
  #     anchor a SUCH THAT base = d1
  # WHERE a.href = "your server";
  conn, cur = startDB("question3.db")

  conn.commit()
  conn.close()


def main():
  #question1()
  question2()
  #question3()
  pass


if __name__ == "__main__":
  main()

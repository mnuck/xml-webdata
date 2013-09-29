#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 1
#
# Prereqs:
#  BeautifulSoup is used for HTML parsing, and is included
#  google-api-python-client is used to implement MENTIONED BY
#   and can be installed by following instructions at:
#   https://developers.google.com/api-client-library/python/start/installation
#
# Put your own Google API developer data in a file called personal_data.py.
# The file should contain the statements:
#    myKey      = 'yourGoogleApiDeveloperKey';
#    mySearchId = 'yourSearchEngineID';
# If you don't have this file, don't expect this program to work!
#
# As per the assingment, this is a hard-coded implemention. The code that
#  would be used to implement the WebSQL-specific operators is here, but
#  we are not attempting to parse WebSQL.
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


def load_anchors_and_page_from_result(result, cur):
  for anchor in result['anchors']:
    try:
      cur.execute("INSERT INTO Anchors VALUES (?,?,?)", anchor)
    except sqlite3.IntegrityError:
      pass
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

  print "\nResults for Question 1:"
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
  min_length = 100

  service = build("customsearch", "v1", developerKey=custom_key.myKey)
  result = service.cse().list(q=search_string, cx=custom_key.mySearchId).execute()

  for item in result['items']:
    url = item['link']
    result = parse_from_url(url)
    load_anchors_and_page_from_result_q2(result, cur, min_length)

  print "\nResults for Question 2:"
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
  # plain-ish english: find the URL for all pages that satisfy the following:
  #   the page must be reachable via any number of only local links
  #   (on the same server) starting from "http://the.starting.doc"
  #  AND
  #   the page must link to (via one global link OR one local and one global)
  #   a page that links to "your server"
  conn, cur = startDB("question3.db")
  starting_doc = "http://web.mst.edu/~mannr4"
  your_server = "http://www.mst.edu"

  service = build("customsearch", "v1", developerKey=custom_key.myKey)

  documents = dict()
  # find all pages that are reachable from starting_doc via only local links
  what_is_local = urlparse(starting_doc).netloc
  frontier = [starting_doc]
  closed = set()
  while frontier:
    current = frontier.pop()
    if current not in documents:
      documents[current] = parse_from_url(current)
    result = documents[current]
    if result is None:
      continue
    for anchor_tuple in result['anchors']:
      href = anchor_tuple[1]
      if urlparse(href).netloc == what_is_local:
        if href not in closed:
          frontier.append(href)
          closed.add(href)
  local_reachable = closed

  # documents reachable from local_reachable in one global link, also get one local
  one_global = set()
  one_local = set()
  for page in local_reachable:
    if page not in documents:
      documents[page] = parse_from_url(page)
    if documents[page] is None:
      continue
    for anchor_tuple in documents[page]['anchors']:
      href = anchor_tuple[1]
      if urlparse(href).netloc == what_is_local:
        one_local.add(href)
      else:
        one_global.add(href)

  # documents reachable from local_reachable in one local followed by one global
  two_steps = set()
  for page in one_local:
    if page not in documents:
      documents[page] = parse_from_url(page)
    if documents[page] is None:
      continue
    for anchor_tuple in documents[page]['anchors']:
      href = anchor_tuple[1]
      if urlparse(href).netloc != what_is_local:
        two_steps.add(href)

  criteria1options = one_global ^ two_steps

  # urls for pages that link to "your server"
  search_string = "link:%s" % your_server
  result = service.cse().list(q=search_string, cx=custom_key.mySearchId).execute()
  criteria2options = set([x['link'] for x in result['items']])

  # document URLs that satisfy both criteria
  results = criteria1options & criteria2options

  for key in results:
    result = documents[key]
    data = (result['url'], result['title'], result['contents'],
            result['content-type'], result['length'], result['modified'])
    try:
      cur.execute("INSERT INTO Documents VALUES (?,?,?,?,?,?)", data)
    except sqlite3.IntegrityError:
      pass

  print "\nResults for Question 3:"
  for row in cur.execute("SELECT url FROM Documents"):
    print row
  print "Question 3 COMPLETE\n"

  conn.commit()
  conn.close()


def main():
  question1()
  question2()
  question3()
  pass


if __name__ == "__main__":
  main()

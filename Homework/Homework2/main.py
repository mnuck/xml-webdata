#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2

from treelib import Tree
from BeautifulSoup import BeautifulSoup

import urllib2
from urlparse import urlparse, urlunparse

def main():
   tree = Tree();
   req = urllib2.urlopen('http://www.cs.toronto.edu')
   contents = req.read()
   try:
      soup = BeautifulSoup(contents)
      title = soup.title.string
   except:  # not html
      pass

if __name__ == '__main__':
   main();

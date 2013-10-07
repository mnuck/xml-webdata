#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2,

from hypertree import Node
from hypertree import Tree
from BeautifulSoup import BeautifulSoup

import urllib2
from urlparse import urlparse, urlunparse

def main():
   hyperTreeRoot = Node(tag='html');
   req = urllib2.urlopen('http://www.cs.toronto.edu')
   contents = req.read()
   try:
      soup = BeautifulSoup(contents)

      t = Tree(hyperTreeRoot);
      t.BuildTree(soup);
 
   except:  # not html
      pass

   t.Show();

if __name__ == '__main__':
   main();

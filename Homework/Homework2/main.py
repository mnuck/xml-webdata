#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2,

from hypertree import Node
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

import urllib2
from urlparse import urlparse, urlunparse

def main():

   req = urllib2.urlopen('http://www.cs.toronto.edu')
   contents = req.read()

   soup = None;
   try:
      soup = BeautifulSoup(contents)
   except:
      pass

   if soup != None:
      hyperTreeRoot = BuildTree(soup);
      print hyperTreeRoot;
   else:
      print 'Some exception raised building the soup!';

if __name__ == '__main__':
   main();


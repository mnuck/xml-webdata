#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2,

from hypertree import Node
from hypertree import Arc
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup
from test import RunTests
from queries import Query1
from queries import Query2
#from queries import Query3

import urllib2
from urlparse import urlparse, urlunparse

# For copying tree nodes.  Calls Node.__deepcopy__
from copy import deepcopy as deepcopy

def main():
   # For later:
   #req = urllib2.urlopen('http://www.cs.toronto.edu')
   #req = urllib2.urlopen('http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm')
   #contents = req.read()
   #print contents;

   #contents = ['<html><head><title>Page title</title></head>',
   #    '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
   #    '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
   #    '</html>'];
  
   #soup = None;
   #try:
   #   soup = BeautifulSoup(contents)
   #except:
   #   pass

   #if soup != None:
   #   print "Original HTML:";
   #   print soup.prettify();
   #   hyperTreeRoot = BuildTree(soup);
   #   print "\nHyperTree:";
   #   hyperTreeRoot.Show();

   #   #query one
   #else:
   #   print 'Some exception raised building the soup!';

   #pass;

   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
      '</html>'];

   Query1(doc);

   # doc = ['<html><head><title>Page title</title></head>',
   #    '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
   #    '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
   #    '</html>'];

   # Query2(doc);

if __name__ == '__main__':
   main();
   #RunTests();


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
from queries import Query3

import urllib2
from urlparse import urlparse, urlunparse

# For copying tree nodes.  Calls Node.__deepcopy__
from copy import deepcopy as deepcopy

def main():
   # Actual web pages
   #req = urllib2.urlopen('http://www.cs.toronto.edu') #alternate webpage
   #req = urllib2.urlopen('http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm') 
   #doc = req.read()
  
   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
      '</html>'];


   raw_input('\nPress Enter to run query 1:');

   #Query1(doc, 'language', 'title');
   Query1(doc, 'id', 'align');

   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>',
       '<more><p id="firstpara" align="center">Another paragraph </more>',
       '</html>'];

   raw_input('\nPress Enter to run query 2:');
   #Query2(doc,'BODY');
   Query2(doc,'para');

   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>',
       '<more><p id="firstpara" align="center">Another paragraph </more>',
       '</html>'];


   raw_input('\nPress Enter to run query 3:');
   #Query3(doc,'BODY','New TAG','New TEXT CONCAT');
   Query3(doc,'Another','H3','New Paragraph');

if __name__ == '__main__':
   main();
   #RunTests();


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
   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
      '</html>'];

   Query1(doc, 'id', 'align');

   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>',
       '<more><p id="firstpara" align="center">Another paragraph </more>',
       '</html>'];

   Query2(doc,'para');

   doc = ['<html><head><title>Page title</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>',
       '<more><p id="firstpara" align="center">Another paragraph </more>',
       '</html>'];

   Query3(doc,'Another','H3','New Paragraph');

if __name__ == '__main__':
   main();


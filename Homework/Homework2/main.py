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

# For copying tree nodes.  Calls Node.__deepcopy__
from copy import deepcopy as deepcopy

def CreateTestTree():
   # Build a simple test tree:
   root = Node('root');
   r = root;

   n = Node('Label1');
   n.fields['Text'] = '1';
   r.children.append(n);

   r = n;
   n = Node('A1');
   n.fields['Text'] = '1';
   r.children.append(n);

   n = Node('A2');
   n.fields['Text'] = '2';
   r.children.append(n);

   r = root;

   n = Node('Label2');
   n.fields['Text'] = '2';
   r.children.append(n);

   r = n;
   n = Node('B1');
   n.fields['Text'] = '1';
   r.children.append(n);

   r = root;

   n = Node('Label3');
   n.fields['Text'] = '3';
   r.children.append(n);

   return root;

def Test1():
   r = CreateTestTree();

   print "The tree:"
   print r;

   for operation in ['Head', 'Tail', 'Prime']:
      print operation,"of the tree:";
      print eval('r.' + operation + '()');
   
   print "Prime 2 of the tree:";
   print r.Prime(2);


def main():
   # For later:
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

   pass;

if __name__ == '__main__':
   # main();
   Test1();


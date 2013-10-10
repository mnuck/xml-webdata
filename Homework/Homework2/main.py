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
from hypertree import NewNode
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

#def CreateNewTestTree():
#   # Build a simple test tree
#   #create objects for tree
#   root = NewNode();
#   node1 = NewNode();
#   node2 = NewNode();
#   node3 = NewNode();
#   Arc1 = Arc(None, root, node1);
#   Arc2 = Arc(None, root, node2);
#   Arc3 = Arc(None, root);
#   Arc4 = Arc(None, node1);
#   Arc5 = Arc(None, node1);
#   Arc6 = Arc(None, node2);

#   #fill out arc data (plus some extra data for testing)
#   Arc1.fields['Text'] = 'Label1';
#   Arc2.fields['Text'] = 'Label2';
#   Arc3.fields['Text'] = 'Label3';
#   Arc3.fields['Date'] = '9 Oct 2013';
#   Arc4.fields['Text'] = 'A1';
#   Arc4.fields['URL'] = 'www.ilovexml.com';
#   Arc5.fields['Text'] = 'A2';
#   Arc6.fields['Text'] = 'B1';
#   Arc6.fields['Publisher'] = 'NGP';

#   #build tree
#   node1.AddArc(Arc4);
#   node1.AddArc(Arc5);
#   node2.AddArc(Arc6);
#   root.AddArc(Arc1);
#   root.AddArc(Arc2);
#   root.AddArc(Arc3);

#   return root;

def Test1():
   r = CreateTestTree();

   print "The tree:"
   print r;

   for operation in ['Head', 'Tail', 'Prime']:
      print operation,"of the tree:";
      print eval('r.' + operation + '()');
   
   print "Prime 2 of the tree:";
   print r.Prime(2);

   print "Tail 2 of the tree:";
   print r.Tail(2);

#def Test2():
#   tree = CreateNewTestTree();

#   print "The tree:"
#   tree.Show();

def SimpleHyperTreeExample():
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))

   print "Original HTML as soup tree:";
   print soup.prettify();
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree:";
   hyperTreeRoot.Show();

def main():
   # For later:
#   req = urllib2.urlopen('http://www.cs.toronto.edu')
   req = urllib2.urlopen('http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm')
   contents = req.read()
   #print contents;
  
   soup = None;
   try:
      soup = BeautifulSoup(contents)
   except:
      pass

   if soup != None:
      print "Original HTML:";
      print soup.prettify();
      hyperTreeRoot = BuildTree(soup);
      print "\nHyperTree:";
      hyperTreeRoot.Show();
   else:
      print 'Some exception raised building the soup!';

   pass;

if __name__ == '__main__':
   #main();
   # Test1();
   #Test2();
   SimpleHyperTreeExample();


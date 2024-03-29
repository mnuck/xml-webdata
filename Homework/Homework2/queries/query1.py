#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2,

from hypertree import Arc
from hypertree import Node
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup
from copy import deepcopy
import string

def Query1(doc=None, field1=None, field2=None):

   if not (doc and field1 and field2):
      print 'Insufficient data to perform query';
   else:
      print 'doc:\n', doc;
      print ''.join(['\nSelect [y.', field1, ', y.', field2,'] From x in doc\'!, y in x\'']);

      #parse html and store in hyper tree
      soup = BeautifulSoup(''.join(doc))
      hyperTreeRoot = BuildTree(soup);

      print 'Hypertree of the HTML:';
      hyperTreeRoot.Show();

      #prime and tail the doc
      hyperTreeRoot = hyperTreeRoot.Prime();
      hyperTreeRoot.Tail();

      results = [];

      while len(hyperTreeRoot.arcs) > 0:
         #head to get first simple tree
         simpleTree = deepcopy(hyperTreeRoot);
         simpleTree.Head();

         #prime to get y
         y = simpleTree.Prime();

         if y:
            #check all of y's arcs for id and align
            for arc in y.arcs:
               idData = arc.Peek(field1);
               alignData = arc.Peek(field2);

               if idData != None or alignData != None:
                  results.append((idData, alignData));

         #this simple tree has been searched, tail root to remove it
         # and continue searching
         hyperTreeRoot.Tail();
      
      print '\nResults:';
      fieldWidth = 15;
      sep = '--------------';
      print ''.join([string.ljust(field1, fieldWidth), string.ljust(field2, fieldWidth)]);
      print ''.join([string.ljust(sep, fieldWidth), string.ljust(sep, fieldWidth)]);
      for result in results:
         try:
            v1 = result[0][0]; # assume we're only inerested in the first  value
         except TypeError:
            v1 = 'None';

         try:
            v2 = result[1][0]; # ditto
         except TypeError:
            v2 = 'None';

         print ''.join([string.ljust(v1, fieldWidth), string.ljust(v2, fieldWidth)]);


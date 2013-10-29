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
from copy import copy

def Query2(doc=None, text=None):

   if not (doc and text):
      print 'No doc and search string provided';
   else:
      print 'doc:\n', doc;
      print ''.join(['\nSelect y from y in doc\', where y\'.text ~ "', text, '"']);

      #parse html and store in hyper tree
      soup = BeautifulSoup(''.join(doc))
      hyperTreeRoot = BuildTree(soup);

      print 'Hypertree of the HTML:';
      hyperTreeRoot.Show();


      #prime doc
      y = hyperTreeRoot.Prime();

      #search all arcs of y for text like para
      results = [];
      SearchAllChildArcsForText(y, text, results);

      for result in results:
         result.Show();
         result.ShowAsHtml();

def SearchAllChildArcsForText(node=None, text=None, results=None):
   found = False;
   if node != None and text != None and results != None:
      #DFS all ars from the node provided looking for text
      for arc in node.arcs:
         while arc.childNode != None:
            if len(arc.childNode.arcs) == 0:
               arc.childNode = None;
            else:
               SearchAllChildArcsForText(arc.childNode, text, results);
               arc.childNode = None;
         #check for text and append to results if found
         for arcText in arc.listOfText:
            if arcText.text.find(text) != -1:
               #found text in this arc
               #return parent arc and end loop
               results.append(deepcopy(arc.parentNode.parentArc));
               found = True;
               break;

         if found:
            break;


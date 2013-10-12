from hypertree import Arc
from hypertree import Node
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

def Query1(doc=None, field1=None, field2=None):

   if not (doc and field1 and field2):
      print 'Insufficient data to perform query';
   else:
      print 'doc:\n', doc;
      print '\nSelect [y.', field1, 'y.', field2,'] From x in doc\'!, y in x\'\'';

      #parse html and store in hyper tree
      soup = BeautifulSoup(''.join(doc))
      hyperTreeRoot = BuildTree(soup);

      #prime and tail the doc
      hyperTreeRoot = hyperTreeRoot.Prime();
      hyperTreeRoot.Tail();

      results = [];

      while hyperTreeRoot != None:
         #head to get first simple tree
         simpleTree = hyperTreeRoot.Head();

         if not simpleTree:
            break;

         #prime twice to get y
         y = simpleTree.Prime(2);

         #check all of y's arcs for id and align
         for arc in y.arcs:
            idDat = arc.Peek(field1);
            alignData = arc.Peek(field2);

            if idData != None or alignData != None:
               results.append((idData, alignData));

         #this simple tree has been searched, tail root to remove it
         # and continue searching
         hyperTreeRoot.Tail();

      print field1,',       ', field2;
      #TODO: make this look good under id and align columns above
      print results;


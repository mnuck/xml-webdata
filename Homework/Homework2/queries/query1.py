from hypertree import Arc
from hypertree import Node
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

def Query1(doc=None):

   if doc == None:
      print 'No doc provided';
   else:
      print 'doc:\n', doc;
      print '\nSelect [y.id, y.align] From x in doc\'!, y in x\'\'';

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

         #prime twice to get y
         y = simpleTree.Prime(2);

         #check all of y's arcs for id and align
         for arc in y.arcs:
            if arc.isField('id'):
               idData = arc.Peek('id');
            else:
               idData = None;
            if arc.isField('align'):
               alignData = arc.Peek('align');
            else:
               alignData = None;
            if idData != None or alignData != None:
               results.append((idData, alignData));

         #this simple tree has been searched, tail root to remove it
         # and continue searching
         hyperTreeRoot.Tail();

      print 'id,       align';
      #TODO: make this look good under id and align columns above
      print results;


from hypertree import Arc
from hypertree import Node
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

def Query2(doc=None):

   if doc == None:
      print 'No doc provided';
   else:
      print 'doc:\n', doc;
      print '\nSelect y from y in doc\'!, where y\'.text ~ "para"';

      #parse html and store in hyper tree
      soup = BeautifulSoup(''.join(doc))
      hyperTreeRoot = BuildTree(soup);

      #prime and tail doc
      y = hyperTreeRoot.Prime();
      y.Tail();

      #search all arcs of y for text like para
      results = [];
      SearchAllArcsForText(y, 'para', results);
      results.ShowAsHTML();

def SearchAllArcsForText(node=None, text=None, results=None):
   
   if node != None and text != None and results != None:
      #DFS all ars from the node provided looking for text
      for arc in node.arcs:
         while arc.childNode != None:
            if len(arc.childNode.arcs) == 0:
               arc.childNode = None;
            else:
               SearchAllArcsForText(arc.childNode, text, results);
         #TODO this may need to change based on changes to Arc class
         #check for text and append to results if found
         for arcText in arc.listOfText:
            if arcText.text.find(text) != -1:
               #found text in this arc
               #return entire arc and end loop
               results.append(arc);
               break;


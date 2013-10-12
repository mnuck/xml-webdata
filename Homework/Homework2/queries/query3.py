from hypertree import Arc
from hypertree import Node
from hypertree.arc import TextBlock
from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

def Query3(doc=None):

   if not doc:
      print 'No doc provided';
   else:
      print 'doc:\n', doc;
      print '\nSelect y\' from y in doc\' + [Tag: "H3", Text: "New Paragraph"] as New Doc, where y\'.text ~ "Another"';

      #parse html and store in hyper tree
      soup = BeautifulSoup(''.join(doc))
      hyperTreeRoot = BuildTree(soup);

      print 'Hypertree of the HTML:';
      hyperTreeRoot.Show();

      #prime doc
      y = hyperTreeRoot.Prime();

      #prime doc
      y = hyperTreeRoot.Prime();

      #search all arcs of y for text like para
      results = [];
      SearchAllArcsForText(y, 'Another', results);

      newRoot = Node();
      for result in results:
         newRoot.AddArc(result);

      #create new node to concatenate onto query result
      newNode = Node();
      newArc = Arc('H3', newNode);
      textBlock = TextBlock('New Paragraph');
      newArc.listOfText.append(textBlock);
      newNode.AddArc(newArc);

      newRoot.Concatenate(newNode);

      print 'New Doc:';
      newRoot.Show();
      print 'HTML:';
      newRoot.ShowAsHtml();
      print;

def SearchAllArcsForText(node=None, text=None, results=None):

   if node != None and text != None and results != None:
      #DFS all ars from the node provided looking for text
      for arc in node.arcs:
         while arc.childNode != None:
            if len(arc.childNode.arcs) == 0:
               arc.childNode = None;
            else:
               SearchAllArcsForText(arc.childNode, text, results);
               arc.childNode = None;
         #TODO this may need to change based on changes to Arc class
         #check for text and append to results if found
         for arcText in arc.listOfText:
            if arcText.text.find(text) != -1:
               #found text in this arc
               #return parent arc and end loop
               results.append(arc);
               break;

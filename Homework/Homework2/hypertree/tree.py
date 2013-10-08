from node import Node

class Tree(object):
   def __init__(self, root=None):
       self.root = root

   # WebOQL operators: 
   # Tree Operators: Head, Tail, Arc, Prime, Hang etc.
   def Head(self, nHead=1):
      pass;

   def Tail(self, nTail=1):
      pass;

   def Arc(self):
      # TODO: Dunno how to specify which arc to fetch.
      pass;

   def Prime(self, nPrime=1):
      pass;

   def Hang(self, otherTree):
      pass;

   def BuildTree(self, inputSoup, parent=None):
      if parent == None:
         parent = self.root;

      # Assume the soup is the current node and all
      # children of the soup should be child nodes
      # of the hypertree.
      if inputSoup.name != None:
         parent.tag = str(inputSoup.name);
      else:
         parent.tag = 'None';
      for child in inputSoup.findChildren():
         childNode = Node();
         self.BuildTree(child, childNode);
         childNode.prev = parent;
         parent.children.append(childNode);
          
   def Show(self):
      print self.root.tag;
      for child in self.root.children:
         print str(child);


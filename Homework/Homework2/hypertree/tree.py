from node import Node

class Tree(object):
   def __init__(self, root=None):
       self.root = root

   def BuildTree(self, inputSoup, node=None):
      if node == None:
         node = self.root;

      # Assume the soup is the current node and all
      # children of the soup should be child nodes
      # of the hypertree.
      if inputSoup.name != None:
         node.tag = str(inputSoup.name);
      else:
         node.tag = 'None';
      for child in inputSoup.findChildren():
         childNode = Node();
         self.BuildTree(child, childNode);
         childNode.prev = node;
         node.children.append(childNode);
          
   def Show(self):
      print self.root.tag;
      for child in self.root.children:
         print str(child);


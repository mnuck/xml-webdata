from node import Node

def BuildTree(inputSoup, parent=None):
   if parent == None:
      parent = Node();

   # Assume the soup is the current node and all
   # children of the soup should be child nodes
   # of the hypertree.
   if inputSoup.name != None:
      parent.tag = str(inputSoup.name);
   else:
      parent.tag = 'None';
   for child in inputSoup.findChildren():
      childNode = Node();
      BuildTree(child, childNode);
      childNode.prev = parent;
      parent.children.append(childNode);

   return parent;
       
def Show(root):
   print root.tag;
   for child in root.children:
      print str(child);


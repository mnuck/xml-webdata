from node import Node

def BuildTree(inputSoup):
   parent = Node();

   if inputSoup.name != None:
      parent.tag = str(inputSoup.name);
   else:
      parent.tag = 'None';
   for child in inputSoup.findChildren():
      childNode = BuildTree(child);
      childNode.prev = parent;
      parent.children.append(childNode);

   return parent;


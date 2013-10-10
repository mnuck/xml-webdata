from newNode import NewNode
from arc import Arc

def BuildTree(inputSoup):
   
   #create new node
   newNode = NewNode();

   # TODO: Extract more from the soup per node than
   #       just the name/tag.
   for child in inputSoup.findChildren():
      #create the arc for this child, with it's parent as newNode
      newArc = Arc(str(inputSoup.name), newNode, None);
      #add the arc to the newNOde
      newNode.AddArc(newArc);

      #set the child node of this arc to node created from 
      #recurse call to BuildTree
      newArc.SetChildNode(BuildTree(child));

   return newNode;


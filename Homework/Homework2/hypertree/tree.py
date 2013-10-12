from node import Node
from arc import Arc
from BeautifulSoup import NavigableString
from BeautifulSoup import Declaration
from BeautifulSoup import Comment
from BeautifulSoup import ProcessingInstruction
from BeautifulSoup import CData

def BuildTree(inputSoup,parentArc=None):
   
   #create new node
   newNode = Node(parentArc);

   for child in inputSoup.contents:
      if type(child) not in [NavigableString, Declaration, Comment, CData, ProcessingInstruction]:
         #create the arc for this child, with it's parent as newNode
         newArc = Arc(str(child.name), newNode, None);
         #store attributes
         for attribute in child.attrs:
            key = str(attribute[0]);
            val = str(attribute[1]);
            if key in newArc.attributes.keys():
               newArc.attributes[key].append(val);
            else:
               newArc.attributes[key] = [val];

         #add the arc to the newNOde
         newNode.AddArc(newArc);

         #set the child node of this arc to node created from 
         #recurse call to BuildTree
         newArc.SetChildNode(BuildTree(child, newArc));
      else:
         #put navigable string with previous tab
         if parentArc != None:
            key = 'Text';
            if key in parentArc.attributes.keys():
               parentArc.attributes[key].append(str(child));
            else:
               parentArc.attributes[key] = [str(child)];

   return newNode;


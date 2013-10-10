from newNode import NewNode
from arc import Arc
from BeautifulSoup import NavigableString
from BeautifulSoup import Declaration
from BeautifulSoup import Comment
from BeautifulSoup import ProcessingInstruction
from BeautifulSoup import CData

def BuildTree(inputSoup,parentArc=None):
   
   #create new node
   newNode = NewNode(parentArc);

   for child in inputSoup.contents:
      if type(child) != NavigableString and type(child) != Declaration and \
      type(child) != Comment and type(child) != CData and type(child) != ProcessingInstruction:
         #create the arc for this child, with it's parent as newNode
         newArc = Arc(str(child.name), newNode, None);
         #store attributes
         for attribute in child.attrs:
            newArc.attributes.append((attribute[0], attribute[1]));

         #add the arc to the newNOde
         newNode.AddArc(newArc);

         #set the child node of this arc to node created from 
         #recurse call to BuildTree
         newArc.SetChildNode(BuildTree(child, newArc));
      else:
         #put navigable string with previous tab
         if parentArc != None:
            parentArc.attributes.append(('Text' , str(child)));

   return newNode;


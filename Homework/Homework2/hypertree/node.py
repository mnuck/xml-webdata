class Node(object):
   def __init__(self, parent=None,arcs=None):
      if arcs == None:
         self.arcs = [];
      else:
         self.arcs = arcs;
      self.parentArc=parent;

   def ShowAsHtml(self, indent=None):
      if len(self.arcs) == 0 and self.parentArc == None:
         print "<html>\n</html>"; # Empty document!
      else:
         for arc in self.arcs:
            arc.ShowAsHtml(indent);     

   def Show(self, indent=None):
      # show all data in this node's arcs
      if len(self.arcs) == 0 and self.parentArc == None:
         print "Tree is empty"
      else:
         for arc in self.arcs:
            arc.Show(indent);

   def AddArc(self, arc):
      self.arcs.append(arc);

   #operators
   #TODO: possibly need to change these so they return copies
   def Tail(self, nTail=1):
      if nTail <= len(self.arcs):
         for tail in range(0, nTail):
            self.arcs.pop(0);

   def Head(self, nHead=1):
      if nHead <= len(self.arcs):
         #keep nHead simple Trees 
         self.arcs = self.arcs[0 : nHead];

   def Prime(self, nPrime=1):
      #if this node has no children, prime returns nothing
      if len(self.arcs) < 1:
         return None;

      #return none if nPrime is invalid
      if nPrime < 1:
         return None;

      #check each child to find the first child with a child
      found = False;
      i = 0;
      while found == False and i < len(self.arcs):
         if len(self.arcs[i].childNode.arcs) > 0:
            #found a child with a child
            child = self.arcs[i].childNode;
            found = True;
         else:
            i = i + 1;

      if found == True:
         if nPrime > 1:
            return child.Prime(nPrime - 1)
         elif nPrime == 1:
            return child;
      else:
         return None;

   def Concatenate(self, nodeToConcat):
      for newArc in nodeToConcat.arcs:
         self.arcs.append(newArc);


from copy import deepcopy as deepcopy

class Node(object):
   def __init__(self, tag=None):
       self.tag = tag
       self.fields = {};
       self.prev = None;
       self.children = [];

   def __copy__(self):
      # Must use deepcopy.  TODO: Allow shallow copy of tag and fields?!
      raise NotImplementedError('Use deepcopy to copy the tree!');

   def __deepcopy__(self, memo):
      # Create the new node
      newNode = type(self)();

      # Take care of anything that can be shallow copied
      newNode.__dict__.update(self.__dict__);

      # now explicitly copy anything that must be deep copied
      newNode.prev = None;
      newNode.children = deepcopy(self.children, memo);
      for child in newNode.children:
         child.prev = newNode;

      # Finally, return the copied node
      return newNode;
   def __repr__(self):
      return str(type(self)) + "(tag=\'" + str(self.tag) + "\')";

   def __str__(self, indent=''):
      if self.tag == None:
         return '<empty node>';

      stringRep = indent + self.tag + '\n';

      indent = indent + '   ';
      for child in self.children:
         childStr = child.__str__(indent) + '\n';
         stringRep = stringRep + childStr;

      return stringRep;

   def Peek(self, field):
      if self.IsField(field):
         return self.fields[field];
      else:
         return None;

   def IsField(self, field):
      return self.fields.has_key(field);

   # WebOQL operators: 
   #    Head, Tail, Arc, Prime, Hang, etc.
   def Head(self, nHead=1):
      pass;

   def Tail(self, nTail=1):
      pass;

   def Arc(self):
      # TODO: Dunno how to specify which arc to fetch.
      pass;

   def Prime(self, nPrime=1):
      pass;

   def Hang(self, arc):
      return 


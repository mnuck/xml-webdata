from copy import copy as copy
from copy import deepcopy as deepcopy

class Node(object):
   def __init__(self, tag=None):
       self.tag = tag
       self.fields = {};
       self.prev = None;
       self.children = [];

   def __copy__(self):
      # Make a shallow copy (children are not copied)
      newNode = type(self)();
      newNode.tag = copy(self.tag);
      newNode.fields = copy(self.fields);
      return newNode;

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

      stringRep = indent + str(self.tag).strip() + '\n';

      indent = indent + '   ';
      for child in self.children:
         childStr = child.__str__(indent);
         stringRep = stringRep + childStr;

      return stringRep;

   def __add__(self, otherNode):
      newRoot = copy(self);
      newRoot.children = deepcopy(self.children) + [deepcopy(otherNode)];
      return newRoot; 

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
      if nHead <= len(self.children):
         newRoot = copy(self);
         newRoot.children = deepcopy(self.children[0 : nHead]);
         for child in newRoot.children:
            child.prev = newRoot;
         return newRoot;
      else:
         return deepcopy(self);

   def Tail(self, nTail=1):
      if nTail < len(self.children):
         newRoot = copy(self);
         newRoot.children = deepcopy(self.children[nTail :]);
         for child in newRoot.children:
            child.prev = newRoot;
         return newRoot;
      else:
         return None;

   def Arc(self):
      # TODO: Dunno how to specify which arc to fetch.
      pass;

   def Prime(self, nPrime=1):
       if len(self.children) == 0:
          return None;

       if nPrime > 1:
          return self.children[0].Prime(nPrime - 1);
       elif nPrime == 1:
          return deepcopy(self.children[0]);
       else:
          return None;

   def Hang(self, tag, fields):
      newRoot = copy(self);
      newRoot.childreen = deepcopy(self);
      for child in newRoot.children:
         child.prev = newRoot;
      return newRoot;

   def Concatenate(self, otherNode):
      # Use overloaded addition operator.
      return self + otherNode;


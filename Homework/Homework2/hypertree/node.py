from copy import deepcopy as deepcopy

class Node(object):
   def __init__(self, tag=None, text=None):
       self.tag = tag
       self.fields = {};
       self.prev = None;
       self.children = [];

   def __copy__(self):
      raise NotImplementedError('Use deepcopy to copy the tree!');

   def __deepcopy__(self, memo):
      newNode = type(self)();
      newNode.__dict__.update(self.__dict__);
      newNode.prev = None;
      newNode.children = deepcopy(self.children, memo);
      for child in newNode.children:
         child.prev = newNode;
      return newNode;

   def __str__(self, indent=''):
      if self.tag == None:
         return '<empty node>';

      stringRep = indent + self.tag + '\n';

      indent = indent + '   ';
      for child in self.children:
         childStr = child.__str__(indent) + '\n';
         stringRep = stringRep + childStr;

      return stringRep;
          
   def __repr__(self):
      return "<Tree Node " + str(self.tag) + " with " + str(len(self.children)) +" children>";

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


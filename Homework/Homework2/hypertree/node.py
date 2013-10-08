class Node(object):
   def __init__(self, tag=None, text=None):
       self.tag = tag
       self.fields = {};
       self.prev = None;
       self.children = [];

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
      return "<Tree Node ", self.tag, " with ", len(self.children), " children>";

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

   def Hang(self, node):
      pass;


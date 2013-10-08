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
      return str(self);

   def Peek(self, field):
      pass;

   def IsField(self, field):
      pass; 

class Arc(object):
   def __init__(self, tag=None, parent=None, child=None):
       self.tag = tag;
       self.fields = {};
       self.parent = parent;
       self.childNode = child;
  
   def Show(self, indent=None):
      #print tag
      if indent != None:
         print(indent),;
      print 'Tag: ', self.tag;
      #print all fields in this arc
      for field in self.fields.keys():
         if indent != None:
            print(indent),;
         print field, ": ", self.fields[field];

      #indent, then show data from the node this arc points to
      if self.childNode != None:
         if len(self.childNode.arcs) > 0:
            if indent == None:
               indent = '      ';
            else:
               indent = indent +  '      ';
            self.childNode.Show(indent);
      else:
         print '';

   def SetChildNode(self, node):
      self.childNode = node;





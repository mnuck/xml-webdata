class Arc(object):
   def __init__(self, tag=None, parent=None, child=None):
       self.tag = tag;
       self.attributes = [];
       self.parentNode = parent;
       self.childNode = child;
  
   def Show(self, indent=None):
      #print tag
      if indent != None:
         print(indent),;
      print 'Tag: ', self.tag;
      #print all attributes in this arc
      for attribute in self.attributes:
         if indent != None:
            print(indent),;
         print attribute[0], ": ", attribute[1];

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





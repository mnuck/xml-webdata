class Arc(object):

   defaultIndent = '      ';

   def __init__(self, tag=None, parent=None, child=None):
       self.tag = tag;
       self.attributes = {};
       self.parentNode = parent;
       self.childNode = child;
  
   def Show(self, indent=None):
      #print tag
      if indent != None:
         print(indent),;
      print 'Tag: ', self.tag;
      #print all attributes in this arc
      for key in self.attributes.keys():
         attribute = self.attributes[key];
         for a in attribute:
            if indent != None:
               print(indent),;
            print key, ": ", a;

      #indent, then show data from the node this arc points to
      if self.childNode != None:
         if len(self.childNode.arcs) > 0:
            if indent == None:
               indent = Arc.defaultIndent;
            else:
               indent = indent +  Arc.defaultIndent;
            self.childNode.Show(indent);
      else:
         print '';

   def SetChildNode(self, node):
      self.childNode = node;





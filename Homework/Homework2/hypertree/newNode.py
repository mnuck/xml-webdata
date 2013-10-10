class NewNode(object):
   def __init__(self, arcs=None):
      if arcs == None:
         self.arcs = [];
      else:
         self.arcs = arcs;

   def Show(self, indent=None):
      # show all data in this node's arcs
      for arc in self.arcs:
         arc.Show(indent);

   def AddArc(self, arc):
      self.arcs.append(arc);


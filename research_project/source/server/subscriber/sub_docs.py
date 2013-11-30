from twisted.web.resource import Resource

class SubDocs(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};     

   def render_GET(self, request):
      render = [];

      return ''.join(render);

from twisted.web.resource import Resource

import cgi

class SubscribePage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the subscriber page HTML 
      self.content = open('html/subscribe.html', 'r').read();      

   def render_GET(self, request):
      return self.content;
   
   def render_POST(self, request):
      # TODO: Handle subscription here!!!
      rt = self.parent.postedStr % ('Subscribed to ' + cgi.escape(request.args['sub-topic'][0]))      
   
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
         
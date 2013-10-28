import hashlib

from twisted.web.resource import Resource

class PublisherPage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the publisher page HTML 
      self.content = open('html/publish.html', 'r').read();

   def render_GET(self, request):
      return self.content;
   
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if 'pub-xml' in request.args and 'pub-topic' in request.args:
         xmlStr = request.args["pub-xml"][0];
         topic  = request.args["pub-topic"][0];

         hasher = hashlib.md5();
         hasher.update(topic);
         hasher.update(xmlStr);
         doc_id = hasher.hexdigest();
         
         self.parent.db.InsertDocument(doc_id, topic, xmlStr)
      
         rt = self.parent.postedStr % ('Document successfully posted with id: <b>' + doc_id + '</b>' );
         
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
   
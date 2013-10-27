from twisted.web.resource import Resource

from publisher.pub_page import PublisherPage
from subscriber.sub_page import SubscribePage

mainPage = '''
<!DOCTYPE html>
<html>
<body>
<p>The main page.</p>
<a href="/pub/?user=%s">Publish</a>
<a href="/sub/?user=%s">Subscribe</a> 
</body>
</html>'''

posted = '''
<html>
<body>
<p>
%s
</p>
<a href="/">Okay...</a> 
</body>
</html>'''

import cgi

class RootPage(Resource):
   # isLeaf = True;
   
   children = { 'pub': PublisherPage(),
                'sub': SubscribePage() };
   
   def __init__(self, db, avatarId):
      Resource.__init__(self);
      self.db = db;
      self.avatarId = avatarId;

   def render_GET(self, request):
      print "render_GET", request;
      return mainPage % (self.avatarId, self.avatarId,);

   def getChild(self, name, request):
      print "getChild",name;
      child = self;
      try:
         child = RootPage.children[name];
      except KeyError:
         pass;
      
      return child;
      
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if 'pub-xml' in request.args and 'pub-topic' in request.args:
         xmlStr = request.args["pub-xml"][0];
         topic  = request.args["pub-topic"][0];

         self.db.InsertDocument(topic, xmlStr)
      
         rt = posted % ('Posted content for topic: ' + cgi.escape(topic));
      elif 'sub-topic' in request.args:
         # TODO: Handle subscription here!!!
         rt = posted % ('Subscribed to ' + cgi.escape(request.args['sub-topic'][0]))
      return rt;
   
from twisted.web.resource import Resource

from publisher.pub_page import PublisherPage
from subscriber.sub_page import SubscribePage

posted = '''
<html>
<body>
<p>
%s
</p>
<a href="/">Okay...</a> 
</body>
</html>'''

class RootPage(Resource):
   # isLeaf = True;
   def __init__(self, db, avatarId):
      Resource.__init__(self);
      
      self.children = { 'pub': PublisherPage(self),
                        'sub': SubscribePage(self) };      
      self.db = db;
      self.avatarId = avatarId;
      self.postedStr = posted;
      
      # Load in the main page HTML 
      self.content = open('html/main.html', 'r').read();

   def render_GET(self, request):
      print "render_GET", request;
      return self.content % (self.avatarId, self.avatarId,);

   def getChild(self, name, request):
      print "getChild",name;
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
      
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if 'pub-xml' in request.args and 'pub-topic' in request.args:
         rt = 'render_POST for pub-xml in root_page.  This should not happen!'
      elif 'sub-topic' in request.args:
         rt = 'render_POST for sub-topic in root_page.  This should not happen!';

      return rt;
   
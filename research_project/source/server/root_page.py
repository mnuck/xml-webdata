from twisted.web.resource import Resource

from publisher.pub_page import PublisherPage
from publisher.pub_docs import PubDocs
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
   def __init__(self, xmlDb, secDb, authorizedUsers, avatarId):
      Resource.__init__(self);
      
      self.children = { 'pub'      : PublisherPage(self),
                        'sub'      : SubscribePage(self),
                        'pub_docs' : PubDocs(self)
                      };      
      self.xmlDb = xmlDb;
      self.secDb = secDb;
      self.authorizedUsers = authorizedUsers;
      self.avatarId = avatarId;
      self.postedStr = posted;
      
      # Load in the main page HTML 
      self.content = open('html/main.html', 'r').readlines();

   def render_GET(self, request):
      # TODO: Display published documents
      render = self.buildDynamicContent();
      return ''.join(render);

   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
      
   def render_POST(self, request):
      rt = 'oops, invalid post data in root_page.'
      return rt;
   
   def buildDynamicContent(self):
      render = self.content;
      return render;
   
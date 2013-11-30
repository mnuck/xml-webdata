from twisted.web.resource import Resource

from publisher.pub_page import PublisherPage
from publisher.pub_docs import PubDocs
from subscriber.sub_page import SubscribePage
from editor.edit_xml import EditorPage

class RootPage(Resource):
   # isLeaf = True;
   def __init__(self, xmlDb, secDb, subDb, authorizedUsers, avatarId):
      Resource.__init__(self);
      
      self.children = { 'pub'      : PublisherPage(self),
                        'sub'      : SubscribePage(self),
                        'pub_docs' : PubDocs(self),
                        'edit_xml' : EditorPage(self)
                      };      
      self.xmlDb = xmlDb;
      self.secDb = secDb;
      self.subDb = subDb;
      self.authorizedUsers = authorizedUsers;
      self.avatarId = avatarId;
      
      # Load in the main page HTML 
      self.postedStr = open('html/posted.html', 'r').read();
      self.content = open('html/main.html', 'r').readlines();

   def render_GET(self, request):
      return ''.join(self.content);

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
      # TODO: Is this needed?  If not, delete!
      render = self.content;
      return render;
   
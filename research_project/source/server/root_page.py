from twisted.web.resource import Resource

from admin.admin_page import AdminPage
from publisher.pub_page import PublisherPage
from publisher.pub_docs import PubDocs
from subscriber.sub_docs import SubDocs
from subscriber.sub_page import SubscribePage
from editor.edit_xml import EditorPage
from editor.show_xml import DisplayPage

class RootPage(Resource):
   # isLeaf = True;
   def __init__(self, pubdb, secDb, subDb, authorizedUsers, avatarId):
      Resource.__init__(self);
      
      self.children = { 'pub'      : PublisherPage(self, '/pub/'),
                        'sub'      : SubscribePage(self, '/sub/'),
                        'pub_docs' : PubDocs(self, '/pub_docs/'),
                        'sub_docs' : SubDocs(self, '/sub_docs/'),
                        'edit_xml' : EditorPage(self, '/edit_xml/'),
                        'show_xml' : DisplayPage(self, '/show_xml/'),
                        'admin'    : AdminPage(self, '/admin/')
                      };      
      self.pubDb = pubdb;
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
   
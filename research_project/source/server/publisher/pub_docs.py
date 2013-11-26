import urllib
from twisted.web.resource import Resource

class PubDocs(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};     

   def render_GET(self, request):
      render = [];
      userDocs = self.parent.secDb.GetDocsForUser(self.parent.avatarId);
      for doc in userDocs:
         urlEncodedArgs = urllib.urlencode({'doc' : doc[0], 'xpath' : './/' });
         try:
            topic = self.parent.xmlDb.GetTopicForDocId(doc[0]);
            for t in topic[0]:
               render.append("<a href='/edit_xml/?" + urlEncodedArgs + "'>" + str(t) + "</a><br>\n");

         except KeyError:
            pass;
      return ''.join(render);

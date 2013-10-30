import hashlib

from twisted.web.resource import Resource

class PublisherPage(Resource):
   authFormatStr = '<tr><td><input name=\'auth\' type=\'checkbox\'>%s</td><td><input name=\'auth_%s_xpath\' type=\'text\'></td></tr>';
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the publisher page HTML 
      self.content = open('html/publish.html', 'r').readlines();

   def render_GET(self, request):
      # Build access list.  Will generate HTML like the following:
      # <tr><td><input name="auth" type="checkbox">Tom</td><td><input name="auth_tom_xpath" type="text"></td>
      # <tr><td><input name="auth" type="checkbox">Matt</td><td><input name="auth_matt_xpath" type="text"></td>      
      users = self.parent.authDb.GetUserList();
      render = [];   
      for line in self.content:
         if '<!-- USER_LIST -->' in line:
            for user in users:
               tableRow = PublisherPage.authFormatStr % (user,user,);
               render.append(tableRow + '\n');
         else:
            render.append(line);
     
      return ''.join(render);
   
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
   
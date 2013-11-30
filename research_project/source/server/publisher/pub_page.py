import hashlib

from twisted.web.resource import Resource

class PublisherPage(Resource):
   authFormatStr = '<tr><td><input name=\'user\' type=\'checkbox\' value=\'%s\'>%s</td><td><input name=\'%s_xpath\' type=\'text\'></td></tr>';
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the publisher page HTML 
      self.content = open('html/publish.html', 'r').readlines();

   def render_GET(self, request):
      # Build access list.  Will generate HTML like the following:
      # <tr><td><input name="user" type="checkbox" value="tom">tom</td><td><input name="tom_xpath" type="text"></td>
      # <tr><td><input name="user" type="checkbox" value="matt">matt</td><td><input name="matt_xpath" type="text"></td>      
      users = self.parent.authorizedUsers;
      render = [];   
      for line in self.content:
         if '<!-- USER_LIST -->' in line:
            for user in users:
               tableRow = PublisherPage.authFormatStr % (user,user,user,);
               render.append(tableRow + '\n');
         else:
            render.append(line);
     
      return ''.join(render);
   
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if self.parent.avatarId != 'guest':
         if 'Publish' in request.args:
            rt = self.PublishDoc(request.args);
         elif 'RemoveAll' in request.args:
            rt = self.RemoveAllDocs();
         elif 'RemoveDocID' in request.args:
            rt = self.RemoveDocByID(request.args["remove-doc-id"][0]);
         elif 'RemoveDocTopic' in request.args:
            rt = self.RemoveDocByTopic(request.args["remove-doc-topic"][0]);
      else:
         rt = self.parent.postedStr % ('Sorry, a guest cannot publish documents.' );            
         
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
   
   def PublishDoc(self, args):
      xmlStr = args["pub-xml"][0];
      topic  = args["pub-topic"][0];
   
      hasher = hashlib.md5();
      hasher.update(topic);
      hasher.update(xmlStr);
      doc_id = hasher.hexdigest();
            
      self.parent.pubDb.InsertDocument(doc_id, topic, xmlStr, self.parent.avatarId)
            
      for user_id in args['user']:
         p_key = user_id + '_xpath';
         xpath = args[p_key][0];
         self.parent.secDb.InsertAuthorization(user_id, doc_id, xpath);
         
      return self.parent.postedStr % ('Document successfully posted with id: <b>' + doc_id + '</b>' );
   
   def RemoveAllDocs(self):
      removed = self.parent.pubDb.RemoveAllDocsByUser(self.parent.avatarId);
      if removed == 'SUCCESS':
         result = self.parent.postedStr % ('Successfully removed all posted documents.');
      else:
         result = self.parent.postedStr % ('Could not remove documents.');
      
      return result;
      
   def RemoveDocByID(self, doc_id):
      removed = self.parent.pubDb.RemoveDocument(doc_id, self.parent.avatarId);

      if removed == 'SUCCESS':
         result = self.parent.postedStr % ('Successfully removed document: ' + doc_id  + '.');
      else:
         result = self.parent.postedStr % ('Could not remove document: ' + doc_id + '.');
      
      return result;
      
   def RemoveDocByTopic(self, topic):
      removed = self.parent.pubDb.RemoveAllDocsOfTopicByUser(topic, self.parent.avatarId);

      if removed == 'SUCCESS':
         result = self.parent.postedStr % ('Successfully removed documents of topic: ' + topic  + '.');
      else:
         result = self.parent.postedStr % ('Could not remove documents of topic: ' + topic + '.');
      
      return result;

import hashlib

from twisted.web.resource import Resource

pubPage = '''
<!DOCTYPE html>
<html>
<body>

<table width="500" border="0">
   <tr>
      <td colspan="2">
      </td>
   </tr>

   <tr>
      <td style="width:100px;">
         <form method="POST" action="./">
            <p><input name="pub-topic" type="text" value=""/></p>
            <p><textarea name="pub-xml" cols=40 rows=20></textarea></p>
            <p> <input type="submit" value="Publish"></p>
            <p> <a href="/">Cancel</a> </p>
         </form>
      </td>
   </tr>

   <tr>
      <td colspan="2" style="text-align:center;">
      </td>
   </tr>
</table>

</body>
</html>'''

class PublisherPage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};

   def render_GET(self, request):
      return pubPage;
   
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
   
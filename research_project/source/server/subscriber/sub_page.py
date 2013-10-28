from twisted.web.resource import Resource

import cgi

subPage = '''
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
            <p>The topic to subscribe to...</p>
            <p><input name="sub-topic" type="text" value="Topic"/></p>
            <p> <input type="submit" value="Subscribe"></p>
         </form>
      </td>
   </tr>

   <tr>
      <td colspan="2" style="text-align:center;">
      </td>
   </tr>
</table>
<p> <a href="/">Cancel</a> </p>
</body>
</html>'''

class SubscribePage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};

   def render_GET(self, request):
      return subPage;
   
   def render_POST(self, request):
      # TODO: Handle subscription here!!!
      rt = self.parent.postedStr % ('Subscribed to ' + cgi.escape(request.args['sub-topic'][0]))      
   
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
         
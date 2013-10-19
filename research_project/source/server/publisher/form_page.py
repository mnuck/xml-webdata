from twisted.web.resource import Resource

import cgi

formPage = '''
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
         <form method="POST">
            <p><input name="pub-topic" type="text" value="Topic"/></p>
            <p><textarea name="pub-xml" cols=40 rows=30>Put your XML here...</textarea></p>
            <p> <input type="submit" value="Publish"></p>
         </form>
      </td>
      <td style="height:200px;width:400px;">
Subscriber stream will appear here ... TODO: Figure out how to do this!!!
      </td>
   </tr>

   <tr>
      <td colspan="2" style="text-align:center;">
      </td>
   </tr>
</table>

</body>
</html>'''

formPosted = '''
<html>
<body>
<p>
%s
</p>
<p>
%s
</p>
</body>
</html>'''

class FormPage(Resource):
   isLeaf = True;
   
   def __init__(self, db):
      Resource.__init__(self);
      self.db = db;

   def render_GET(self, request):
      return formPage;
   
   def render_POST(self, request):
      xmlStr = cgi.escape(request.args["pub-xml"][0]);
      topic  = cgi.escape(request.args["pub-topic"][0]);
      rt = formPosted % (topic, xmlStr);
      return rt;
   
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

import cgi

formPage = '''
<!DOCTYPE html>
<html>
<body>
<form method="POST">
   <div>
      <p><input name="pub-topic" type="text" value="Topic"/></p>
      <p><textarea name="pub-xml" cols=40 rows=30>Put your XML here...</textarea></p>
   </div>
   <div>
      <input type="submit" value="Publish">
   </div>
</form>
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
   def render_GET(self, request):
      # return '<html><body><form method="POST"><input name="the-field" type="text" /></form></body></html>'
      return formPage;
   
   def render_POST(self, request):
      xmlStr = cgi.escape(request.args["pub-xml"][0]);
      topic  = cgi.escape(request.args["pub-topic"][0]);
      rt = formPosted % (topic, xmlStr);
      return rt;

factory = Site(FormPage())
reactor.listenTCP(8880, factory)
reactor.run()

from twisted.web.resource import Resource

from publisher.pub_page import PublisherPage
from subscriber.sub_page import SubscribePage

mainPage = '''
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>CS437Project</title>
</head>
<body>
<style type="text/css">
a:link {
COLOR: #FFFFFF;
}
a:visited {
COLOR: #00CC00;
}
a:hover {
COLOR: #FF0000;
}
a:active {
COLOR: #00CC00;
}
</style>
<div id="container" style="width: 800px;">
<div id="header"
style="color: rgb(255, 255, 255); background-color: rgb(0, 66, 0);">
<h1 style="margin-bottom: 0pt;">CS437 Publisher/Subscriber Portal</h1>
</div>
<div id="menu"
style="color: rgb(255, 255, 255); background-color: rgb(0, 66, 0); height: 400px; width: 100px; float: left;">
<br>
<a href="/pub/?user=%s">Publish</a><br>
<br>
<a href="/sub/?user=%s">Subscribe</a><br>
</div>
<div id="content"
style="color: rgb(0, 0, 0); background-color: rgb(238, 238, 238); height: 400px; width: 700px; float: left;">
<div style="height: 400px; width: 350px; float: left;">Inside Content1
</div>
<div style="height: 400px; width: 350px; float: right;">Inside Content2
</div>
</div>
<div id="footer"
style="color: rgb(255, 255, 255); background-color: rgb(0, 66, 0); clear: both; text-align: left;">
</div>
</div>
</body>
</html>'''

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
   def __init__(self, db, avatarId):
      Resource.__init__(self);
      
      self.children = { 'pub': PublisherPage(self),
                        'sub': SubscribePage(self) };      
      self.db = db;
      self.avatarId = avatarId;
      self.postedStr = posted;

   def render_GET(self, request):
      print "render_GET", request;
      return mainPage % (self.avatarId, self.avatarId,);

   def getChild(self, name, request):
      print "getChild",name;
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;
      
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if 'pub-xml' in request.args and 'pub-topic' in request.args:
         rt = 'render_POST for pub-xml in root_page.  This should not happen!'
      elif 'sub-topic' in request.args:
         rt = 'render_POST for sub-topic in root_page.  This should not happen!';

      return rt;
   
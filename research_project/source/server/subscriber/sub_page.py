from twisted.web.resource import Resource

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
   children = {};
   
   def __init__(self):
      Resource.__init__(self);

   def render_GET(self, request):
      return subPage;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = SubscribePage.children[name];
      except KeyError:
         pass;
      
      return child;
         
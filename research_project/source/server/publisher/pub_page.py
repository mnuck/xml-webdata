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
            <p><input name="pub-topic" type="text" value="Topic"/></p>
            <p><textarea name="pub-xml" cols=40 rows=20>Put your XML here...</textarea></p>
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
   def __init__(self):
      Resource.__init__(self);

   def render_GET(self, request):
      return pubPage;
   
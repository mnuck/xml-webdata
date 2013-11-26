from twisted.web.resource import Resource

class EditorPage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the editor page HTML       
      self.content = open('html/edit.html', 'r').readlines();

   def render_GET(self, request):
      # TODO: If self.content is not a list, ditch the ''.join() stuff!
      try:
         doc_id = request.args['doc'][0];
         xpath  = request.args['xpath'][0];
      except KeyError:
         pass;

      doc = self.parent.xmlDb.GetPartialDoc(doc_id, xpath);

      script = "document.getElementById('xpath-input').value='" + xpath + "';\n";
      script = script + "document.getElementById('xmlarea').value='" + doc + "';\n";
      # TODO: Fix new lines in script.  They are ok as long as the line is continued
      #       with \ and an explict new line, \n, is added.
      # e.g.
      # document.getElementById('xmlarea').value="<category>\n\
      # <item>\n\
      # this is an item\n\
      # </item>\n\
      # </category>\n\
      # <item>\n\
      # this is an item\n\
      # </item>";      

      render = [];   
      for line in self.content:
         if '<!--SCRIPT-->' in line:
            render.append(script);
         else:
            render.append(line);

      return ''.join(render);
   
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;   
     

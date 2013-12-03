from twisted.web.resource import Resource

class DisplayPage(Resource):
   def __init__(self, parent, path):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      self.path = path;
      
      # Load in the editor page HTML       
      self.content = open('html/show.html', 'r').readlines();

   def render_GET(self, request):
      try:
         doc_id = request.args['doc'][0];
         xpath  = request.args['xpath'][0];
      except KeyError:
         pass;

      # TODO: Check xpath for validity against the security database.
      doc = self.parent.pubDb.GetPartialDoc(doc_id, xpath);

      modXpath = '';
      for x in xpath:
         if x == '\'':
            modXpath = modXpath + '\\\'';
         else:
            modXpath = modXpath + x;

      modDoc = '';
      for c in doc:
         if c == '\n':
            modDoc = modDoc + '\\\n'
         elif c == '"':
            modDoc = modDoc + '\\"';
         else:
            modDoc = modDoc + c;

      script = "document.getElementById('xpath-input').value='" + modXpath + "';\n";
      script = script + 'document.getElementById(\'xmlarea\').value=\"' + modDoc + '\";\n';
 
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
     

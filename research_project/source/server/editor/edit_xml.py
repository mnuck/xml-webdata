from twisted.web.resource import Resource

class EditorPage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the editor page HTML       
      self.content = open('html/edit.html', 'r').readlines();

   def render_GET(self, request):
      try:
         doc_id = request.args['doc'][0];
         xpath  = request.args['xpath'][0];
      except KeyError:
         pass;

      # TODO: Check xpath for validity against the security database.
      doc = self.parent.xmlDb.GetPartialDoc(doc_id, xpath);

      modDoc = '';
      for c in doc:
         if c == '\n':
            modDoc = modDoc + '\\\n'
         else:
            modDoc = modDoc + c;

      script = "document.getElementById('xpath-input').value='" + xpath + "';\n";
      script = script + 'document.getElementById(\'xmlarea\').value=\"' + modDoc + '\";\n';
      script = script + 'document.getElementById(\'doc-id\').value=\"' + doc_id + '\";\n';
 
      render = [];   
      for line in self.content:
         if '<!--SCRIPT-->' in line:
            render.append(script);
         else:
            render.append(line);

      return ''.join(render);
   
   def render_POST(self, request):
      rt = 'oops, invalid post data!'
      if 'xpath' in request.args and 'pub-xml' in request.args and 'doc' in request.args:
         xpath  = request.args["xpath"][0];
         pubXml = request.args["pub-xml"][0];
         doc_id = request.args["doc"][0];

         doc_publisher = self.parent.xmlDb.GetPublisherForDocId(doc_id)
         self.parent.xmlDb.UpdateDocument(doc_id, xpath, pubXml, doc_publisher[0][0]);
         
         rt = self.parent.postedStr % ('Document successfully posted with id: <b>' + doc_id + '</b>' );

      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;   
     

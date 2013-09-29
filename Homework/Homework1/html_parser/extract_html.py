from HTMLParser import HTMLParser

# pages with inline javascript sometimes blow this up
# like, for instance, http://cs.mst.edu


class HTMLAnchorAndTitleExtractor(HTMLParser):
    # Simple class constructor.
    def __init__(self):
       # Call the base class constructor
       HTMLParser.__init__(self)
       # 'attributes' is a list of tuples.
       self.anchors = []
       self.title = ""
       self.parsingTitle = False
       self.parsingAnchor = False
       self.parsingScript = False
       self.currentAnchor = []

    def handle_starttag(self, tag, attrs):
      tag = tag.lower()
      if not self.parsingScript:
        print "start tag!", tag
        if tag == 'a':
          self.currentAnchor = attrs
          self.parsingAnchor = True
          print "parsing an anchor:", attrs
        elif tag == 'title':
          self.parsingTitle = True
        elif tag == 'script':
          self.parsingScript = True

    def handle_endtag(self, tag):
      tag = tag.lower()
      if tag == 'script':
        self.parsingScript = False
      if not self.parsingScript:
        print "end tag!", tag
        if tag == 'a':
          self.parsingAnchor = False
        elif tag == 'title':
          self.parsingTitle = False

    def handle_data(self, data):
      if self.parsingAnchor:
        self.currentAnchor += tuple([data])
        self.anchors.append(self.currentAnchor)
        self.currentAnchor = []
      if self.parsingTitle:
        self.title += data

    # Accessor for anchorAttributes (strictly not necessary in python, but good form).
    def GetAnchorAttributes(self):
       return self.anchors

    def GetTitle(self):
      return self.title

from HTMLParser import HTMLParser

class HTMLAnchorExtractor(HTMLParser):
    # Simple class constructor.
    def __init__(self):
       # Call the base class constructor
       HTMLParser.__init__(self);
       # 'attributes' is a list of tuples.
       self.anchorAttributes = [];

    # handle_starttag method only recognizes and operates on anchor <A> tags...
    def handle_starttag(self, tag, attrs):
        if tag == 'a' or tag == 'A':
           for attr in attrs:
              self.anchorAttributes.append(attrs);

    # Accessor for anchorAttributes (strictly not necessary in python, but good form).
    def GetAnchorAttributes(self):
       return self.anchorAttributes;

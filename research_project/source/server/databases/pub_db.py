import sqlite3
try:
   import xml.etree.cElementTree as ET
except ImportError:
   import xml.etree.ElementTree as ET

class PublisherDatabase(object):
   def __init__(self, filename):
      self.conn = sqlite3.connect(filename)
      self.cur = self.conn.cursor()
      self.cur.execute("CREATE TABLE IF NOT EXISTS Documents (doc_id text, topic text, doc text, primary key (doc_id))")
      self.conn.commit();
   
   def InsertDocument(self, doc_id, topic, document):
      data = (doc_id, topic, document)
      try:
         #TODO: return something when doc couldn't be inserted due to duplicate key
         self.cur.execute("INSERT INTO Documents VALUES (?,?,?)", data)
         self.conn.commit();
      except sqlite3.IntegrityError:
         pass;

   def GetDocuments(self, topic):
      #TODO: need to verify users access level and only return docs
      #      they are allowed to access, likely another layer in between to handle this
      qstring = 'SELECT doc FROM Documents WHERE topic=\"' + topic + '\"';
      self.cur.execute(qstring)
      rows = self.cur.fetchall()
      return rows;
   
   def GetPartialDoc(self, doc_id, xpath):
      #TODO: verify access level
      #get doc matching id and put it in an element tree to perform xpath query
      qstring = 'SELECT doc FROM Documents WHERE doc_id=\"' + doc_id + '\"';
      self.cur.execute(qstring);
      doc = self.cur.fetchall();
      root = ET.fromstring(doc);
      #see http://docs.python.org/2/library/xml.etree.elementtree.html#supported-xpath-syntax
      #for supported xpath syntax
      #return a list of all subelements that match the xpath query
      return root.findall(xpath);
   
   def ReplaceDocument(self, doc_id, topic, url, document):
      data = (id, topic, document);
      qstring = 'SELECT doc FROM Documents WHERE doc_id=\"' + doc_id + '\"';
      self.cur.execute(qstring);
      if len(self.cur.fetchall()) > 0:
         #doc to update not found
         return(-1);
      else:
         qstring = 'DELETE FROM Documents WHERE doc_id=\"' + doc_id + '\"';
         self.cur.execute(qstring);
         self.cur.execute("INSERT INTO Documents VALUES (?,?,?)", data)
         self.conn.commit();
     
   def UpdateDocument(self, doc_id, xpath, document):
      #TODO: need to actually perform replacement and use 'write' to get
      #      a new XML string back to put back into the database
      qstring = 'SELECT doc_id, topic, doc FROM Documents WHERE doc_id=\"' + doc_id + '\"';
      self.cur.execute(qstring);
      doc = self.cur.fetchall();
      
      if len(doc) > 0:
         root = ET.fromstring(doc);
         partialDoc = root.findall(xpath);
         #TODO: replace partialDoc with document, not sure how yet
         qstring = 'DELETE FROM Documents WHERE doc_id=\"' + doc_id + '\"';
         self.cur.execute(qstring);
         #TODO: use ET.write() to write new document out to xml string and 
         #      replace doc[0].document with it
         new_data = (doc[0].id, doc[0].topic, ET.tostring(root, encoding='us-ascii', method='xml' ));
         self.cur.execute("INSERT INTO Documents VALUES (?,?,?)", new_data)
         self.conn.commit();
      else:
         return (-1);      

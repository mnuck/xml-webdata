import sqlite3

class PublisherDatabase(object):
   def __init__(self, filename):
      self.conn = sqlite3.connect(filename)
      self.cur = self.conn.cursor()
      self.cur.execute("DROP TABLE IF EXISTS Documents")
      self.cur.execute("CREATE TABLE Documents (topic text, url text, primary key (topic, url))")
   
   def InsertDocument(self, topic, document):
      data = (topic, document)
      try:
         self.cur.execute("INSERT INTO Documents VALUES (?,?)", data)
      except sqlite3.IntegrityError:
         pass

   def GetDocuments(self, topic):
      qstring = 'SELECT url FROM Documents WHERE topic=\"' + topic + '\"';
      self.cur.execute(qstring)
      rows = self.cur.fetchall()
      return rows;      

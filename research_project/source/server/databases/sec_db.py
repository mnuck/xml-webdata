import sqlite3

class SecurityDatabase(object):
   def __init__(self, filename):
      self.conn = sqlite3.connect(filename)
      self.cur = self.conn.cursor()
      self.cur.execute("CREATE TABLE IF NOT EXISTS Authorizations (doc_id text, user_id text, xpath text, primary key (doc_id,user_id,xpath))")
      self.conn.commit();
   
   def InsertAuthorization(self, user_id, doc_id, xpath):
      data = (doc_id, user_id, xpath)
      try:
         self.cur.execute("INSERT INTO Authorizations VALUES (?,?,?)", data)
         self.conn.commit();
      except sqlite3.IntegrityError:
         pass;

   def GetAuthorization(self, doc_id):
      qstring = 'SELECT user_id,xpath FROM Authorizations WHERE doc_id=\"' + doc_id + '\"';
      self.cur.execute(qstring)
      rows = self.cur.fetchall()
      return rows; 
   
   def GetDocsForUser(self, user):
      qstring = 'SELECT doc_id FROM Authorizations WHERE user_id=\"' + user + '\"';
      self.cur.execute(qstring)
      rows = self.cur.fetchall()
      return rows;
   
   def GetAuthUsers(self, doc):
      qstring = 'SELECT user_id FROM Authorizations WHERE doc_id=\"' + doc + '\"';
      self.cur.execute(qstring)
      rows = self.cur.fetchall()
      return rows;
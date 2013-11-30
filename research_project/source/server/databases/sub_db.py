import sqlite3

class SubscriberDatabase(object):
   def __init__(self, filename):
      self.conn = sqlite3.connect(filename)
      self.cur = self.conn.cursor()
      self.cur.execute("CREATE TABLE IF NOT EXISTS Subscribers (user_id text, topic text, primary key (user_id, topic))")
      self.conn.commit();
   
   def AddSubscription(self, user_id, topic):
      data = (user_id, topic)
      try:
         self.cur.execute("INSERT INTO Subscribers VALUES (?,?)", data)
         self.conn.commit();
         return (0);
      except sqlite3.IntegrityError:
         return (-1);

   def RemoveSubscription(self, user_id, topic):
      qstring = 'DELETE FROM Subscribers WHERE user_id=\"' + user_id + '\" AND topic=\"' + topic + '\"';
      try:
         self.cur.execute(qstring)
         self.conn.commit();
         return (0);
      except sqlite3.IntegrityError:
         return (-1);

   def RemoveAllSubscriptions(self):
      qstring = 'DELETE FROM Subscribers';
      try:
         self.cur.execute(qstring)
         self.conn.commit();
         return (0);
      except sqlite3.IntegrityError:
         return (-1);

   def RemoveAllTopicsForUser(self, user_id):
      qstring = 'DELETE FROM Subscribers where user_id=\"' + user_id + '\"';
      try:
         self.cur.execute(qstring)
         self.conn.commit();
         return (0);
      except sqlite3.IntegrityError:
         return (-1);

   def RemoveAllUsersForTopic(self, topic):
      qstring = 'DELETE FROM Subscribers where topic=\"' + topic + '\"';
      try:
         self.cur.execute(qstring)
         self.conn.commit();
         return (0);
      except sqlite3.IntegrityError:
         return (-1);

   def GetTopicsOfSubscriber(self, user_id):
      qstring = 'SELECT topic FROM Documents WHERE user_id=\"' + user_id + '\"';
      self.cur.execute(qstring);
      topics = self.cur.fetchall();
      return topics;
   
   def GetSubscribersOfTopic(self, topic):
      qstring = 'SELECT user_id FROM Documents WHERE topic=\"' + topic + '\"';
      self.cur.execute(qstring);
      users = self.cur.fetchall();
      return users;

   def GetAllUsers(self):
      qstring = 'SELECT user_id FROM Documents';
      self.cur.execute(qstring);
      users = self.cur.fetchall();
      return users;

   def GetAllTopics(self):
      qstring = 'SELECT topic FROM Documents';
      self.cur.execute(qstring);
      topics = self.cur.fetchall();
      return topics;
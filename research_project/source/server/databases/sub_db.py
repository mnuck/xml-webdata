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
         #TODO: add exception handling
         return (-1);

   def RemoveSubscription(self, user_id, topic):
      qstring = 'SELECT topic FROM Subscribers WHERE user_id=\"' + user_id + '\" AND topic=\"' + topic + '\"';
      try:
         self.cur.execute(qstring)
         topics = self.cur.fetchall();
      except sqlite3.IntegrityError:
         #TODO: add exception handling
         return 'ERROR';
         
      if len(topics) > 0:
         qstring = 'DELETE FROM Subscribers WHERE user_id=\"' + user_id + '\" AND topic=\"' + topic + '\"';
         try:
            self.cur.execute(qstring)
            self.conn.commit();
            return 'SUCCESS';
         except sqlite3.IntegrityError:
            #TODO: add exception handling
            return 'ERROR';
      else:
         return 'Not Found';

   def RemoveAllSubscriptions(self):
      qstring = 'SELECT user_id FROM Subscribers';
      try:
         self.cur.execute(qstring)
         users = self.cur.fetchall();
      except sqlite3.IntegrityError:
         #TODO: add exception handling
         return 'ERROR';

      if len(users) > 0:
         qstring = 'DELETE FROM Subscribers';
         try:
            self.cur.execute(qstring)
            self.conn.commit();
            return 'SUCCESS';
         except sqlite3.IntegrityError:
            #TODO: add exception handling
            return 'ERROR';
      else:
         return 'Not Found'

   def RemoveAllTopicsForUser(self, user_id):
      qstring = 'SELECT topic FROM Subscribers WHERE user_id=\"' + user_id + '\"';
      try:
         self.cur.execute(qstring)
         topics = self.cur.fetchall();
      except sqlite3.IntegrityError:
         #TODO: add exception handling
         return 'ERROR';

      if len(topics) > 0:
         qstring = 'DELETE FROM Subscribers where user_id=\"' + user_id + '\"';
         try:
            self.cur.execute(qstring)
            self.conn.commit();
            return 'SUCCESS';
         except sqlite3.IntegrityError:
            #TODO: add exception handling
            return 'ERROR';
      else:
         return 'Not Found';

   def RemoveAllUsersForTopic(self, topic):
      qstring = 'SELECT user_id FROM Subscribers WHERE topic=\"' + topic + '\"';
      try:
         self.cur.execute(qstring)
         users = self.cur.fetchall();
      except sqlite3.IntegrityError:
         #TODO: add exception handling
         return 'ERROR';

      if len(users) > 0:
         qstring = 'DELETE FROM Subscribers where topic=\"' + topic + '\"';
         try:
            self.cur.execute(qstring)
            self.conn.commit();
            return 'SUCCESS';
         except sqlite3.IntegrityError:
            #TODO: add exception handling
            return 'ERROR';
      else:
         return "Not Found"

   def GetTopicsOfSubscriber(self, user_id):
      qstring = 'SELECT topic FROM Subscribers WHERE user_id=\"' + user_id + '\"';
      self.cur.execute(qstring);
      topics = self.cur.fetchall();
      return topics;
   
   def GetSubscribersOfTopic(self, topic):
      qstring = 'SELECT user_id FROM Subscribers WHERE topic=\"' + topic + '\"';
      self.cur.execute(qstring);
      users = self.cur.fetchall();
      return users;

   def GetAllUsers(self):
      qstring = 'SELECT user_id FROM Subscribers';
      self.cur.execute(qstring);
      users = self.cur.fetchall();
      return users;

   def GetAllTopics(self):
      qstring = 'SELECT topic FROM Subscribers';
      self.cur.execute(qstring);
      topics = self.cur.fetchall();
      return topics;

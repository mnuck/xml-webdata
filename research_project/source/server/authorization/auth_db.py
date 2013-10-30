class AuthorizationDatabase(object):
   def __init__(self, authDbFile, sepChar):
      self.dbFile = authDbFile;
      self.sepChar = sepChar;

   def GetFile(self):
      return self.dbFile;

   def GetUserList(self):
      users = [];
      with open(self.dbFile, 'r') as f:
         for line in f:
            l = line.split(self.sepChar);
            users.append(l[0]);
      return users;
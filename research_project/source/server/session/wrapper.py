from twisted.web import guard
from twisted.cred.portal import Portal
from twisted.cred.checkers import FilePasswordDB

class SessionWrapper(object):
   def __init__(self, dbPassFile, realm):
      self.wrapper = guard.HTTPAuthSessionWrapper(
         Portal(realm, [FilePasswordDB(dbPassFile)]),
         [guard.DigestCredentialFactory('md5', 'Authentication required for CS437 - XML Web Data Pub/Sub')]);
      
   def GetWrapper(self):
      return self.wrapper;
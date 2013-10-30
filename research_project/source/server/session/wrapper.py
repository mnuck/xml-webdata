from twisted.web import guard
from twisted.cred.portal import Portal
from twisted.cred.checkers import FilePasswordDB

class SessionWrapper(object):
   def __init__(self, passDb):
      self.passwordDb = passDb;
      
   def GetWrapper(self, realm):
      wrapper = guard.HTTPAuthSessionWrapper(
         Portal(realm, [FilePasswordDB(self.passwordDb.GetFile())]),
         [guard.DigestCredentialFactory('md5', 'Authentication required for CS437 - XML Web Data Pub/Sub')])
      return wrapper
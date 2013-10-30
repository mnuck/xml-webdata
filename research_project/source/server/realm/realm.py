from zope.interface import implements
from twisted.web import resource
from twisted.cred.portal import IRealm

from root_page import RootPage

class Realm(object):
   """
   A realm which gives out L{RootPage} instances for authenticated users.
   """
   implements(IRealm)
   
   def __init__(self, db, authDb):
      self.pubdb = db;
      self.authDb = authDb;
   
   def requestAvatar(self, avatarId, mind, *interfaces):
      print "User",avatarId,"authenticated.";
      if resource.IResource in interfaces:
         return resource.IResource, RootPage(self.pubdb, self.authDb, avatarId), lambda: None
      raise NotImplementedError()
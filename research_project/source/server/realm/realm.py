from zope.interface import implements
from twisted.web import resource
from twisted.cred.portal import IRealm

from root_page import RootPage

class Realm(object):
   """
   A realm which gives out L{RootPage} instances for authenticated users.
   """
   implements(IRealm)
   
   def __init__(self, db, secDb, subDb, users):
      self.pubdb = db;
      self.authorizedUsers = users;
      self.secDb = secDb;
      self.subDb = subDb;
   
   def requestAvatar(self, avatarId, mind, *interfaces):
      print "User",avatarId,"authenticated.";
      if resource.IResource in interfaces:
         return resource.IResource, RootPage(self.pubdb, self.secDb, self.subDb, self.authorizedUsers, avatarId), lambda: None
      raise NotImplementedError()
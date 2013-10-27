#!/usr/bin/env python
import sys

from zope.interface import implements

from twisted.python import log
from twisted.internet import reactor
from twisted.web import server, resource, guard
from twisted.cred.portal import IRealm, Portal
# TODO: Replace this with a file-based checker!
from twisted.cred.checkers import FilePasswordDB

from publisher.pub_db import PublisherDatabase

from root_page import RootPage

# TODO: Remove this from global scope! (Is required for creation of RootPage).
# Create a database for shared use between the pub and the sub.
pubdb = PublisherDatabase('publisher.db');

# TODO: Move this to a file!  Rename it to something appropriate for this project.
class SimpleRealm(object):
   """
   A realm which gives out L{RootPage} instances for authenticated users.
   """
   implements(IRealm)
   
   def requestAvatar(self, avatarId, mind, *interfaces):
      print "User",avatarId,"authenticated.";
      if resource.IResource in interfaces:
         return resource.IResource, RootPage(pubdb,avatarId), lambda: None
      raise NotImplementedError()

def main():
   # TODO: Log to a file?!
   log.startLogging(sys.stdout);

   wrapper = guard.HTTPAuthSessionWrapper(
        Portal(SimpleRealm(), [FilePasswordDB('passwords.txt')]),
        [guard.DigestCredentialFactory('md5', 'Authentication required for CS437 - XML Web Data Pub/Sub')])

   # Publishers connect and post data on this port:
   pubFactory = server.Site(resource = wrapper);
   reactor.listenTCP(8025, pubFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();

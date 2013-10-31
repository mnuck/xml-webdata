#!/usr/bin/env python
import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.web import server

from databases.pub_db import PublisherDatabase
from databases.sec_db import SecurityDatabase
from session import SessionWrapper
from authorization import AuthorizationDatabase
from realm.realm import Realm

def main():
   # TODO: Log to a file?!
   log.startLogging(sys.stdout);

   # Create the databases shared between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');
   secdb = SecurityDatabase('security.db');
   
   authDb = AuthorizationDatabase('authorization/passwords.txt', ':')
   
   r = Realm(pubdb, secdb, authDb.GetUserList()); # Use 'r' just for Aaron! ;-)
   
   # Create a session wrapper for authentication
   wrapper = SessionWrapper(authDb.GetFile(), r);   

   pubFactory = server.Site(resource = wrapper.GetWrapper());
   reactor.listenTCP(8025, pubFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();

#!/usr/bin/env python
import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.web import server

from databases.pub_db import PublisherDatabase
from session import SessionWrapper
from realm.realm import Realm

def main():
   # TODO: Log to a file?!
   log.startLogging(sys.stdout);

   # Create a database for shared use between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');
   
   # Create a session wrapper for authentication
   wrapper = SessionWrapper('authorization/passwords.txt');

   r = Realm(pubdb); # Just for Aaron! ;-)

   pubFactory = server.Site(resource = wrapper.GetWrapper(r));
   reactor.listenTCP(8025, pubFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();

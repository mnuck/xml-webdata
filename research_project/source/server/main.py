#!/usr/bin/env python
from twisted.internet import reactor
from twisted.web.server import Site

from publisher.pub_db import PublisherDatabase

from root_page import RootPage

def PushData(pubdb, subFactory):
   for subClient in subFactory.clients:
      subClient.PushData(pubdb);
   reactor.callLater(1, PushData, pubdb, subFactory);

def main():
   # Create a database for shared use between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');

   # Publishers connect and post data on this port:
   pubFactory = Site(RootPage(pubdb))
   reactor.listenTCP(8025, pubFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();


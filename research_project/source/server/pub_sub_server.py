#!/usr/bin/env python
from twisted.internet import reactor

from pub_factory import PubFactory
from sub_factory import SubFactory
from pub_db import PublisherDatabase

def PushData(pubFactory, subFactory):
   for subClient in subFactory.clients:
      subClient.PushData(pubFactory);
   reactor.callLater(1, PushData, pubFactory, subFactory);

def main():
   # Create a database for shared use between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');

   # Publishers connect and post data on this port:
   pubFactory = PubFactory(pubdb);
   reactor.listenTCP(8025, pubFactory);

   # Subscribers connect and fetch data on this port:
   subFactory = SubFactory(pubdb);
   reactor.listenTCP(8181, subFactory);

   # Once per second, push the subscription data to
   # the clients
   reactor.callLater(1, PushData, pubFactory, subFactory);

   reactor.run();

if '__main__' == __name__:
   main();



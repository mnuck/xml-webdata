#!/usr/bin/env python
from twisted.internet import reactor

from subscriber.sub_factory import SubFactory
from publisher.pub_db import PublisherDatabase
from publisher.form_page import FormPage
from twisted.web.server import Site

def PushData(pubdb, subFactory):
   for subClient in subFactory.clients:
      subClient.PushData(pubdb);
   reactor.callLater(1, PushData, pubdb, subFactory);

def main():
   # Create a database for shared use between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');

   # Publishers connect and post data on this port:
   # pubFactory = PubFactory(FormPage(), pubdb);
   pubFactory = Site(FormPage(pubdb))
   reactor.listenTCP(8025, pubFactory);

   # Subscribers connect and fetch data on this port:
   subFactory = SubFactory(pubdb);
   reactor.listenTCP(8181, subFactory);

   # Once per second, push the subscription data to
   # the clients
   # TODO: Instead of pushing every second, push data to the
   #       clients only when they request it?
   reactor.callLater(1, PushData, pubdb, subFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();


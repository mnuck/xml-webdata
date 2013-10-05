#!/usr/bin/env python
from twisted.internet import reactor

from pub_factory import PubFactory

def main():
   reactor.listenTCP(1025, PubFactory());
   reactor.run();

if '__main__' == __name__:
   main();



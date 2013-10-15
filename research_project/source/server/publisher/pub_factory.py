from pub_protocol import PubProtocol

from twisted.internet import protocol

#
#  The publisher factory.  This class creates instances
#  of the PubProtocol class when a new publisher client
#  connects.
#

class PubFactory(protocol.Factory):
   def __init__(self, pubdb):
      # Book keep the clients for convenience.
      self.clients = set()
      # Store a reference to the shared database.
      self.pubdb = pubdb;
   
   def buildProtocol(self, addr):
      # Called when a client connects and a protocol instance
      # is needed.
      return PubProtocol(self)

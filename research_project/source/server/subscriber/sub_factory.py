from sub_protocol import SubProtocol

from twisted.internet import protocol

class SubFactory(protocol.Factory):
   def __init__(self, pubdb):
      self.clients = set()
      self.pubdb = pubdb;
   
   def buildProtocol(self, addr):
      return SubProtocol(self)

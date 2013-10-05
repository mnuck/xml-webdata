from pub_protocol import PubProtocol

from twisted.internet import protocol

class PubFactory(protocol.Factory):
    def __init__(self, pubdb):
        self.clients = set()
        self.pubdb = pubdb;

    def buildProtocol(self, addr):
        return PubProtocol(self)

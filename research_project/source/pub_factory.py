from pub_protocol import PubProtocol

from twisted.internet import protocol

class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)

from twisted.protocols import basic

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
       print "Publisher sent: ", line

       # Publisher on this port writes: <topic> <url>
       # Note: later wrap this in XML.  For now, just
       # text strings and insert them into the db.
       # (yes, this is bad for NOW!)
       strs = line.split();
       # BAD BAD BAD: assume [0] = topic, [1] = url
       self.factory.pubdb.InsertDocument(strs[0], strs[1]);

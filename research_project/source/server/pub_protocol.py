from twisted.protocols import basic

#
#  Instances of this class handle communication with the
#  publisher clients.  The clients will publish data in
#  the system (broker) through this class.
#

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        # For convenience store reference to the creator factory.
        self.factory = factory

    def connectionMade(self):
        # Connection established, store the protocol object in
        # the creator factory's clients list.
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        # Connection closed, remove the book keeping.
        self.factory.clients.remove(self)

    def lineReceived(self, line):
       # Called when data is sent from the publisher client.
       print "Publisher sent: ", line

       # Publisher on this port writes: <topic> <url>
       # Note: later wrap this in XML.  For now, just
       # text strings and insert them into the db.
       # (yes, this is bad for NOW!)
       strs = line.split();
       # BAD BAD BAD: assume [0] = topic, [1] = url
       self.factory.pubdb.InsertDocument(strs[0], strs[1]);

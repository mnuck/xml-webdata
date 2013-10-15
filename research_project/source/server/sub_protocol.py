from twisted.protocols import basic

class SubProtocol(basic.LineReceiver):
   def __init__(self, factory):
      self.factory = factory
      self.subTopic = None;
   
   def connectionMade(self):
      self.factory.clients.add(self)
   
   def connectionLost(self, reason):
      self.factory.clients.remove(self)
   
   def lineReceived(self, line):
      print "Subscriber set topic to: ", line
   
      # Set the topic to the input line.
      self.subTopic = line;
   
   def PushData(self, pubFactory):
      if self.subTopic != None:
         urls = pubFactory.pubdb.GetDocuments(self.subTopic);
         for url in urls:
            # TODO: revise this to write XML
            self.transport.write(url[0].encode('ascii') + '\n');
         
         # Clear the request so data isn't streamed endlessly.
         # TODO: Need a away to handle this such that data for
         #       the requested topic is sent only once yet any
         #       new entries for that topic are also pushed to
         #       the subscribers.
         self.subTopic = None;

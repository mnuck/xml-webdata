from twisted.web.resource import Resource

import cgi

class SubscribePage(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      
      # Load in the subscriber page HTML 
      self.content = open('html/subscribe.html', 'r').read();      

   def render_GET(self, request):
      return self.content;
   
   def render_POST(self, request):
      rt = self.parent.postedStr % ('');
      if request.args.Subscribe == 'Subscribe':
         rt = self.Subscribe(request.args['sub-topic'][0]);
      elif request.args.Remove == 'Remove Subscription':
         rt = self.Remove(request.args['sub-topic'][0]);
      elif request.args.RemoveAll == 'Remove All Subscriptions':
         rt = self.RemoveAll();
      return rt;
   
   def getChild(self, name, request):
      child = self;
      try:
         child = self.children[name];
      except KeyError:
         pass;
      
      return child;

   def Subscribe(self, topic):
      failed = self.parent.subDb.AddSubscription(self.parent.avatarId, topic);
      if failed:
         rt = self.parent.postedStr % ('Could not subscribe to ' + topic);
      else:
         rt = self.parent.postedStr % ('Subscribed to ' + topic);
      return rt;

   def Remove(self, topic):
      failed = self.parent.subDb.RemoveSubscription(self.parent.avatarId, topic);
      if failed:
         rt = self.parent.postedStr % ('Could not remove subscription to ' + topic);
      else:
         rt = self.parent.postedStr % ('Removed subscription to ' + topic);
      return rt;

   def RemoveAll(self):
      failed = self.parent.subDb.RemoveAllTopicsForUser(self.parent.avatarId);
      if failed:
         rt = self.parent.postedStr % ('Could not remove all subscriptions');
      else:
         rt = self.parent.postedStr % ('Removed all subscriptions');
      return rt;
         
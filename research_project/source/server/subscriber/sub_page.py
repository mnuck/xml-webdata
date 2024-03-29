from twisted.web.resource import Resource

import cgi

class SubscribePage(Resource):
   def __init__(self, parent, path):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};
      self.path = path;
      
      # Load in the subscriber page HTML 
      self.content = open('html/subscribe.html', 'r').read();      

   def render_GET(self, request):
      return self.content;
   
   def render_POST(self, request):
      rt = self.parent.postedStr % ('',self.path);
      if 'Subscribe' in request.args:
         rt = self.Subscribe(request.args['sub-topic'][0]);
      elif 'Remove' in request.args:
         rt = self.Remove(request.args['sub-topic'][0]);
      elif 'RemoveAll' in request.args:
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
         rt = self.parent.postedStr % ('Could not subscribe to ' + topic + '.', self.path);
      else:
         rt = self.parent.postedStr % ('Subscribed to ' + topic + '.', self.path);
      return rt;

   def Remove(self, topic):
      result = self.parent.subDb.RemoveSubscription(self.parent.avatarId, topic);
      if result == 'Not Found':
         rt = self.parent.postedStr % ('You are not subscribed to ' + topic + '.', self.path);
      elif result == 'SUCCESS':
         rt = self.parent.postedStr % ('Removed subscription to ' + topic + '.', self.path);
      return rt;

   def RemoveAll(self):
      result = self.parent.subDb.RemoveAllTopicsForUser(self.parent.avatarId);
      if result == 'Not Found':
         rt = self.parent.postedStr % ('You do not have any subscriptions to remove.', self.path);
      elif result == 'SUCCESS':
         rt = self.parent.postedStr % ('Removed all subscriptions.', self.path);
      return rt;
         
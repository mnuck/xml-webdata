from twisted.web.resource import Resource

class SubDocs(Resource):
   def __init__(self, parent):
      Resource.__init__(self);
      self.parent = parent;
      self.children = {};     

   def render_GET(self, request):
      render = [];
      
      # Get the current user's subscribed topics
      subTopics = self.parent.subDb.GetTopicsOfSubscriber(self.parent.avatarId);
      
      # See which of those are published
      for t in subTopics:
         # Verify that of the published topics, the current user is granted access.
         topic = str(t[0]);
         docsForTopic = self.parent.pubDb.GetDocIds(topic);
         for d in docsForTopic:
            doc = str(d[0]);
            authUsers = self.parent.secDb.GetAuthUsers(doc);
            for user in authUsers:
               if self.parent.avatarId == str(user[0]):
                  render.append(topic + "<br>\n");
      
      # Return the set from the preceding operations.
      return ''.join(render);

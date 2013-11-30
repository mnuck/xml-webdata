#!/usr/bin/env python
import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.web import server

from databases.pub_db import PublisherDatabase
from databases.sec_db import SecurityDatabase
from databases.sub_db import SubscriberDatabase
from session import SessionWrapper
from authorization import AuthorizationDatabase
from realm.realm import Realm

def main():
   # TODO: Log to a file?!
   log.startLogging(sys.stdout);

   # Create the databases shared between the pub and the sub.
   pubdb = PublisherDatabase('publisher.db');
   secdb = SecurityDatabase('security.db');
   subdb = SubscriberDatabase('subscriber.db');
   
   # Used for logging into the portal.  Strictly part of the security model?
   authDb = AuthorizationDatabase('authorization/passwords.txt', ':')
   
   # Use 'thisIsTheVariableNameOfTheRealmThatIsInUseDuringThisRun' just for Tom! ;-)
   thisIsTheVariableNameOfTheRealmThatIsInUseDuringThisRun = Realm(pubdb, secdb, authDb.GetUserList());
   
   # Create a session wrapper for authentication
   wrapper = SessionWrapper(authDb.GetFile(), thisIsTheVariableNameOfTheRealmThatIsInUseDuringThisRun);   

   pubFactory = server.Site(resource = wrapper.GetWrapper());
   reactor.listenTCP(8025, pubFactory);

   # Start the main loop.
   reactor.run();

if '__main__' == __name__:
   main();

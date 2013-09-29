# Put your own Google API developer key and search engine ID in a file
# file called personal_data.py
# The file should contain the statement:
#    myKey = 'yourGoogleApiDeveloperKey';
#    mySearchID = 'yourSearchEngineID';
# If you don't have it, don't expect this line to work:

import personal_data
from apiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
                  developerKey=personal_data.myKey)

  res = service.cse().list(q='Secure+XML',
                           cx=personal_data.mySearchID).execute()

  print res
#  pprint.pprint(res)

if __name__ == "__main__":
  main()

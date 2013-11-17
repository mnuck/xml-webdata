#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/mnuck/zorba-2.9.1/build/dist/share/python')
import zorba_api

with open("Things.xml", 'r') as f:
	raw_data = f.read()

store = zorba_api.InMemoryStore_getInstance()
zorba = zorba_api.Zorba_getInstance(store)

doc = zorba_api.Item_createEmptyItem()
dataManager = zorba.getXmlDataManager()
docIter = dataManager.parseXML(raw_data)
docIter.open()
docIter.next(doc)

docManager = dataManager.getDocumentManager()
docManager.put("things.xml", doc)


query = '''
for $x in doc('things.xml')/THINGS/PHONEBOOK/PHONE
return ($x/NAME, $x/OFFICE)
'''
xquery = zorba.compileQuery(query)
print xquery.execute()


query = '''
<ul>
{
for $x in doc('things.xml')/THINGS/PHONEBOOK/PHONE
return <li>
<b>{data($x/NAME/LAST)}</b>
<i>{data($x/OFFICE)}</i>
</li>
}
</ul>
'''
xquery = zorba.compileQuery(query)
print xquery.execute()


query = '''
{
for $x in doc('things.xml')/THINGS/FACULTY/FACULTY_MEMBER
let $b := doc('things.xml')/THINGS/PHONEBOOK/PHONE[NAME/FIRST = $x/NAME/FIRST and NAME/LAST = $x/NAME/LAST]
where $x/YEAR > 1990
  and $x/POSITION = 'Assistant Professor'
return ($x/NAME, $b/EMAIL, $x/INTERESTS)
}
'''
xquery = zorba.compileQuery(query)
print xquery.execute()




zorba.shutdown()
zorba_api.InMemoryStore_shutdown(store)

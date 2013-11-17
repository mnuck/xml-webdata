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


def xquery1():
	query = '''
	for $x in doc('things.xml')/THINGS/PHONEBOOK/PHONE
	return ($x/NAME, $x/OFFICE)
	'''
	xquery = zorba.compileQuery(query)
	with open('xquery1.out', 'w') as f:
		f.write(xquery.execute())


def xquery2():
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
	with open('xquery2.out.html', 'w') as f:
		f.write(xquery.execute())


def xquery3():
	query = '''
	{
	for $x in doc('things.xml')/THINGS/FACULTY/FACULTY_MEMBER
	let $b := doc('things.xml')/THINGS/PHONEBOOK/PHONE[NAME/FIRST = $x/NAME/FIRST 
	                                               and NAME/LAST  = $x/NAME/LAST]
	where $x/YEAR > 1990
	  and $x/POSITION = 'Assistant Professor'
	return ($x/NAME, $b/EMAIL, $x/INTERESTS)
	}
	'''
	xquery = zorba.compileQuery(query)
	with open('xquery3.out', 'w') as f:
		f.write(xquery.execute())


def xquery4():
	query = '''
	for $x in doc('things.xml')/THINGS/FACULTY/FACULTY_MEMBER[contains(INTERESTS, 'databases')
	                                                       or contains(INTERESTS, 'intelligence')]
	let $b := doc('things.xml')/THINGS/CATALOG/COURSE_INFO[lower-case(INSTRUCTOR/LAST) = lower-case($x/NAME/LAST)]
	return ($x/NAME/FIRST, $x/NAME/LAST, $x/POSITION, $x/INTERESTS, $b/COURSE)
	'''
	xquery = zorba.compileQuery(query)
	with open('xquery4.out', 'w') as f:
		f.write(xquery.execute())


def xquery5():
	query = '''
	for $x in doc('things.xml')/THINGS/FACULTY/FACULTY_MEMBER
	let $b := doc('things.xml')/THINGS/OFFICE_HOURS_LISTING/OFFICE_HOURS[NAME/LAST = $x/NAME/LAST 
	                                                                 and contains(HOURS, 'by appointment')]
	return ($x/NAME/FIRST, $x/NAME/LAST)
	'''
	xquery = zorba.compileQuery(query)
	with open('xquery5.out', 'w') as f:
		f.write(xquery.execute())


def xquery6():
	query = '''
	for $x in doc('things.xml')/THINGS/PHONEBOOK/PHONE
	let $b := doc('things.xml')/THINGS/CATALOG/COURSE_INFO[NAME/LAST = $x/NAME/LAST]
	return ($x/NAME/LAST, $x/PHONE)
	'''
	xquery = zorba.compileQuery(query)
	with open('xquery6.out', 'w') as f:
		f.write(xquery.execute())


xquery1()
xquery2()
xquery3()
xquery4()
xquery5()
xquery6()

zorba.shutdown()
zorba_api.InMemoryStore_shutdown(store)

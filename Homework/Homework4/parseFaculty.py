#!/usr/bin/env python
#
# Homework 4
# Thomas Guenther
# Matthew Nuckolls
# Aaron Powers

import re
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

input_filename = "Faculty.txt"
output_filename = "Faculty.xml"

with open(input_filename, 'r') as f:
	raw_data = f.readlines()

raw_data = [x.strip() for x in raw_data]  # strip newlines

with open(output_filename, 'w') as f:
	topmost_e = Element("FACULTY")
	tree = ET(topmost_e)	
	for row in raw_data:
		record = row.split(',')
		record = [x.strip() for x in record]
		record[-1] = record[-1][:-1] # strip trailing period
		name = record[0]

		# some names are two words, some names are three
		some_names = name.split(' ')
		if len(some_names) == 2:
			firstname = some_names[0]
			lastname = some_names[1]
			middlename = None
		elif len(some_names) == 3:
			(firstname, middlename, lastname) = some_names

		position = record[1]

		# Some universities have a comma in their name,
		# because they are fundamentally bad people.
		index_of_year = 0
		for i in xrange(len(record)):
			if re.match('^\d+\.?$', record[i]):
				index_of_year = i
				break

		alma = ', '.join(record[2:index_of_year])
		year = record[index_of_year]
		if index_of_year != len(record) - 1:
			interests = ", ".join(record[index_of_year + 1:])
		root_e = SubElement(topmost_e, "FACULTY_MEMBER")
		name_e = SubElement(root_e, "NAME")
		first_e = SubElement(name_e, "FIRST")
		first_e.text = firstname
		if middlename is not None:
			middle_e = SubElement(name_e, "MIDDLE")
			middle_e.text = middlename
		last_e = SubElement(name_e, "LAST")
		last_e.text = lastname
		position_e = SubElement(root_e, "POSITION")
		position_e.text = position
		education_e = SubElement(root_e, "EDUCATION")
		education_e.text = alma
		year_e = SubElement(root_e, "YEAR")
		year_e.text = year
		if index_of_year != len(record) - 1:
			interests_e = SubElement(root_e, "INTERESTS")
			interests_e.text = interests
	tree.write(f)
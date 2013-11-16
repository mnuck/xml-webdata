#!/usr/bin/env python

import re
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

input_filename = "Faculty.txt"
output_filename = "Faculty.xml"

with open(input_filename, 'r') as f:
	raw_data = f.readlines()

raw_data = [x.strip() for x in raw_data]  # strip newlines

with open(output_filename, 'w') as f:
	for row in raw_data:
		record = row.split(',')
		record = [x.strip() for x in record]
		record[-1] = record[-1][:-1] # strip trailing period
		name = record[0]
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
		root_e = Element("FACULTY MEMBER")
		name_e = SubElement(root_e, "NAME")
		name_e.text = name
		position_e = SubElement(root_e, "POSITION")
		position_e.text = position
		education_e = SubElement(root_e, "EDUCATION")
		education_e.text = alma
		year_e = SubElement(root_e, "YEAR")
		year_e.text = year
		if index_of_year != len(record) - 1:
			interests_e = SubElement(root_e, "INTERESTS")
			interests_e.text = interests
		element = ET(root_e)
		element.write(f)
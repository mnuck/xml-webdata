#!/usr/bin/env python

import re
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

input_filename = "Office.txt"
output_filename = "Office.xml"

with open(input_filename, 'r') as f:
	raw_data = f.readlines()

raw_data = [x.strip() for x in raw_data]  # strip newlines
raw_data = raw_data[:-1]                   # remove the header line

name_re = r"^(.*?)"
office_re = r"\(([\w \d]+)\)$"
matcher = " ".join([name_re, office_re])

gathering_hours = False
hours = ""
with open(output_filename, 'w') as f:
	topmost_e = Element("PHONEBOOK")
	tree = ET(topmost_e)
	for row in raw_data:
		if not gathering_hours:
			gathering_hours = True
			match = re.match(matcher, row)
			if match is not None:
				(name, office) = match.groups()
			hours = ''
			(name, office) = match.groups()
			# some names are two words, some names are three
			some_names = name.split(' ')
			if len(some_names) == 2:
				firstname = some_names[0]
				lastname = some_names[1]
				middlename = None
			elif len(some_names) == 3:
				(firstname, middlename, lastname) = some_names
		else:
			if row != '':
				hours += row + '\n'
			else:
				gathering_hours = False
				hours = hours.strip()
				root_e = SubElement(topmost_e, "OFFICE_HOURS")
				name_e = SubElement(root_e, "NAME")
				if firstname is not None:
					first_e = SubElement(name_e, "FIRST")
					first_e.text = firstname
				if middlename is not None:
					middle_e = SubElement(name_e, "MIDDLE")
					middle_e.text = middlename
				if lastname is not None:
					last_e = SubElement(name_e, "LAST")
					last_e.text = lastname
				office_e = SubElement(root_e, "OFFICE")
				office_e.text = office
				hours_e = SubElement(root_e, "HOURS")
				hours_e.text = hours
	tree.write(f)

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
	for row in raw_data:
		if not gathering_hours:
			gathering_hours = True
			match = re.match(matcher, row)
			if match is not None:
				(name, office) = match.groups()
			hours = ''
			(name, office) = match.groups()
		else:
			if row != '':
				hours += row + '\n'
			else:
				gathering_hours = False
				hours = hours.strip()
				root_e = Element("OFFICE HOURS")
				name_e = SubElement(root_e, "FACULTY")
				name_e.text = name
				office_e = SubElement(root_e, "OFFICE")
				office_e.text = office
				hours_e = SubElement(root_e, "HOURS")
				hours_e.text = hours
				element = ET(root_e)
				element.write(f)

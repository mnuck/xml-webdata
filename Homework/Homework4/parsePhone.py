#!/usr/bin/env python

import re
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

input_filename = "Phone.txt"
output_filename = "Phone.xml"

with open(input_filename, 'r') as f:
	raw_data = f.readlines()

raw_data = [x.strip() for x in raw_data]  # strip newlines
raw_data = raw_data[1:]                   # remove the header line

name_re = r"^(\w+, \w+)"
office_re = r"(\w+ \d+\w?)"
phone_re = r"(\d\-\d\d\d\d)"
email_re = r"([\w\.@]+)$"
matcher = " ".join([name_re, office_re, phone_re, email_re]) 

with open(output_filename, 'w') as f:
	for row in raw_data:
		match = re.match(matcher, row)
		if match is not None:
			(name, office, phone, email) = re.search(matcher, row).groups()
			firstname = None
			middlename = None
			lastname = None
			some_names = name.split(' ')
			if len(some_names) == 2:
				firstname = some_names[1]
				lastname = some_names[0][:-1]
				middlename = None
			elif len(some_names) == 3:
				(firstname, middlename, lastname) = some_names
				lastname = lastname[:-1]


			root_e = Element("FACULTY PHONE RECORD")
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
			phone_e = SubElement(root_e, "PHONE")
			phone_e.text = phone
			email_e = SubElement(root_e, "EMAIL")
			email_e.text = email
			element = ET(root_e)
			element.write(f)
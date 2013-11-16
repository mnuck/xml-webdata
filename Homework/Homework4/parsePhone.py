#!#/usr/bin/env python

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
			root_e = Element("FacultyPhoneType")
			name_e = SubElement(root_e, "FACULTY")
			name_e.text = name
			office_e = SubElement(root_e, "OFFICE")
			office_e.text = office
			phone_e = SubElement(root_e, "PHONE")
			phone_e.text = phone
			email_e = SubElement(root_e, "EMAIL")
			email_e.text = email
			element = ET(root_e)
			element.write(f)
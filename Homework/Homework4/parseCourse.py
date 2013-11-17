#!/usr/bin/env python
#
# Homework 4
# Thomas Guenther
# Matthew Nuckolls
# Aaron Powers

import re
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# from http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

input_filename = "Course.txt"
output_filename = "Course.xml"

with open(input_filename, 'r') as f:
	raw_data = f.readlines()

raw_data = [x.strip() for x in raw_data]  # strip newlines

records = chunks(raw_data, 3)

name_re = r"^(.*?)\."
hours_re = r"\((\d+)\)$"
prereq_re = r"Prerequisite: (.*?)\."
instructor_re = r"Instructor: (.*?)\.$"
first_matcher = " ".join([name_re, hours_re])
with open(output_filename, 'w') as f:
	topmost_e = Element("CATALOG")
	tree = ET(topmost_e)
	for record in records:
		first_line = record[0]
		second_line = record[1]
		match = re.match(first_matcher, first_line)
		if match is not None:
			(name, hours) = match.groups()
		prereq_match = re.search(prereq_re, second_line)
		if prereq_match is not None:
			prereq_to_strip = prereq_match.group(0)
			second_line = second_line.replace(prereq_to_strip, '')
			prereqs = prereq_match.group(1)
		instructor_match = re.search(instructor_re, second_line)
		if instructor_match is not None:
			instructor_to_strip = instructor_match.group(0)
			second_line = second_line.replace(instructor_to_strip, '')
			instructor = instructor_match.group(1)

			# some names are two words, some names are three
			some_names = instructor.split(' ')
			if len(some_names) == 1:
				firstname = None
				middlename = None
				lastname = some_names[0]
			elif len(some_names) == 2:
				firstname = some_names[0]
				lastname = some_names[1]
				middlename = None
			elif len(some_names) == 3:
				(firstname, middlename, lastname) = some_names

		description = second_line

		root_e = SubElement(topmost_e, "COURSE_INFO")
		name_e = SubElement(root_e, "COURSE")
		name_e.text = name
		credits_e = SubElement(root_e, "CREDIT_HOURS")
		credits_e.text = hours
		description_e = SubElement(root_e, "DESCRIPTION")
		description_e.text = description
		if prereq_match is not None:
			prereqs_e = SubElement(root_e, "REQUIREMENTS")
			prereqs_e.text = prereqs
		if instructor_match is not None:
			instructor_e = SubElement(root_e, "INSTRUCTOR")
			if firstname is not None:
				first_e = SubElement(instructor_e, "FIRST")
				first_e.text = firstname
			if middlename is not None:
				middle_e = SubElement(instructor_e, "MIDDLE")
				middle_e.text = middlename
			if lastname is not None:
				last_e = SubElement(instructor_e, "LAST")
				last_e.text = lastname
	tree.write(f)

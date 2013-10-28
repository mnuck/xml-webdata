#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3

import json

def oid_to_string(oid, OEM, prefix):
	tup = OEM[oid]
	result = prefix + tup[0]
	if tup[1] == "SET":
		result += set_to_string(tup[2], prefix + "  ")
	else:
		result += " " + str(tup[2])
	return result


def set_to_string(input, OEM, prefix=""):
	result = ""
	for oid in input:
		result += "\n" + oid_to_string(oid, OEM, prefix)
	return result


def loadOEM(filename):
	with open("OEM.txt") as f:
		raw_data = f.read()
	return json.loads(raw_data)
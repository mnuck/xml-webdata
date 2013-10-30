#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3

# Utility functions to read the OEM from a file,
# parse tuples into human-readable output,
# and construct Lindex and Vindex objects

from collections import defaultdict
import json


class vindex(object):
    def __init__(self, OEM, lindex, labels):
        self.string = dict()
        self.real = dict()
        self.coerced = dict()
        for (oid, label) in lindex:
            if label not in labels or OEM[oid][1] == "SET":
                continue
            for index in [self.string, self.real, self.coerced]:
                if label not in index:
                    index[label] = list()
            value = OEM[oid][2]
            self.string[label].append((oid, str(value)))
            if type(value) in [type(0), type(0.0)]:
                self.real[label].append((oid, value))
            else:
                try:
                    self.coerced[label].append((oid, float(value)))
                except ValueError:
                    pass

    # Given a label, operator, and value, return all oids
    # for which operator(stored_value, value) returns true.
    # Account for coersion rules as per the source paper.
    def match(self, label, operator, rvalue):
        result = set()
        if type(rvalue) in [type(0), type(0.0)]:
            for (oid, stored_value) in self.real[label]:
                if operator(stored_value, rvalue):
                    result.add(oid)
            for (oid, stored_value) in self.coerced[label]:
                if operator(stored_value, rvalue):
                    result.add(oid)
        else:
            for (oid, stored_value) in self.string[label]:
                if operator(stored_value, rvalue):
                    result.add(oid)
            try:
                coerced = float(rvalue)
                for (oid, stored_value) in self.real[label]:
                    if operator(stored_value, coerced):
                        result.add(oid)
            except ValueError:
                pass

        return result


# Construct a key:value map where the keys look like (child_oid, label)
# and the values look like parent_oid, for all oids in OEM, where label
# is in labels.
def construct_lindex(OEM, labels):
    result = defaultdict(list)
    for parent in OEM:
        if parent == "root":
            continue
        if OEM[parent][1] == "SET":
            for child in OEM[parent][2]:
                label = OEM[child][0]
                if label in labels:
                    key = (child, OEM[child][0])
                    if key not in result:
                        result[key] = list()
                    result[key].append(parent)
    return result


# thin wrapper around vindex constructor.
def construct_vindex(OEM, lindex, labels):
    return vindex(OEM, lindex, labels)


# Given an oid, display all values in the subtree in a human readable format.
def oid_to_string(oid, OEM, prefix):
    tup = OEM[oid]
    result = prefix + tup[0]
    if tup[1] == "SET":
        result += set_to_string(tup[2], OEM, prefix + "  ")
    else:
        result += " " + str(tup[2])
    return result

# Given an oid for which the value is a set, display all values in the subtree
# in a human readable format.
def set_to_string(input, OEM, prefix=""):
    result = ""
    for oid in input:
        result += "\n" + oid_to_string(oid, OEM, prefix)
    return result


# Load the OEM from the JSON encoded file.
def loadOEM(filename):
    with open("OEM.txt") as f:
        raw_data = f.read()
    return json.loads(raw_data)

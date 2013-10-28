#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3

# We are implementing the LORE query plan for the following query:
# SELECT DBGroup.Member.Office
# WHERE  DBGroup.Member.Age > 30

# Which is equivalent to:
# SELECT O
# FROM DBGroup.Member, M.Office O
# WHERE EXISTS y in M.Age : y < 30

# And our expected output is:
# Office "Gates 252"
# Office
#   Building "CIS"
#   Building "411"

# For the "without indexing" case, we are implementing the query plan
# given in our notes as Figure 3, modified to remove the superfluous
# Aggregate operation.

from operators import SELECT, SCAN, JOIN, PROJECT
from utilities import loadOEM, set_to_string

OEM = dict()
OA = dict()


def query_plan():
	global OA, OEM
	scan1 = SCAN(OA, OEM, "root", "DBGroup", "oa0")
	scan2 = SCAN(OA, OEM, "oa0", "Member", "oa1")
	scan3 = SCAN(OA, OEM, "oa1", "Office", "oa2")
	scan4 = SCAN(OA, OEM, "oa1", "Age", "oa3")
	join1 = JOIN(OA, OEM, scan1, scan2)
	join2 = JOIN(OA, OEM, join1, scan3)
	select1 = SELECT(OA, OEM, scan4, "oa3", lambda x: x > 30)
	join3 = JOIN(OA, OEM, join2, select1)
	project1 = PROJECT(OA, OEM, join3, "oa2") # FIXME
	return [x for x in join3.get_iterator()]


def main():
	global OEM
	OEM = loadOEM("OEM.txt")
	result = query_plan()
	print set_to_string(result, OEM)


if __name__ == '__main__':
   main()
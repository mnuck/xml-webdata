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

# Significant guidance gained from
# http://infolab.stanford.edu/lore/pubs/lore97.pdf.

from operators import SELECT, SCAN, JOIN, PROJECT
from operators import VINDEX, LINDEX, ONCE, NAMED_OBJ
from utilities import loadOEM, set_to_string
from utilities import construct_lindex, construct_vindex

OEM = dict()


# For the "without indexing" case, we are implementing the query plan
# given in our notes as Figure 3, modified to remove the superfluous
# Aggregate operation.
def query_plan():
    OA = dict()
    predicate = lambda x: x > 30
    scan1 = SCAN("root", "DBGroup", "oa0", OA, OEM, "scan1")
    scan2 = SCAN("oa0", "Member", "oa1", OA, OEM, "scan2")
    scan3 = SCAN("oa1", "Office", "oa2", OA, OEM, "scan3")
    scan4 = SCAN("oa1", "Age", "oa3", OA, OEM, "scan4")
    join1 = JOIN(scan1, scan2, OA, OEM, "join1")
    join2 = JOIN(join1, scan3, OA, OEM, "join2")
    select1 = SELECT(scan4, "oa3", predicate, OA, OEM, "select1")
    join3 = JOIN(join2, select1, OA, OEM, "join3")
    project1 = PROJECT(join3, "oa2", OA, OEM, "project1")
    return [x for x in project1]


# For the "with indexing" case, we are implementing the query plan given
# in our names as Figure 6.
def query_plan_indexed():
    OA = dict()
    l_index = construct_lindex(OEM, ["Age", "Member"])
    v_index = construct_vindex(OEM, l_index, ["Age"])
    operator1 = lambda x, y: x > y
    vindex1 = VINDEX("Age", operator1, 30, "oa2", v_index, OA, OEM, "vindex1")
    lindex1 = LINDEX("oa2", "Age", "oa1", l_index, OA, OEM, "lindex1")
    lindex2 = LINDEX("oa1", "Member", "oa0", l_index, OA, OEM, "lindex2")
    scan1 = SCAN("oa1", "Office", "oa3", OA, OEM, "scan1")
    once1 = ONCE(lindex1, OA, OEM, "once1")
    named_obj1 = NAMED_OBJ(lindex2, "DBGroup", "oa0", OA, OEM, "named_obj1")
    join1 = JOIN(once1, named_obj1, OA, OEM, "join1")
    join2 = JOIN(vindex1, join1, OA, OEM, "join2")
    join3 = JOIN(join2, scan1, OA, OEM, "join3")
    project1 = PROJECT(join3, "oa3", OA, OEM, "project1")
    return [x for x in project1]


def main():
    global OEM
    OEM = loadOEM("OEM.txt")

    print "STATE OUTPUT DURING RUN OF NON-INDEX QUERY"
    result1 = query_plan()

    print "\nSTATE OUTPUT DURING RUN OF INDEXED QUERY"
    result2 = query_plan_indexed()

    print "\nNON-INDEXED QUERY OUTPUT:"
    print set_to_string(result1, OEM)

    print "\nINDEXED QUERY OUTPUT:"
    print set_to_string(result2, OEM)


if __name__ == '__main__':
    main()

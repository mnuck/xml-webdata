#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3


# common superclass to contain info used by all operators
class OPERATOR(object):
    def __init__(self, OA, OEM, name):
        self.OA, self.OEM, self.name = OA, OEM, name


# Iterate through the oids of the oid stored in start
# reachable via path. Store each reachable oid in OA[target],
# and yield it up to the caller.
class SCAN(OPERATOR):
    def __init__(self, start, path, target, *args):
        self.start, self.path, self.target = start, path, target
        super(SCAN, self).__init__(*args)

    def __iter__(self):
        targets = [self.OEM[self.start]] \
            if self.start == "root" \
            else self.OEM[self.OA[self.start]][2]
        for oid in targets:
            if self.OEM[oid][0] == self.path:
                self.OA[self.target] = oid
                print self.name, self.OA[self.target], self.OA
                yield self.OA[self.target]


# For each result yielded by left_child_op,
# yield all results yielded by right_child_op.
class JOIN(OPERATOR):
    def __init__(self, left_child_op, right_child_op, *args):
        self.left, self.right = left_child_op, right_child_op
        super(JOIN, self).__init__(*args)

    def __iter__(self):
        for a in self.left:
            for b in self.right:
                print self.name, b, self.OA
                yield b


# For each result yielded by child_op,
# if predicate returns true
# when passed the value of the oid currently in OA[input_oa],
# then yield the result yielded by the child_op
class SELECT(OPERATOR):
    def __init__(self, child_op, input_oa, predicate, *args):
        self.child, self.input, self.predicate = child_op, input_oa, predicate
        super(SELECT, self).__init__(*args)

    def __iter__(self):
        for oid in self.child:
            key = self.OA[self.input]
            if self.predicate(self.OEM[key][2]):
                print self.name, oid, self.OA
                yield oid


# For each result yielded by child_op,
# yield the oid in OA[input_oa]
class PROJECT(OPERATOR):
    def __init__(self, child_op, input_oa, *args):
        self.child, self.input = child_op, input_oa
        super(PROJECT, self).__init__(*args)

    def __iter__(self):
        for oid in self.child:
            print self.name, oid, self.OA
            yield self.OA[self.input]


# For each result yielded by child_op,
# yield that result exactly once
class ONCE(OPERATOR):
    def __init__(self, child_op, *args):
        self.child = child_op
        super(ONCE, self).__init__(*args)

    def __iter__(self):
        seen = set()
        for oid in self.child:
            if oid not in seen:
                seen.add(oid)
                print self.name, oid, self.OA
                yield oid


# For each result yielded by child_op,
# If the label of the oid currently in OA[input_oa] equals label,
# then yield the result yielded by child_op.
class NAMED_OBJ(OPERATOR):
    def __init__(self, child_op, label, input_oa, *args):
        self.child, self.label, self.input = child_op, label, input_oa
        super(NAMED_OBJ, self).__init__(*args)

    def __iter__(self):
        for oid in self.child:
            key = self.OA[self.input]
            if self.label == self.OEM[key][0]:
                print self.name, oid, self.OA
                yield oid


# Given the oid currently in OA[start] and a label,
# yield all parent oids that can reach the oid currently in OA[start]
# by an edge with that label.
class LINDEX(OPERATOR):
    def __init__(self, start, label, target, lindex, *args):
        self.start, self.target = start, target
        self.label, self.lindex = label, lindex
        super(LINDEX, self).__init__(*args)

    def __iter__(self):
        key = (self.OA[self.start], self.label)
        for oid in self.lindex[key]:
            self.OA[self.target] = oid
            print self.name, oid, self.OA
            yield oid


# Given a label, operator, and value,
# yield all atomic oids reachable via an edge with that label, for which
# the provided operator returns true when the value associated with that
# oid is the first parameter and the value passed in is the second parameter.
class VINDEX(OPERATOR):
    def __init__(self, label, operator, value, target, vindex, *args):
        self.label, self.operator, self.value = label, operator, value
        self.target, self.vindex = target, vindex
        super(VINDEX, self).__init__(*args)

    def __iter__(self):
        for oid in self.vindex.match(self.label, self.operator, self.value):
            self.OA[self.target] = oid
            print self.name, oid, self.OA
            yield oid

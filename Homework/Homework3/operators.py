#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3

# Immediately prior to yielding a result,
# each operator prints its name,
#                      what it is yielding,
#                      and the current state of OA.

class OPERATOR(object):
	def __init__(self, OA, OEM, name):
		self.OA, self.OEM, self.name = OA, OEM, name


class SCAN(OPERATOR):
	def __init__(self, start, path, target, *args):
		self.start, self.path, self.target = start, path, target
		super(SCAN, self).__init__(*args)

	def __iter__(self):
		targets = [self.OEM[self.start]]  \
				  if self.start == "root" \
				  else self.OEM[self.OA[self.start]][2]
		for oid in targets:
			if self.OEM[oid][0] == self.path:
				self.OA[self.target] = oid
				print self.name, self.OA[self.target], self.OA
				yield self.OA[self.target]


class JOIN(OPERATOR):
	def __init__(self, left_child_op, right_child_op, *args):
		self.left, self.right = left_child_op, right_child_op
		super(JOIN, self).__init__(*args)

	def __iter__(self):
		for a in self.left:
			for b in self.right:
				print self.name, b, self.OA
				yield b


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


class PROJECT(OPERATOR):
	def __init__(self, child_op, input_oa, *args):
		self.child, self.input = child_op, input_oa
		super(PROJECT, self).__init__(*args)

	def __iter__(self):
		for oid in self.child:
			print self.name, oid, self.OA
			yield self.OA[self.input]

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

class SCAN(object):
	def __init__(self, OA, OEM, start, path, target, name):
		self.name = name
		self.OA = OA
		self.OEM = OEM
		self.start = start
		self.path = path
		self.target = target

	def get_iterator(self):
		targets = [self.OEM[self.start]]  \
				  if self.start == "root" \
				  else self.OEM[self.OA[self.start]][2]
		for oid in targets:
			if self.OEM[oid][0] == self.path:
				self.OA[self.target] = oid
				print self.name, self.OA[self.target], self.OA
				yield self.OA[self.target]


class JOIN(object):
	def __init__(self, OA, OEM, left_child_op, right_child_op, name):
		self.name = name
		self.OA = OA
		self.OEM = OEM
		self.left = left_child_op
		self.right = right_child_op

	def get_iterator(self):
		for a in self.left.get_iterator():
			for b in self.right.get_iterator():
				print self.name, b, self.OA
				yield b


class SELECT(object):
	def __init__(self, OA, OEM, child_op, input_oa, predicate, name):
		self.name = name
		self.OA = OA
		self.OEM = OEM
		self.child = child_op
		self.input = input_oa
		self.predicate = predicate

	def get_iterator(self):
		for oid in self.child.get_iterator():
			key = self.OA[self.input]
			if self.predicate(self.OEM[key][2]):
				print self.name, oid, self.OA
				yield oid


class PROJECT(object):
	def __init__(self, OA, OEM, child_op, input_oa, name):
		self.name = name
		self.OA = OA
		self.OEM = OEM
		self.child = child_op
		self.input = input_oa

	def get_iterator(self):
		for oid in self.child.get_iterator():
			print self.name, oid, self.OA
			yield self.OA[self.input]

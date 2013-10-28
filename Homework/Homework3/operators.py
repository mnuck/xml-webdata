#!/usr/bin/env python
#
#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 3

class SCAN(object):
	def __init__(self, OA, OEM, start, path, target):
		self.OA = OA
		self.OEM = OEM
		self.start = start
		self.path = path
		self.target = target

	def get_iterator(self):
		if self.start == "root":
			self.OA[self.target] = self.OEM[self.start]
			yield self.OA[self.target]
		else:
			for oid in self.OEM[self.OA[self.start]][2]:
				if self.OEM[oid][0] == self.path:
					self.OA[self.target] = oid
					yield self.OA[self.target]


class JOIN(object):
	def __init__(self, OA, OEM, left_child_op, right_child_op):
		self.OA = OA
		self.OEM = OEM		
		self.left = left_child_op
		self.right = right_child_op

	def get_iterator(self):
		for a in self.left.get_iterator():
			for b in self.right.get_iterator():
				yield b


class SELECT(object):
	def __init__(self, OA, OEM, child_op, input_oa, predicate):
		self.OA = OA
		self.OEM = OEM
		self.child = child_op
		self.input = input_oa
		self.predicate = predicate

	def get_iterator(self):
		for tup in self.child.get_iterator():
			key = self.OA[self.input]
			if self.predicate(self.OEM[key][2]):
				yield tup


class PROJECT(object):  # FIXME
	def __init__(self, OA, OEM, child_op, input_oa):
		self.OA = OA
		self.OEM = OEM
		self.child = child_op
		self.input = input_oa

	def get_iterator(self):
		for tup in self.child.get_iterator():
			key = self.OA[self.input]
			if self.OEM[key] == tup:
				yield tup
#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib import *

class ConsoleWriter(object):
	"""
	This class ...
	"""
	def __init__(self):
		super(ConsoleWriter, self).__init__()
		self.DatabaseClient = DatabaseClient()
		self.data = self.DatabaseClient.read_local_data()

	def begin_query(self):
		print("Please enter a number from 1-5!: ")
		entry = input()
		print("Entry is: ", entry)
		print(self.data)


if __name__ == '__main__':
	Writer = ConsoleWriter()
	Writer.begin_query()
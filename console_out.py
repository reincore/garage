#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib import *

class ConsoleWriter(object):
	"""
	This class ...
	"""
	def __init__(self):
		super(ConsoleWriter, self).__init__()
		self.Presenter = Presenter()

	def begin_query(self):
		print("Please enter a number from 1-4!: ")
		entry = str(raw_input())
		isEntryAccepted = self.Presenter.handle_user_input(entry)

		if not isEntryAccepted:
			self.begin_query()
		else: 
			print ("Currently this is it... Success!")


if __name__ == '__main__':
	Writer = ConsoleWriter()
	Writer.begin_query()
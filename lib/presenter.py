#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.service import *


class Presenter(object):
	"""
	This class contains the methods to get and set garage service data,
	as well as the implementation of the project logic.
	"""
	
	def __init__(self):
		super(Presenter, self).__init__()
		self.accepted_user_entries = ['1', '2', '3', '4', '?']
		

	# Getter methods
	def get_garage_service(self):
		pass

	def get_board_service(self):
		pass

	# Setter methods
	def set_garage_service(self, data):
		pass

	def set_board_service(self, data):
		pass

	# Logic
	def car_enters(self, car_data):
		pass

	def car_exits(self, car_data):
		pass

	# User input handling
	def handle_user_input(self, entry):
		if entry in self.accepted_user_entries:
			print("Entry is: {0} and it is of accepted format" ).format(entry)
			return True
		else:
			print("Entry is: {0} and it is NOT of accepted format" ).format(entry)
			return False
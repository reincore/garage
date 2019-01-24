#!/usr/bin/python
#-*- encoding: utf-8 -*-

import json


class DatabaseClient(object):
	"""
	This class contains the methods to read data from database 
	(currently a local .txt file). 
	"""
	
	def __init__(self):
		super(DatabaseClient, self).__init__()
		

	def get_garage_data(self, input_file_name="garage.txt"):
		"""
		This method reads and returns the garage.txt file data. Supposedly, there 
		are three garage entries, each having a name, capacity and availability value.
		"""

		file_path = "data/" + str(input_file_name)
		try:
			with open(file_path) as file_name:
				file_data = json.load(file_name)
		except ValueError as e:
			raise Exception("The file '{0}' could not be read! Please check its file extension and file content.")

		if file_data:
			return file_data
		else:
			return ""

	def write_local_data(self, output_file_name):
		pass

	def get_board_data(self, input_file_name="garage.txt"):
		"""
		This method reads and returns the garage.txt file data. Supposedly, there 
		are three garage entries, each having a name, capacity and availability value.
		"""

		file_path = "data/" + str(input_file_name)
		try:
			with open(file_path) as file_name:
				file_data = json.load(file_name)
		except ValueError as e:
			raise Exception("The file '{0}' could not be read! Please check its file extension and file content.")

		if file_data:
			return file_data
		else:
			return ""



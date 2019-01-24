#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.file_client import *


class Repository(object):
	"""
	This class contains the methods to 
	"""
	
	def __init__(self):
		super(Repository, self).__init__()
		self.garage_repo = None
		self.board_repo = None

		self.file_client = DatabaseClient()

	# Getter & Setter methods
	def get_garage_repo(self):
		pass

	def get_board_repo(self):
		return self.file_client.get_board_data()

	def set_garage_repo(self, garage_data):
		pass

	def set_board_repo(self, board_data):
		pass

	# Repository methods
	def get_garage_data(self):
		garage_data = self.file_client.get_garage_data()
		if garage_data:
			return garage_data
		else:
			print("File empty!")
			return None

	def set_file_client_data(self, data):
		pass

#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.repository import *


class Service(object):
	"""
	This class contains the getter and setter methods for Board repo and Garage repo.
	"""
	
	def __init__(self):
		super(Service, self).__init__()
		self.garage_service = None
		self.board_service = None

		self.repository = Repository()

	# Getter & Setter methods
	def get_garage_service(self):
		pass

	def set_garage_service(self, garage_service_data):
		pass

	def get_board_service(self):
		return self.repository.get_board_repo()

	def set_board_service(self, board_service_data):
		pass

	# Service methods
	def get_garage_repo(self):
		garage_file_data = self.repository.get_garage_data()
		if garage_file_data:
			return garage_file_data
		else:
			return None
			
	def set_garage_repo(self, garage_repo_data):
		pass

	def get_board_repo(self):
		pass

	def set_board_repo(self, board_repo_data):
		pass


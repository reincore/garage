#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.repository import *


class Service(object):
	"""
	This class contains the methods to get and set Board 
	"""
	
	def __init__(self):
		super(Service, self).__init__()
		self.garage_service = None
		self.board_service = None

	# Getter methods
	def get_garage_service(self):
		pass

	def get_board_service(self):
		pass

	def get_garage_repo(self):
		pass

	def get_board_repo(self):
		pass

	# Setter methods
	def set_garage_service(self, garage_service_data):
		pass

	def set_board_service(self, board_service_data):
		pass

	def set_garage_repo(self, garage_repo_data):
		pass

	def set_board_repo(self, board_repo_data):
		pass
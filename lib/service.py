#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.repository import *
from lib.entity import *


class Service(object):
	"""
	This class contains the getter and setter methods for Board repo and Garage repo.
	"""
	
	def __init__(self):
		super(Service, self).__init__()
		self.garage_service = None
		self.board_service = None
		
		self.entity = Entity()
		self.repository = Repository()

	# Getter & Setter methods

	def get_board_service(self):
		return self.repository.get_board_repo()


	# Service methods
	def get_garage_repo(self):
		garage_file_data, self.entity.garage = self.repository.get_garage_data()
		if garage_file_data:
			return garage_file_data, self.entity
		else:
			return None
			
	def set_garage_repo(self, garage_repo_data):
		self.repository.set_garage_repo(garage_repo_data)

	def add_vehicle(self, new_vehicle_data):
		self.entity.vehicle = self.repository.add_vehicle(new_vehicle_data)
		return self.entity.vehicle


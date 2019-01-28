#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.file_client import *
from lib.entity import *


class Repository(object):
	"""
	This class contains the methods to 
	"""
	
	def __init__(self):
		super(Repository, self).__init__()
		self.garage_repo = None
		self.board_repo = None

		self.file_client = DatabaseClient()
		self.entity = Entity()

	# Getter & Setter methods

	def get_board_repo(self):
		return self.file_client.get_board_data()

	def set_garage_repo(self, garage_data):
		self.file_client.set_garage_data(garage_data)

	# Repository methods
	def get_garage_data(self):
		garage_data = self.file_client.get_garage_data()
		self.entity.garage = garage_data
		if garage_data:
			return garage_data, self.entity
		else:
			print("File empty!")
			return None

	def add_vehicle(self, new_vehicle_data):
		""" Add vehicle to the vehicle list """
		self.entity.vehicle = self.entity.add_vehicle(new_vehicle_data)
		return self.entity.vehicle

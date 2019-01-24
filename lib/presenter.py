#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.service import *
from lib.console_out import *
from lib.entity import *
import sys

class Presenter(object):
	"""
	This class contains the methods to get and set garage service data,
	as well as the implementation of the project logic.
	"""
	
	def __init__(self):
		super(Presenter, self).__init__()
		self.service = Service()	
		self.entity = Entity()

	# Getter & Setter methods
	def get_garage_service(self):
		garage_file_data = self.service.get_garage_repo()
		if garage_file_data:
			return garage_file_data
		else:
			return None

	def get_board_content(self):
		return self.service.get_board_service()

	def set_garage_service(self, data):
		pass

	def set_board_service(self, data):
		 # self.service.set_board_service(data)
		 pass

	# Logic
	def add_new_car(self, new_vehicle_data):
		self.entity.add_vehicle(new_vehicle_data)

	def remove_car(self, license_plate):
		pass

	def navigate_new_car(self, new_vehicle):
		# This should be changed to entity
		board_content = self.get_board_content()
		target_garage = ""

		for garage in board_content:
			if int(garage['availability']) > 0:
				target_garage = garage['name']
				break
			else:
				target_garage = None

		return target_garage

	def handle_new_car(self, license_plate, brand, model, year, color):
		new_vehicle = {
		"id": license_plate, 
		"brand": brand, 
		"model": model, 
		"year": year, 
		"color": color
		}

		# Check the board display
		# empty_slot = self.check_board()

		# Add new car to the car list
		self.add_new_car(new_vehicle)

		# Place new car in the nearest available garage slot
		parked_garage = self.navigate_new_car(new_vehicle)
		return parked_garage
		

	

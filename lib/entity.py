#!/usr/bin/python
#-*- encoding: utf-8 -*-

class Entity(object):
	"""
	This class contains two lists, namely garage and vehicle as fields.
	There are also getter and setter methods of this class for each field.
	"""
	def __init__(self):
		super(Entity, self).__init__()
		self.garage = []
		self.vehicle = []
		self.board = []

	def get_garage(self):
		return self.garage

	def add_garage(self, new_garage):
		self.garage.append(new_garage)
		print("{0} appended to the end of Garage list!".format(new_garage))

	def get_vehicle(self, license_plate):
		# Entered license plate is matched with a car from the car list and is returned

		for car in self.vehicle:
			if license_plate in car:
				return car

	def add_vehicle(self, new_vehicle_data):
		# Received parameter is a dictionary that contains the:
		# license_plate, brand, model, year and color

		self.vehicle.append(new_vehicle_data)

	def get_board_data(self):
		return self.board

	def set_board_data(self):
		pass

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

	def get_garage(self):
		return self.garage

	def set_garage(self, new_garage):
		self.garage.append(new_garage)
		print("{0} appended to the end of Garage list!".format(new_garage))

	def get_vehicle(self):	
		return self.vehicle

	def set_vehicle(self, new_vehicle):
		self.vehicle.append(new_vehicle)
		print("{0} appended to the end of Vehicle list!".format(new_vehicle))

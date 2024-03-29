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
		garage_file_data, self.entity = self.service.get_garage_repo()
		if garage_file_data:
			return garage_file_data, self.entity.garage
		else:
			return None

	def get_board_content(self):
		board_data = self.service.get_board_service()
		return board_data

	def set_garage_service(self, data):
		pass

	def set_board_service(self, data):
		# self.service.set_board_service(data)
		pass

	# Logic
	def add_new_car(self, new_vehicle_data):
		self.entity.vehicle = self.service.add_vehicle(new_vehicle_data)
		return self.entity.vehicle

	def remove_car(self, license_plate):
		pass

	def navigate_new_car(self, new_vehicle):
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

		# Check license plate validity
		is_license_plate_valid = self.validate_license_plate(license_plate)
		if not is_license_plate_valid:
			return False, None

		# Add new car to the car list
		vehicle_list = self.add_new_car(new_vehicle)
		print("Vehicle list is: ")
		print(vehicle_list)
		print("Garage list is: ")
		print(self.entity.garage)

		# Place new car in the nearest available garage slot
		parked_garage = self.navigate_new_car(new_vehicle)
		return True, parked_garage

	def validate_license_plate(self, license_plate):
		ALPHABET = "abcdefghijklmnoprstuvyzABCDEFGHIJKLMNOPRSTUVYZ"
		NUMBERS = "0123456789"

		try:
			city_code = int(license_plate[:2])
			is_length_valid = (6 < len(license_plate) < 10)

			# City code is between 0 and 81 and first two characters are not alphabetical
			is_beginning_valid = ((0 < city_code < 81)
				and not (any(c.isalpha() for c in license_plate[0:2])))

			# Middle characters (index 3 and 4) are alphabetical
			is_middle_chars_valid = (all(c.isalpha() for c in license_plate[2:4])
				and (license_plate[2] and license_plate[5] not in ALPHABET))

			# Last 3 characters are numerical and -5th character is not numerical
			is_ending_valid = (all(c in NUMBERS for c in license_plate[-3:])) and not (license_plate[-5] in NUMBERS) and (int(license_plate[-3:]) > 0)

			if (is_length_valid 
				and is_beginning_valid 
				and is_middle_chars_valid 
				and is_ending_valid):
				is_license_plate_valid = True

			else: 
				is_license_plate_valid = False
				
		except (ValueError, IndexError) as e:
			is_license_plate_valid = False

		if not is_license_plate_valid:
			print("Error: license plate is not correct, you must enter a valid license plate!")		
		return is_license_plate_valid

	

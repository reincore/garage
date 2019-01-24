#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.presenter import *


class ConsoleWriter(object):
	"""
	This class prints instructions on the console window and 
	handles method calls to Presenter class instances.
	"""

	def __init__(self):
		super(ConsoleWriter, self).__init__()
		self.presenter = Presenter()
		self.entity = Entity()
		self.accepted_user_entries = ['1', '2', '3', '4', '?']

	def print_menu(self):
		print("Menu")
		print("1) Press '1' to add a vehicle")
		print("2) Press '2' to remove a vehicle")
		print("3) Press '3' to print board content")
		print("4) Press '4' to quit the application")
		print("5) Press '?' to print this menu again")
		print("\n")

	def begin_query(self):
		print("Choose option: ")
		entry = str(input())
		isEntryAccepted = self.verify_user_input(entry)

		if not isEntryAccepted:
			self.begin_query()
		else: 
			print ("Currently this is it... Success!")


	def verify_user_input(self, entry):
		if entry in self.accepted_user_entries:
			print(f"Entry is: {entry} and it is of accepted format" )
			self.handle_user_input(entry)

		else:
			print(f"Entry is: {entry} and it is NOT of accepted format" )
			return False

	def print_board_content(self):
		board_content = self.presenter.get_board_content()

		print("Board " 
			+ str(board_content[0]['name']) + ": " + str(board_content[0]['availability']) + ", " 
			+ str(board_content[1]['name']) + ": " + str(board_content[1]['availability']) + ", " 
			+ str(board_content[2]['name']) + ": " + str(board_content[2]['availability'])
			)


	def handle_user_input(self, entry):
		if entry == "1":
			# Add a vehicle to garage (and garage.txt)
			print("Pressed option is '1'.")
			print("License plate:")
			license_plate = str(input())
			print("Brand:")
			brand = str(input())
			print("Model:")
			model = str(input())
			print("Year:")
			year = str(input())
			print("Color:")
			color = str(input())

			# Add new car to the car list
			parked_garage = self.presenter.handle_new_car(license_plate, brand, model, year, color)
			
			### Make a call to Presenter to obtain board data ###

			print(f"Location of {brand} {model} {license_plate} is {parked_garage}.")

			self.print_board_content()
		
		elif entry == "2":
			# Remove a vehicle from a garage (and from garage.txt)
			print("Pressed option is '2'.")
			print("Enter a license plate:")
			license_plate = str(input())

			### Remove car with license_plate data ###

			### Make a call to Presenter to obtain board data ###
			self.print_board_content()

		elif entry == "3":
			# Print current board content

			### Make a call to Presenter to obtain board data ###
			self.print_board_content()
			

		elif entry == "4":
			# Quit the application
			print("Terminating program...")
			sys.exit(0)

		elif entry == "?":
			# Print the menu on console
			self.print_menu()
			
		else: 
			raise Exception("User input is accepted but is erroneous! Terminating... ")


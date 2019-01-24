#!/usr/bin/python
#-*- encoding: utf-8 -*-

from lib.console_out import *


class ConsoleApp(object):
	"""
	Initializer class to start the console app
	"""

	def __init__(self):
		super(ConsoleApp, self).__init__()
		self.console_writer = ConsoleWriter()

	def start(self):
		self.console_writer.print_menu()
		self.console_writer.begin_query()


if __name__ == '__main__':
	App = ConsoleApp()
	App.start()
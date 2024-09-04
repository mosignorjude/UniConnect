#!/usr/bin/python3

"""
Unit Test for BaseModel Class
"""

import os

import console
import unittest
from unittest.mock import patch
from io import StringIO
import models
import inspect
from models import storage
from models.engine.file_storage import FileStorage

UniConnectCommand = console.UniConnectCommand
classes = storage.models

class TestUniConnectCommandDocs(unittest.TestCase):
	""" Class for testing console documentation """

	def setUp(self):
		""" Sets up test cases. """
		file = 'file.json'
		if (os.path.exists(file)):
			os.remove(file)
		self.resetStorage()

	def resetStorage(self):
		FileStorage._FileStorage__objects = {}
		if os.path.isfile(FileStorage._FileStorage__file_path):
			os.remove(FileStorage._FileStorage__file_path)

	@classmethod
	def setUpClass(cls):
		"""init: prints output to mark new tests"""
		cls.all_funcs = inspect.getmembers(console.UniConnectCommand,
        									inspect.isfunction)

	def test_create(self):
		"""Tests create for all classes."""
		for classname in classes:
			self.help_test_do_create(classname)

	def help_test_redirect_output(self, command):
		""" Helpwer method to get redirected output """
		with patch('sys.stdout', new=StringIO()) as f:
			UniConnectCommand().onecmd(command)
		return f.getvalue()[:-1]

	def help_test_do_create(self, classname):
		"""Helper method to test the create command."""
		uid = self.help_test_redirect_output("create {}".format(classname))
		self.assertTrue(len(uid) > 0)
		key = "{}.{}".format(classname, uid)
		result = self.help_test_redirect_output("all {}".format(classname))
		self.assertTrue(uid in result)

	def test_do_create_invalid_class(self):
		""" Test for none existing classes """
		result = self.help_test_redirect_output('create garbaage')
		self.assertTrue(len(result) > 0)
		self.assertEqual(result, "** class doesn't exist **")

	def test_do_create_to_many_args(self):
		""" Test for many args """
		result = self.help_test_redirect_output('create BaseModel somthing else')
		self.assertTrue(len(result) > 0)
		self.assertEqual(result, "** Too many argument for create **")

	def test_do_create_no_arg(self):
		""" Test for no args """
		result = self.help_test_redirect_output('create')
		self.assertTrue(len(result) > 0)
		self.assertEqual(result, "** class name missing **")

	def test_do_show(self):
		""" Test show command """
		result = self.help_test_redirect_output('create BaseModel')
		result2 = self.help_test_redirect_output('show BaseModel {}'.format(result))
		self.assertTrue(len(result) > 0)
		self.assertTrue(len(result2) > 0)
		self.assertEqual(result2.split()[1][1:-1], result)
		self.resetStorage()

	def test_do_show_missing_class(self):
		result = self.help_test_redirect_output('show')
		self.assertTrue(len(result) > 0)
		self.assertEqual(result, "** class name missing **")


if __name__ == '__main__':
	unittest.main()
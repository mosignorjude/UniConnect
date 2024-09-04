#!/usr/bin/python3

""" Test for BaseModel Class """


import unittest
import uuid
import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	""" Test class for BaseModel """

	def test_new_instance(self):
		base = BaseModel()
		self.assertTrue(isinstance(base.id, str))
		self.assertTrue(isinstance(base.created_at, type(datetime.datetime.now())))
		self.assertTrue(isinstance(base.updated_at, type(datetime.datetime.now())))

		self.assertEqual(base.created_at, base.updated_at)

	def test_copy_instance(self):
		base = BaseModel()
		new_base = BaseModel(**base.to_dict())
		self.assertEqual(base.id, new_base.id)
		self.assertEqual(base.created_at, new_base.created_at)
		self.assertEqual(base.updated_at, new_base.updated_at)
		self.assertDictEqual(base.to_dict(), new_base.to_dict())

	def test_create_instance_with_id(self):
		""" Test BaseModel when created with only id kwarg """
		base = BaseModel(id=10)
		self.assertTrue(isinstance(base.id, str))
		self.assertTrue(isinstance(base.created_at, type(datetime.datetime.now())))
		self.assertTrue(isinstance(base.updated_at, type(datetime.datetime.now())))

	def test_create_instance_with_created_at(self):
		""" Test BaseModel when created with only created_at kwarg """
		base = BaseModel(created_at=datetime.datetime.now().isoformat())
		self.assertTrue(isinstance(base.id, str))
		self.assertTrue(isinstance(base.created_at, type(datetime.datetime.now())))
		self.assertTrue(isinstance(base.updated_at, type(datetime.datetime.now())))

		self.assertEqual(base.created_at, base.updated_at)

	def test_create_instance_with_updated_at(self):
		""" Test BaseModel when created with only created_at kwarg """
		base = BaseModel(updated_at=datetime.datetime.now().isoformat())
		self.assertTrue(isinstance(base.id, str))
		self.assertTrue(isinstance(base.created_at, type(datetime.datetime.now())))
		self.assertTrue(isinstance(base.updated_at, type(datetime.datetime.now())))

		self.assertEqual(base.created_at, base.updated_at)

	def test_str(self):
		model = BaseModel(id="1234")
		expected_str = f"[BaseModel] (1234) {model.__dict__}"
		self.assertEqual(str(model), expected_str)

	# def test_error(self):
	# 	""" Test BaseModel to raise error for invalid types """
	# 	self.assertRaises(TypeError, BaseModel(), id=[3], msg='id must be a string')

	def test_save(self):
		base = BaseModel()
		old_updated_at = base.updated_at
		base.save()
		self.assertNotEqual(base.updated_at, old_updated_at)
		base_value = 'BaseModel.'+base.id
		self.assertIn(base_value, storage.all())

	def test_to_dict(self):
		base = BaseModel()
		base_dict = base.to_dict()
		self.assertEqual(base_dict['id'], base.id)
		self.assertEqual(base_dict['__class__'], "BaseModel")
		self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
		self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())

	def test_from_dict(self):
		obj_dict = {
			"id": "1234", 
			"created_at": "2023-09-03T12:00:00",
			"updated_at": "2023-09-03T12:00:00"
		}
		model = BaseModel.from_dict(obj_dict)
		self.assertEqual(model.id, "1234")
		self.assertEqual(model.created_at, datetime.datetime.fromisoformat("2023-09-03T12:00:00"))
		self.assertEqual(model.updated_at, datetime.datetime.fromisoformat("2023-09-03T12:00:00"))

if __name__ == '__main__':
	unittest.main()


import unittest
from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes.CIField import CIField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError


class Test_CIField(unittest.TestCase):
	
	def setUp(self):
		self.CiField=(Factory.get_class('CIField'))()

	def test_check_id_1(self):
		try:
			self.CiField.check_id('46406953')
			self.assertEqual
		except ValidationError:
			self.assertEqual(1,0)

	def test_check_id_2(self):
		try:
			self.CiField.check_id('46406955')
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_check_id_2(self):
		try:
			self.CiField.check_id('1234')
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_int_check_1(self):
		self.CiField.int_check(1)
		self.assertEqual

	def test_int_check_2(self):
		try:
			self.CiField.int_check('a')
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_get_methods(self):
		l=self.CiField.get_methods()
		self.assertEqual(len(l),3)

	def test_tostring(self):
		self.assertEqual(self.CiField.__str__(),"Cedula")

import unittest
from dynamicForms.fieldtypes import Field
from dynamicForms.fields import Validations
from dynamicForms.fields import Field_Data
from dynamicForms.fields import Validations
from dynamicForms.fieldtypes.TextField import TextField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError


class Test_Number_Field(unittest.TestCase):
	
	def setUp(self):
		self.TextField=(Factory.get_class('TextField'))()

	def test_check_length_1(self):
		try:
			f=Field_Data()
			f.validations.max_len_text=100
			self.TextField.check_length("test_string",field=f)
			self.assertEqual
		except ValidationError:
			self.assertEqual(1,0)

	def test_check_length_2(self):
		try:
			f=Field_Data()
			f.validations.max_len_text=1
			self.TextField.check_length("test_string",field=f)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_get_methods(self):
		f=Field_Data()
		f.validations.max_len_text=1
		l=self.TextField.get_methods(field=f)
		self.assertEqual(len(l),2)

	def test_check_consistency_1(self):
		try:
			f=Field_Data()
			f.validations.max_len_text=1
			self.TextField.check_consistency(f)
			self.assertEqual
		except ValidationError:
			self.assertEqual(0,1)

	def test_check_consistency_2(self):
		try:
			f=Field_Data()
			f.validations.max_len_text=-1
			self.TextField.check_consistency(f)
			self.assertEqual(0,1)
		except ValidationError:
			self.assertEqual

	def test_tostring(self):
		self.assertEqual(self.TextField.__str__(),"Single Line Text")
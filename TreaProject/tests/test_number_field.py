import unittest
from dynamicForms.fieldtypes import Field
from dynamicForms.fields import Validations
from dynamicForms.fields import Field_Data
from dynamicForms.fieldtypes.NumberField import NumberField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError

class Test_Number_Field(unittest.TestCase):

	def setUp(self):
		self.NumberField=(Factory.get_class('NumberField'))()

	def test_cheq_min_1(self):
		f=Field_Data()
		f.validations.min_number=2
		self.NumberField.check_min(10,field=f)
		self.assertEqual
	
	def test_cheq_min_2(self):
		try:
			f=Field_Data()
			f.validations.min_number=20
			self.NumberField.check_min(10,field=f)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_cheq_max_1(self):
		f=Field_Data()
		f.validations.max_number=21
		self.NumberField.check_max(10,field=f)
		self.assertEqual

	def test_cheq_max_2(self):
		try:
			f=Field_Data()
			f.validations.max_number=10
			self.NumberField.check_max(20,field=f)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual
	
	def test_int_check(self):
		try:
			self.NumberField.int_check(1)
			self.assertEqual
		except ValidationError:
			self.assertEqual(1,0)

	def test_int_check(self):
		try:
			self.NumberField.int_check('a')
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_get_methods(self):
		f=Field_Data()
		f.validations.max_number=20
		f.validations.min_number=1
		l=self.NumberField.get_methods(field=f)
		self.assertEqual(len(l),4)

	def test_check_consistency_1(self):
		try:
			f=Field_Data()
			f.validations.max_number=20
			f.validations.min_number=1
			self.NumberField.check_consistency(f)
			self.assertEqual
		except ValidationError:
			self.assertEqual(1,0)


	def test_check_consistency_2(self):
		try:
			f=Field_Data()
			f.validations.max_number=20
			f.validations.min_number=50
			self.NumberField.check_consistency(f)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual
	
	def test_tostring(self):
		self.assertEqual(self.NumberField.__str__(),"NumberField")
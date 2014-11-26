import unittest
from dynamicForms.fieldtypes.CheckboxField import CheckboxField 
from dynamicForms.fields import Field_Data
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError

class Test_CheckBoxField(unittest.TestCase):
	
	def setUp(self):
		self.CBField=(Factory.get_class('CheckboxField'))()


	def test_belong_check_1(self):
		f=Field_Data()
		f.max_id=8
		self.CBField.belong_check("2",field=f,options=[{"id":2}])
		self.assertEqual

	def test_belong_check_2(self):
		try:
			f=Field_Data()
			f.max_id=8
			self.CBField.belong_check("10",field=f,options=[{"id":2}])
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_belong_check_3(self):
		f=Field_Data()
		f.max_id=8
		self.CBField.belong_check("2#3",field=f,options=[{"id":2},{"id":3}])
		self.assertEqual

	def test_tostring(self):
		self.assertEqual(self.CBField.__str__(),"Checkbox")
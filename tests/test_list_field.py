import unittest
from dynamicForms.fieldtypes.ListField import ListField
from dynamicForms.fields import  Option
from dynamicForms.fields import Field_Data
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError

class NewFieldList(ListField):
    """
    newField List
    """
    template_name = "test_template_name"
    edit_template_name = "test_edit_template_name"
    prp_template_name = "test_prp_template_name"

class Test_List_Field(unittest.TestCase):
 	
	@classmethod
	def setUpClass(cls):
		"""
		Register the new fieldtypes
		"""
		Factory.register('NewFieldList', NewFieldList)
	
	def setUp(self):
		self.ListField=(Factory.get_class('NewFieldList'))()

	
	def test_belong_check_1(self):
		f=Field_Data()
		f.max_id=5
		o={'id':1}
		self.ListField.belong_check(1,field=f,options=[o])
		self.assertEqual

	def test_belong_check_2(self):
		try:
			f=Field_Data()
			f.max_id=5
			o={'id':1}
			self.ListField.belong_check(8,field=f,options=[o])
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_check_consistency(self):
		try:
			f=Field_Data()
			f.option=[]
			self.ListField.check_consistency(f)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_get_options_labels(self):
		f={"options":['a','b']}
		l=self.ListField.get_option_labels(f)
		self.assertEqual(l,['a','b'])

	def test_get_options(self):
		d={"pages": [{ "fields": [{"field_id": 1,"max_id":8,"options":8}]}]}
		r=self.ListField.get_options(d,1)
		self.assertEqual(r,8)

	def test_get_methods(self):
		l=self.ListField.get_methods()
		self.assertEqual(len(l),2)

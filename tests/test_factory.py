import unittest
from dynamicForms.fieldtypes.CIField import CIField as CIField
from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError


class NewField2(Field.Field):
    """
    newField Type
    """
    template_name = "test_template_name"
    edit_template_name = "test_edit_template_name"
    prp_template_name = "test_prp_template_name"


class Test_Field(unittest.TestCase):

	#test FieldFactory.py
	def test_factory_register_new_type(self):
		#register a new field type
		try:
			Factory.register('NewField2', NewField2)
			self.assertEqual(0,0)
		except:
			self.assertEqual(1,0)

	def test_factory_register_old_type(self):
		#register a type that exist in factory
		try:
			Factory.register('CIField', CIField)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual(0,0)

	def test_factory_get_class(self):
		field = (Factory.get_class('CIField'))()
		b=type(field) is CIField
		self.assertEqual(b,True)

	def test_factory_get_string(self):
		l=Factory.get_strings()
		self.assertEqual(l['CIField'],"Cedula")

	




import unittest
from dynamicForms.fieldtypes import ModelField
from dynamicForms.models import FieldEntry
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError


class FieldEntryField(ModelField.ModelField):
    prp_template_name = "club/properties.html"
    model = FieldEntry
    name =  "FieldEntryField"
    
    def get_assets():
        return ['formularios/js/fields/FieldEntryField.js']
    
    def __str__(self):
        return "FieldEntryField"

class Test_ModelField(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		Register the new fieldtypes
		"""
		Factory.register('Fentry', FieldEntryField)

	def test_getMethods(self):
		m=(Factory.get_class('Fentry'))()
		l=m.get_methods()
		self.assertEqual(len(l),2)
	
	def test_belong_check(self):
		try:
			m=(Factory.get_class('Fentry'))()
			m.belong_check(1)
			self.assertEqual(1,0)
		except:
			self.assertEqual
	
	def test_find_options(self):
		try:
			m=(Factory.get_class('Fentry'))()
			m.find_options()
			self.assertEqual(1,0)
		except:
			self.assertEqual

	def test_get_options(self):
		m=(Factory.get_class('Fentry'))()
		try:
			m.get_options(a, a)
			self.assertEqual(1,0)
		except:
			self.assertEqual
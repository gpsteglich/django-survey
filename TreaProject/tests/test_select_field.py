import unittest
from dynamicForms.fieldtypes.SelectField import SelectField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError

class Test_SelectedField(unittest.TestCase):
	
	def setUp(self): 
		self.SelectField=(Factory.get_class('SelectField'))()

	def test_tostring(self):
		self.assertEqual(self.SelectField.__str__(),"Combo Box")
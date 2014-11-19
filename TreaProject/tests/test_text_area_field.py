import unittest
from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import TextAreaField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory


class Test_Text_Area_Field(unittest.TestCase):

	def setUp(self):
		self.TextField=(Factory.get_class('TextAreaField'))()

	def test_tostring(self):
		self.assertEqual(self.TextField.__str__(),"Multi Line Text")
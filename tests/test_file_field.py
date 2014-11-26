import unittest
from dynamicForms.fieldtypes.FileField import FileField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory



class Test_File_Field(unittest.TestCase):

	def setUp(self):
		self.FileField=(Factory.get_class('FileField'))()

	def test_tostring(self):
		self.assertEqual(self.FileField.__str__(),"FileField")
import unittest
from dynamicForms.fieldtypes.EmailField import EmailField
from dynamicForms.fields import Field_Data
from dynamicForms.fields import Validations
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError

class Test_CheckBoxField(unittest.TestCase):
	
	def setUp(self):
		self.EmailField=(Factory.get_class('EmailField'))()

	def test_mail_check_1(self):
		self.EmailField.mail_check('usuariomail@company.com')
		self.assertEqual

	def test_mail_check_2(self):
		try:
			self.EmailField.mail_check('usuariomailompany.com')
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual

	def test_get_methods_1(self):
		f=Field_Data()
		l=self.EmailField.get_methods(field=f)
		self.assertEqual(len(l),2)

	def test_get_methods_2(self):
		f=Field_Data()
		v=Validations()
		v.max_len_text=20
		f.validations=v
		l=self.EmailField.get_methods(field=f,)
		self.assertEqual(len(l),3)


	def test_tostring(self):
		self.assertEqual(self.EmailField.__str__(),"Email")
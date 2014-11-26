import unittest
from dynamicForms.fields import *


class Test_fields_file(unittest.TestCase):

	def setUp(self):
		pass

	def test_json_class(self):
		json=JSONField()
		s=json.to_python("")
		self.assertEqual("",s)

	def test_Validations(self):
		v=Validations()
		v.max_len_text = 20
		v.max_number = 30
		v.min_number = 1
		r=v.valid_number()
		self.assertEqual(r,True)
		r2=v.valid_text()
		self.assertEqual(r2,True)
		v2=Validations()
		v2.max_len_text =-1
		v2.max_number = 1
		v2.min_number = 30
		r3=v2.valid_number()
		self.assertEqual(r3,False)
		r4=v2.valid_text()
		self.assertEqual(r4,False)

	def test_Option(self):
		o=Option()
		o.label="lable"
		o.id=2
		self.assertEqual

	def test_Dependencies(self):
		d=Dependencies()
		d.fields=[1,2,3],
		d.pages=[1,2,3]
		self.assertEqual

	def test_Field(self):
		f=Field_Data()
		f.text ='Text'
		f.required ='True'
		f.tooltip = 'Tooltip'
		f.answer = 'Answ'
		f.dependencies = Dependencies()
		f.validations = Validations()
		f.options = []
		f.max_id = 8
		f.field_type ='Type'
		field_id = 8
		self.assertEqual

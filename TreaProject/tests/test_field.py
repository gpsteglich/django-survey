import unittest
from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from dynamicForms.models import Form,Version,FormEntry,FieldEntry
from django.core.exceptions import ValidationError


class NewField(Field.Field):
    """
    newField Type
    """
    template_name ="test_template_name"
    edit_template_name = "test_edit_template_name"
    prp_template_name = "test_prp_template_name"
    sts_template_name="test_statisitics_name"


class Test_Field(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		"""
		Register the new fieldtypes
		"""
		Factory.register('NewField', NewField)
	
	def setUp(self):
		self.field=(Factory.get_class('NewField'))()

	def test_field_validate(self):
		#test generic method validate
		try:
			kw={}
			b=self.field.validate(1,**kw)
			self.assertEqual(0,0)
		except ValidationError:
			self.assertEqual(1,0)
	
	def test_null_check_1(self):
		try:
			self.field.null_check(1)
			self.assertEqual(0,0)
		except ValidationError:
			self.assertEqual(1,0)

	def test_null_check_2(self):
		try:
			self.field.null_check(None)
			self.assertEqual(1,0)
		except ValidationError:
			self.assertEqual(0,0)

	def test_get_methods(self):
		b=self.field.get_methods()
		self.assertEqual(len(b),1)
		self.assertEqual(b[0].__name__,'null_check')

	def test_get_validations(self):
		d={"pages": [{ "fields": [{"field_id": 1,"validations": {"maxnum":1}, }]}]}
		l=self.field.get_validations(d,1)
		self.assertEqual(len(l),1)
		self.assertEqual(l['maxnum'],1)

	def test_get_options(self):
		d={"pages": [{ "fields": [{"field_id": 1,"validations": {"maxnum":1}, }]}]}
		l=self.field.get_options(d,1)
		self.assertEqual(l,None)

	def test_field_checkconsistency(self):
		#test generic method check_consistency
		b=self.field.check_consistency(self.field)
		self.assertEqual(b,None)
	
	"""
	no se si se usa
	def test_count_responses_pct(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user)
       	f1.save()
        v1 = Version.objects.create(json='{"prueba":"valor"}', form=self.f1)
        v1.save()
        self.resp1=FieldEntry.objects.create(field_id=1,)
    """
	def test_get_statistics_1(self):
		f={"field_type":'type1',"text":'text1',"required":False}
		e=self.field.get_statistics([],f)
		self.assertEqual(e['field_type'],'type1')
		self.assertEqual(e['field_text'],'text1')
		self.assertEqual(e['required'],'No')


	def test_get_statistics_2(self):
		f={"field_type":'type1',"text":'text1',"required":True}
		e=self.field.get_statistics([],f)
		self.assertEqual(e['field_type'],'type1')
		self.assertEqual(e['field_text'],'text1')
		self.assertEqual(e['required'],'Yes')


	def test_get_render(self):
		#test get render template
		s=self.field.render()
		self.assertEqual(s,"fields/test_template_name")
	
	def test_get_render_properties(self):
		#test getrender properties template
		s=self.field.render_properties()
		self.assertEqual(s,"fields/test_prp_template_name")

	def test_get_render_edit(self):
		#test getrender properties template
		s=self.field.render_edit()
		self.assertEqual(s,"fields/test_edit_template_name")
	
	def test_get_render_statisitcs(self):
		s=self.field.render_statistic()
		self.assertEqual(s,"fields/test_statisitics_name")

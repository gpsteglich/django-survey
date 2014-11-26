import unittest
from dynamicForms.models import Form,Version,FormEntry,FieldEntry
from django.contrib.auth.models import User
from dynamicForms.fields import PUBLISHED, DRAFT , EXPIRED
import datetime




class Test_Mo(unittest.TestCase):


	def setUp(self):
		#create user
		self.user = User(username='test',email='mail', password='password')
		self.user.save()


	def test_form_1(self):
		try:
			f= Form.objects.create(title = "new form1", owner= self.user , slug='slug')
			f.save()
			self.assertEqual(1,0)
		except:
			self.assertEqual

	def test_form_2(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		f1.save()
		self.assertEqual(f1.__str__(),"new form1")

	def test_form_3(self):
		f2 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		f2.save()
		try:
			f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
			f1.save()
			self.assertEqual(1,0)
		except Exception as e:
			self.assertEqual

	def test_version_1(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		f1.save()
		v1 = Version.objects.create(json='{"prueba":"valor"}', form=f1)
		v1.save()
		self.assertEqual

	def test_version_2(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		f1.save()
		v1 = Version.objects.create(json='{"prueba":"valor"}', form=f1)
		v1.save()
		try:
			v2 = Version.objects.create(json='{"prueba":"valor"}', form=f1,number=8)
			v2.save()
			self.assertEqual(1,0)
		except:
			self.assertEqual

	def test_version_3(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		
		f1.save()
		v1 = Version.objects.create(json='{"prueba":"valor"}', form=f1)
		v1.publish_date=None
		v1.save()
		v1.status=PUBLISHED
		v1.save()
		v2 = Version.objects.create(json='{"prueba":"valor"}', form=f1,status=PUBLISHED)
		v2.publish_date=None
		v2.save()
		l=Version.objects.filter(status=EXPIRED,form=f1)
		print(l)
		self.assertEqual(len(l),1)

	def test_version_4(self):
		try:
			f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
			f1.save()
			v1 = Version.objects.create(json='{"prueba":"valor"}', form=f1)
			v1.publish_date=datetime.datetime.now()
			v1.save()
			self.assertEqual(1,0)
		except:
			self.assertEqual

	def test_queryset_1(self):
		f1 = Form.objects.create(title = "new form1", owner= self.user , slug='slug')
		f1.save()
		v1 = Version.objects.create(json='{"logic": {"fields": {}, "pages": {}}, "pages": [{"fields": [{"tooltip": "", "field_type": "NumberField", "validations": {"max_number": 100, "min_number": 0}, "dependencies": {"fields": [], "pages": []}, "field_id": 1, "answer": [], "text": "Numero", "required": false}, {"tooltip": "", "field_type": "CheckboxField", "options": [{"label": "Leer", "id": 1}, {"label": "TV", "id": 2}, {"label": "Deportes", "id": 3}], "validations": {}, "dependencies": {"fields": [], "pages": []}, "max_id": 3, "field_id": 2, "answer": [], "text": "Hobbies", "required": false}, {"tooltip": "", "field_type": "SelectField", "options": [{"label": "Argentina", "id": 1}, {"label": "Uruguay", "id": 2}, {"label": "Brasil", "id": 3}], "validations": {}, "dependencies": {"fields": [], "pages": []}, "max_id": 3, "field_id": 3, "answer": [], "text": "Paises", "required": false}, {"tooltip": "", "field_type": "TextField", "validations": {"max_len_text": 255}, "dependencies": {"fields": [], "pages": []}, "field_id": 4, "answer": [], "text": "Nombre", "required": false}], "subTitle": "pagina"}], "after_submit": {"sendMail": false, "action": "Show Message", "redirect": "http://", "mailRecipient": "", "message": "Thank you. You successfully filled the form!", "mailSender": "", "mailText": "", "mailSubject": ""}}', form=f1)

		form_entry_1 = FormEntry.objects.create(version=v1, entry_time=datetime.datetime.now())
		form_entry_1.save()

		field_entry_1 = FieldEntry.objects.create(    field_id=1,
													field_type='NumberField',
													text='NumberField',
													required=False,
													shown=True,
													answer=25,
													entry=form_entry_1
												)
		field_entry_1.save()
		field_entry_2 = FieldEntry.objects.create(    field_id=2,
													field_type='TextField',
													text='TextField',
													required=False,
													shown=True,
													answer='Respuesta 1',
													entry=form_entry_1
												)
		field_entry_2.save()
		form_entry_2 = FormEntry.objects.create(version=v1, entry_time=datetime.datetime.now())
		form_entry_2.save()
		field_entry_1 = FieldEntry.objects.create(    field_id=1,
													field_type='NumberField',
													text='NumberField',
													required=False,
													shown=True,
													answer=40,
													entry=form_entry_2
												)
		field_entry_1.save()
		field_entry_2 = FieldEntry.objects.create(    field_id=2,
													field_type='TextField',
													text='TextField',
													required=False,
													shown=True,
													answer='Respuesta 2',
													entry=form_entry_2
												)
		field_entry_2.save()

		queryset = Version.objects.get_entries(version=v1.pk)
		l = queryset.data_number(field_id=1, data=25, operator='lt')
		self.assertEqual(len(l),0)
		l = queryset.data_number(field_id=1, data=25, operator='lte')
		self.assertEqual(len(l),1)
		l = queryset.data_number(field_id=1, data=25, operator='gt')
		self.assertEqual(len(l),1)
		l = queryset.data_number(field_id=1, data=25, operator='gte')
		self.assertEqual(len(l),2)
		l = queryset.data_number(field_id=1, data=40, operator='eq')
		self.assertEqual(len(l),1)
		l = queryset.data_number(field_id=1, data=40, operator='eq', exclude=True)
		self.assertEqual(len(l),1)

		l = queryset.data_icontains(field_id=2, data='Respuesta')
		self.assertEqual(len(l),2)
		l = queryset.data_icontains(field_id=2, data='Respuesta', exclude=True)
		self.assertEqual(len(l),0)
		l = queryset.data_iexact(field_id=2, data='Respuesta')
		self.assertEqual(len(l),0)
		l = queryset.data_iexact(field_id=2, data='Respuesta', exclude=True)
		self.assertEqual(len(l),2)







	def tearDown(self):
		self.user.delete()




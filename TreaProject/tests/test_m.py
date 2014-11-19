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










	def tearDown(self):
		self.user.delete()




from django.test import TestCase
# Create your tests here.
from dynamicForms import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test.client import Client
import datetime;
from dynamicForms import login


class FormTestCase(TestCase):
    
    def setUp(self):
        
        f1 = models.Form.objects.create(title = "new form1", 
                                        publish_date = datetime.datetime.now(),
                                        expiry_date = datetime.datetime.now(),
                                        owner_id = 1)
        f2 = models.Form.objects.create(title = "new form2", 
                                        publish_date = datetime.datetime.now(),
                                        expiry_date = datetime.datetime.now(),
                                        owner_id = 1)
        f3 = models.Form.objects.create(title = "new form3", 
                                        publish_date = datetime.datetime.now(),
                                        expiry_date = datetime.datetime.now(),
                                        owner_id = 1)
        f4 = models.Form.objects.create(title = "new form4", 
                                        publish_date = datetime.datetime.now(),
                                        expiry_date = datetime.datetime.now(),
                                        owner_id = 1)
        f5 = models.Form.objects.create(title = "new form5", 
                                        publish_date = datetime.datetime.now(),
                                        expiry_date = datetime.datetime.now(),
                                        owner_id = 1)
        
        self.user = User.objects.create_user(
            username='user', email='user@Test', password='user')
        
        
    def test_create(self):
        
        f1 = models.Form.objects.get(title = "new form1")
        self.assertEqual(f1.title, "new form1")   
        self.assertEqual(f1.slug, "new-form1")
        
    def test_slug_exists(self):
         
        try:
            f1 = models.Form.objects.create(title = "new fórm1", 
                                            publish_date = datetime.datetime.now(),
                                            expiry_date = datetime.datetime.now(),
                                            owner_id = 1)    
        except Exception:
         
             print ("OK: Creation of new form not allowed because generated slug already exists db")
         #f2 = models.Form.objects.get(title = "new form1")
         
    def test_delete_form(self):
                 
        try: 
            f1 = models.Form.objects.get(title = "new form6")
        except: 
            print("OK: new form6 does not exists because it has never been created")
        f1 = models.Form.objects.get(title = "new form4")
        f1.delete()
        try:
            f1 = models.Form.objects.get(title = "new form4")
        except:
            print("OK: new form4 has been deleted")
            
        f1 = models.Form.objects.get(title = "new form2")
        self.assertEqual(f1.title, "new form2")
        self.assertEqual(f1.slug, "new-form2")
        entry_list = list(models.Form.objects.all())
        count = entry_list.__len__()
        self.assertEqual(count,4)
         
             
    def test_count_forms(self):     
         
         entry_list = list(models.Form.objects.all())
         count = entry_list.__len__()
         self.assertEqual(count,5)
         
    def test_fall_login(self):
        
        c = Client()
        response = c.post('/dynamicForms/login/', {'username': 'user', 'password': 'user'}, follow = True)
        self.assertEqual(response.status_code, 200)
        response = c.post('/dynamicForms/login/', {'username': 'user2', 'password': 'user2'}, follow = True)
        self.assertEqual(response.status_code, 200)
        
        
        
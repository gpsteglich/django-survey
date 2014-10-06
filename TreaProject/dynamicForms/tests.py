from django.test import TestCase
# Create your tests here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test.client import Client
import datetime;

from dynamicForms import login
from dynamicForms.fields import PUBLISHED, DRAFT
from dynamicForms.models import Form,Version,FormEntry,FieldEntry


class FormTestCase(TestCase):
    
    def setUp(self):
                    
        #testing user
        self.user = User.objects.create_user('user', 'user@mail.com', 'password')
        
        #login user
        self.client.login(username='user', password='password')
        
        #create some testing forms
        self.f1 = models.Form.objects.create(title = "new form1", owner= user)
        self.v1 = models.Version.objects.create(json='{"prueba":"valor"}', form=f1)
        self.f2 = models.Form.objects.create(title = "new form2", owner= user)
        self.v2 = models.Version.objects.create(json='{"prueba":"valor"}', form=f2)
                                      
    def test_new_version_form(self):
        
        #create-new-version-for-form-f1
        self.client.get("/dynamicForms/version/"+self.f1.id+"/"+self.v1.number+"/new", follow=True)
        
        #check-if-new-version-was-created
        new_version = models.Version.objects.get(number=self.v1.number+1)
        
        #check-if-new-version's-data-is-correct
        self.assertEqual(new_version.form, self.f1)   
        self.assertEqual(new_version.status, DRAFT)
        self.assertEqual(new_version.json, self.v1.json)
    
  
    def test_duplicate_form(self):
        
        #duplicate-form-f1
        resp.self.client.get("/dynamicForms/version/"+self.f1.id+"/"+self.v1.number+"/duplicate", follow=True)
        self.assertEqual(resp.status_code, 200)
        
        #check-if-form-was-correctly-duplicated
        f1_duplicated = models.Form.objects.get(title=self.f1.title+"(duplicated)")
        
        #check-if-its+data-is-correct
        versions = models.Version.objects.filter(form=f1_duplicated)
             
        self.assertEqual(len(versions), 1)
        v = versions[0]
        self.assertEqual(v.status, DRAFT)
        self.assertEqual(v.json, self.v1.json) 
        
        
    def test_delete_form(self):
        
        #delete-form-f1
        self.client.get("/dynamicForms/form/delete/"+self.f2.id, follow=True)
        
        #check-if-form-was-correctly-deleted
        try:
            f2 = models.Form.objects.get(title="new form2" )
        except:
            print("OK: new f1 has been deleted")   

    def test_delete_version(self):
        
        #delete-version1-form-f1
        self.client.get("/dynamicForms/version/delete/"+self.f1.id+"/"+self.v1.number, follow=True)
        
        #check-if-form-was-correctly-deleted
        try:
            f1 = models.Form.objects.get(title="new form1" )
        except:
            print("OK: new f1 has been deleted")
            
        try:
            v1 = models.Version.objects.get(number=self.v1.number)
        except:
            print("OK: new v1 has been deleted")         
    
          

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui  import  Select 

from django.test import LiveServerTestCase
from selenium import webdriver

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import Client

from dynamicForms.fields import PUBLISHED, DRAFT
from dynamicForms.models import Form,Version,FormEntry,FieldEntry
from dynamicForms.views import FillForm

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui  import  Select 

import time

class completar_logic(LiveServerTestCase):

    def setUp(self):
              
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.maxDiff = None

        self.user = User.objects.create_user('test', 'email', 'test')
        self.user.save() 
              
        
        self.f1 = Form.objects.create(title = "FormLogic",slug = "Formlogic", owner= self.user)
        self.f1.save()
        j='{"pages": [{"fields": [{"text": "Age:", "dependencies": {"fields": ["2", "3"], "pages": []}, "tooltip": "", "required": false, "validations": {"max_number": null, "min_number": null}, "answer": [], "field_type": "NumberField", "field_id": 1}, {"text": "Sign in E-mail ADULT:", "dependencies": {"fields": [], "pages": []}, "tooltip": "", "required": false, "validations": {"max_len_text": 255}, "answer": [], "field_type": "EmailField", "field_id": 2}, {"text": "Sign in CI UNDER-AGE", "dependencies": {"fields": [], "pages": []}, "tooltip": "", "required": false, "validations": {}, "answer": [], "field_type": "CIField", "field_id": 3}], "subTitle": ""}], "after_submit": {"mailSender": "", "mailSubject": "", "message": "Thank you. You successfully filled the form!", "redirect": "http://", "sendMail": false, "action": "Show Message", "mailText": "", "mailRecipient": ""}, "logic": {"fields": {"2": {"action": "All", "operation": "Show", "conditions": [{"field": 1, "operatorsList": ["greater_than", "greater_than_or_equal", "equal", "not_equal", "less_than_or_equal", "less_than"], "comparator": "greater_than_or_equal", "value": "18", "field_type": "NumberField", "operandKind": "input"}]}, "3": {"action": "All", "operation": "Show", "conditions": [{"field": 1, "operatorsList": ["greater_than", "greater_than_or_equal", "equal", "not_equal", "less_than_or_equal", "less_than"], "comparator": "less_than_or_equal", "value": "17", "field_type": "NumberField", "operandKind": "input"}]}}, "pages": {}}}'
        self.v1 = Version.objects.create(json=j, form=self.f1)
        self.v1.save()
        self.v1.status=PUBLISHED
        self.v1.save()
        time.sleep(5)

    def test_login(self): 

        base_url = "http://localhost:8081/inefop/"
               
        # Go to complete form
        self.driver.get(base_url + "visor#formlogic")
        
        time.sleep(1)
        #Find and complete field Age
        elem = self.driver.find_element_by_xpath("//div[2]/ng-form/div/div/input")
        elem.clear()
        elem.send_keys("16")        
        
        time.sleep(2)
        #find and complete CI
        elem = self.driver.find_element_by_xpath("//div[4]/ng-form/div/div/input")
        elem.send_keys("45907611")
        
        #click in submit
        elem = self.driver.find_element_by_xpath("//div[4]/button").click()
        
        time.sleep(2)
        # Go to complete form again
        #self.driver.get(base_url + "visor#formlogic")
        self.driver.back()
        
        time.sleep(2)
        #Find and complete field Age
        elem = self.driver.find_element_by_xpath("//div[2]/ng-form/div/div/input")
        elem.clear()
        elem.send_keys("34")
                
        time.sleep(2)
        #find and complete email
        elem = self.driver.find_element_by_xpath("//div[3]/ng-form/div/div/input")
        elem.send_keys("correo@gmail.com")
        
        #click in submit
        elem = self.driver.find_element_by_xpath("//div[4]/button").click()
        time.sleep(5)
        
               
        e=FormEntry.objects.filter(version_id=self.v1.id).order_by('id')
        e0=e[0]
        # field Age
        fe=FieldEntry.objects.get(entry_id=e0.id,field_id='1')
        self.assertEqual('16',fe.answer)
        #field
        fe=FieldEntry.objects.get(entry_id=e0.id,field_id='3')
        self.assertEqual('45907611',fe.answer)
        
        e1=e[1]
        # field Age
        fe=FieldEntry.objects.get(entry_id=e1.id,field_id='1')
        self.assertEqual('34',fe.answer)
        #field
        fe=FieldEntry.objects.get(entry_id=e1.id,field_id='2')
        self.assertEqual('correo@gmail.com',fe.answer)        
        

    def tearDown(self):    
        self.driver.close()




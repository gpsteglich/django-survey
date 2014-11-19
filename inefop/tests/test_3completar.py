from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui  import  Select 

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
import json

class completar_form(LiveServerTestCase):

    def setUp(self):
                
        self.user = User.objects.create_user('test', 'email', 'test')
        self.user.save() 
        
        self.f1 = Form.objects.create(title = "FormCampos",slug = "formcampos", owner= self.user)
        self.f1.save()
        j='{"logic": {"pages": {}, "fields": {}}, "after_submit": {"mailText": "", "mailSender": "", "mailSubject": "", "message": "Thank you. You successfully filled the form!", "action": "Show Message", "mailRecipient": "", "redirect": "http://", "sendMail": false}, "pages": [{"subTitle": "", "fields": [{"field_type": "CIField", "field_id": 1, "tooltip": "", "validations": {}, "answer": [], "required": true, "text": "Sign in CI", "dependencies": {"pages": [], "fields": []}}, {"field_type": "CheckboxField", "field_id": 2, "tooltip": "", "validations": {}, "options": [{"id": 1, "label": "Soccer"}, {"id": 2, "label": "Rugby"}, {"id": 3, "label": "Basketball"}], "answer": [], "max_id": 3, "required": false, "text": "Sports you like:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "EmailField", "field_id": 3, "tooltip": "", "validations": {"max_len_text": 255}, "answer": [], "required": false, "text": "Sign in E-mail:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "MatriculaField", "field_id": 4, "tooltip": "", "validations": {}, "answer": [], "required": false, "text": "Car registration:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "NumberField", "field_id": 5, "tooltip": "", "validations": {"max_number": null, "min_number": null}, "answer": [], "required": false, "text": "Age:", "dependencies": {"pages": [], "fields": []}}]}, {"subTitle": "", "fields": [{"field_type": "SelectField", "field_id": 6, "tooltip": "", "validations": {}, "options": [{"id": 1, "label": "Male"}, {"id": 2, "label": "Female"}], "answer": [], "max_id": 2, "required": false, "text": "Sex:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "TextAreaField", "field_id": 7, "tooltip": "", "validations": {"max_len_text": 10}, "answer": [], "required": false, "text": "Somethings about you:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "TextField", "field_id": 8, "tooltip": "", "validations": {"max_len_text": 255}, "answer": [], "required": false, "text": "Whatever you want:", "dependencies": {"pages": [], "fields": []}}]}]}'
        j = json.loads(j) 
        self.v1 = Version.objects.create(json=j, form=self.f1)
        self.v1.save()
        self.v1.status=PUBLISHED
        self.v1.save()
        time.sleep(5)
        
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.maxDiff = None

    def test_login(self): 

        base_url = "http://localhost:8081/inefop/"
                     
        # Go to complete form
        self.driver.get(base_url + "visor#formcampos")
        
        time.sleep(1)
        #Find and complete field CI
        elem = self.driver.find_element_by_xpath("//input")
        elem.click()
        elem.send_keys("45907611")
                
        #Find and select sports
        elem = self.driver.find_element_by_xpath("//div[2]/div/label").click()
        elem = self.driver.find_element_by_xpath("//div[3]/div/label").click()
                
        #Find and complete field Email
        elem = self.driver.find_element_by_xpath("//div[4]/ng-form/div/div/input")
        elem.click()
        elem.send_keys("nicolasribero7@gmail.com")
        
        #Find and complete field Matricula
        elem = self.driver.find_element_by_xpath("//div[5]/ng-form/div/div/input")
        elem.click()
        elem.send_keys("SER1234")
        
        #Find and complete field Age
        elem = self.driver.find_element_by_xpath("//div[6]/ng-form/div/div/input")
        elem.clear()
        elem.send_keys("25")
        
        #next page
        self.driver.find_element_by_xpath("//button[2]").click()
        
        #Find and select sex
        elem = self.driver.find_element_by_xpath("//select")
        elem.click()
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)
        
        #Find and complete field text area
        elem = self.driver.find_element_by_xpath("//textarea")
        elem.send_keys("Adios")
        
        
        #Find and complete field single area
        elem = self.driver.find_element_by_xpath("//div[4]/ng-form/div/div/input")
        elem.send_keys("barbaro")
        
        #Submit
        self.driver.find_element_by_xpath('//div[4]/button').click()
        time.sleep(10)
        
        e=FormEntry.objects.get(version_id=self.v1.id)
        # field CI
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='1')
        self.assertEqual('45907611',fe.answer)
        #field
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='2')
        self.assertEqual('2#3',fe.answer)
        #field Email
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='3')
        self.assertEqual('nicolasribero7@gmail.com',fe.answer)
        #field Matricula
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='4')
        self.assertEqual('SER1234',fe.answer)
        #field Age
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='5')
        self.assertEqual('25',fe.answer)
        #field sex
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='6')
        self.assertEqual('2',fe.answer)
        #field test area
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='7')
        self.assertEqual('Adios',fe.answer)
        #field single area
        fe=FieldEntry.objects.get(entry_id=e.id,field_id='8')
        self.assertEqual('barbaro',fe.answer)       
        
        
    def tearDown(self):    
        self.driver.close() 



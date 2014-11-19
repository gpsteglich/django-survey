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
from selenium.webdriver.common.alert import Alert

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui  import  Select 

import time
import json

class New_form(LiveServerTestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.maxDiff = None

        self.user = User.objects.create_user('test', 'email', 'test')
        self.user.save()

    def test_newform(self):    
        base_url = "http://localhost:8081/inefop/"
                
        # login web
        self.driver.get(base_url + "login/")
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("test")  
        elem.send_keys(Keys.RETURN)
        
        #click in new form
        self.driver.find_element_by_link_text('New form').click()
        
        #put the title
        elem = self.driver.find_element_by_name('title')
        elem.send_keys("FormCampos")
        
        #click in palette and CI button
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('CIField').click()
        
        #click in field add
        self.driver.find_element_by_xpath("//div[1]/ul/li[1]/div/div/label").click()
        
        time.sleep(1)
        #select field in properties and put the question
        elem =self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Sign in CI")
        
        #required true
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[3]/div[1]/lable/input").click()
        
        #---------------------------------------------------------------------
        #click in palette and Checkbox button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('CheckboxField').click()
        
       
        #click in field add
        self.driver.find_element_by_xpath("//div[1]/ul/li[2]/div/div/label").click()
        
        time.sleep(1)
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Sports you like:")
        
        #click in add options
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/button").click()
        #add options
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/div/div/div/input")
        elem.clear()
        elem.send_keys("Soccer")
        #click in add options
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/button").click()
        #add options
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/div[2]/div/div/input")
        elem.clear()
        elem.send_keys("Rugby")
        #click in add options
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/button").click()
        #add options
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/div[3]/div/div/input")
        elem.clear()
        elem.send_keys("Basketball")
        
        #---------------------------------------------------------------------
        #click in palette and Email button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('EmailField').click()
        #click in properties
        
        #click in field add
        self.driver.find_element_by_xpath("//div[1]/ul/li[3]/div/div/label").click()
        
        time.sleep(1)
                
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Sign in E-mail:")
         
        self.driver.execute_script("window.scrollBy(0,450);")        
        
        #---------------------------------------------------------------------
        #click in palette and Matricula button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('MatriculaField').click()
        
        #click in field add
        self.driver.find_element_by_xpath("//div[1]/ul/li[4]/div/div/label").click()
        
        time.sleep(1)
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Car registration:")
               
        #---------------------------------------------------------------------
        
        #click in palette and Number button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('NumberField').click()
        
               
        #click in field add
        self.driver.find_element_by_xpath("//div[1]/ul/li[5]/div/div/label").click()
        
        time.sleep(1)
        
              
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Age:")
        
        self.driver.execute_script("window.scrollBy(0,700);")
        
        ##--------------------------------------------------------------------
        #click in palette and New Page
        self.driver.find_element_by_link_text('Palette').click()
                
        elem=self.driver.find_element_by_id('new_page')
        elem.send_keys(Keys.RETURN)
        
        self.driver.find_element_by_xpath("//form/div[2]/div[2]/div[1]/label").click()
        time.sleep(1)
        ##--------------------------------------------------------------------
        
        #click in palette and Combo Box button        
        self.driver.find_element_by_link_text('Palette').click()
        elem=self.driver.find_element_by_id('SelectField')
        elem.send_keys(Keys.RETURN)
        
        
        self.driver.execute_script("window.scrollBy(0,350);")
        #click in field add        
        self.driver.find_element_by_xpath("//div[2]/ul/li[1]/div/div/label").click()
        time.sleep(1)
                
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Sex:")
        
        #click in add options
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/button").click()
        time.sleep(1)
        
        #go to pop up and add options
        elem = self.driver.find_element_by_xpath("//div[@id='myModal']/div/div/div[2]/div[2]/textarea")
        elem.click()
        elem.send_keys("Male\nFemale")
                #close po up
        self.driver.find_element_by_xpath("//div[@id='myModal']/div/div/div[3]/button").click()
        self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[3]/div[1]/lable/input").click()
        
        #---------------------------------------------------------------------
        
        #click in palette and Multi line text button       
        self.driver.find_element_by_link_text("Palette").click()
        time.sleep(2)
        
        elem=self.driver.find_element_by_id('TextAreaField')
        elem.send_keys(Keys.RETURN)
              
        #click in field add
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/div/div/label").click()
        
        time.sleep(1)
                
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Somethings about you:")
        
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[4]/input")
        elem.clear()
        elem.send_keys("10")
        
        
        self.driver.execute_script("window.scrollBy(0,450);")
        #---------------------------------------------------------------------
        
        #click in palette and Single line text button       
        self.driver.find_element_by_link_text('Palette').click()
        
        elem=self.driver.find_element_by_id('TextField')
        elem.send_keys(Keys.RETURN)
        
        
        #click in field add
        self.driver.find_element_by_xpath("//div[2]/ul/li[3]/div/div/label").click()
        
        time.sleep(1)
        
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Whatever you want:")
        #---------------------------------------------------------------------
                      
        #publish
        self.driver.find_element_by_css_selector('div.text-right > button.btn.btn-default').click()
       
       
        Alert(self.driver).accept()
                
        time.sleep(10)
        
        
        
        form=Form.objects.get(title='FormCampos')
        vers=Version.objects.get(form=form)
        js='{"logic": {"pages": {}, "fields": {}}, "after_submit": {"mailText": "", "mailSender": "", "mailSubject": "", "message": "Thank you. You successfully filled the form!", "action": "Show Message", "mailRecipient": "", "redirect": "http://", "sendMail": false}, "pages": [{"subTitle": "", "fields": [{"field_type": "CIField", "field_id": 1, "tooltip": "", "validations": {}, "answer": [], "required": true, "text": "Sign in CI", "dependencies": {"pages": [], "fields": []}}, {"field_type": "CheckboxField", "field_id": 2, "tooltip": "", "validations": {}, "options": [{"id": 1, "label": "Soccer"}, {"id": 2, "label": "Rugby"}, {"id": 3, "label": "Basketball"}], "answer": [], "max_id": 3, "required": false, "text": "Sports you like:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "EmailField", "field_id": 3, "tooltip": "", "validations": {"max_len_text": 255}, "answer": [], "required": false, "text": "Sign in E-mail:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "MatriculaField", "field_id": 4, "tooltip": "", "validations": {}, "answer": [], "required": false, "text": "Car registration:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "NumberField", "field_id": 5, "tooltip": "", "validations": {"max_number": null, "min_number": null}, "answer": [], "required": false, "text": "Age:", "dependencies": {"pages": [], "fields": []}}]}, {"subTitle": "", "fields": [{"field_type": "SelectField", "field_id": 6, "tooltip": "", "validations": {}, "options": [{"id": 1, "label": "Male"}, {"id": 2, "label": "Female"}], "answer": [], "max_id": 2, "required": false, "text": "Sex:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "TextAreaField", "field_id": 7, "tooltip": "", "validations": {"max_len_text": 10}, "answer": [], "required": false, "text": "Somethings about you:", "dependencies": {"pages": [], "fields": []}}, {"field_type": "TextField", "field_id": 8, "tooltip": "", "validations": {"max_len_text": 255}, "answer": [], "required": false, "text": "Whatever you want:", "dependencies": {"pages": [], "fields": []}}]}]}'
               
        js = json.loads(js)         
        self.assertEquals(json.loads(vers.json),js)
      
                
        def tearDown(self):    
            self.driver.close()     
     
         
        
        
        
         
                    
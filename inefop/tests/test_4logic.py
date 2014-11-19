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

from selenium.webdriver.firefox.webdriver import WebDriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui  import  Select 

import time
import json

class New_logic(LiveServerTestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.user = User.objects.create_user('test', 'email', 'test')
        self.user.save()

    def test_login(self): 

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
        elem.send_keys("FormLogic")
        
        
        #---------------------------------------------------------------------
        
        #click in palette and Number button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('NumberField').click()
       
        time.sleep(1)
        #click in field add
        self.driver.find_element_by_xpath("//ul/li[1]/div/div/label").click()
        
        
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div/input")
        elem.send_keys("Age:")
        
        ##--------------------------------------------------------------------
        
        #click in palette and Email button       
        self.driver.find_element_by_link_text('Palette').click()
        self.driver.find_element_by_id('EmailField').click()
        
                
        self.driver.execute_script("window.scrollBy(0,-100);")
        time.sleep(1)
        #click in field add
        self.driver.find_element_by_xpath("//ul/li[2]/div/div/label").click()
        
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[1]/input")
        elem.send_keys("Sign in E-mail ADULT:")
        
        #LOGIC EMAIL MAYOR
        
        #Click en Config
        self.driver.find_element_by_link_text('Config').click()
        
        #Click in field logic
        self.driver.find_element_by_xpath("//div[@id='tab3']/div[2]/button").click()
        
        time.sleep(1)
        #Click in add logic button
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div[2]/button")
        elem.send_keys(Keys.RETURN)
        
        #Select field Sign in Age:
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[1]/select")
        elem.click()                        
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)
        
        # select condition greater_than_or_equal
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[2]/select")
        elem.click()                        
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)
        
        #put number
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[3]/input")
        elem.send_keys("18")
        
        #Click Apply
        self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[5]/button[1]").click()
        
                                            
        ##--------------------------------------------------------------------
        #click in palette and CI button
        
        time.sleep(1)
        elem = self.driver.find_element_by_link_text('Palette')
        elem.send_keys(Keys.RETURN)
        
        self.driver.find_element_by_id('CIField').click()
        
        time.sleep(1)
        #click in field add
        self.driver.find_element_by_xpath("//ul/li[3]/div/div/label").click()
        
        time.sleep(1)
        #select field in properties and put the question
        elem = self.driver.find_element_by_xpath("//div[@id='tab2']/div/div/div[2]/div[1]/input")
        time.sleep(2)
        elem.send_keys("Sign in CI UNDER-AGE")
        
        
        # LOGIC CI MENOR
        
        #Click en Config
        self.driver.find_element_by_link_text('Config').click()
        
        #Click in field logic
        self.driver.find_element_by_xpath("//div[@id='tab3']/div[2]/button").click()
        
        time.sleep(1)
        #Click in add logic button
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div[2]/button")
        elem.send_keys(Keys.RETURN)
        
        #Select field Sign in Age:
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[1]/select")
        elem.click()                        
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)
        
        # select condition less_than_or_equal
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[2]/select")
        elem.click()                        
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)
        
        #put number
        elem = self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[3]/div/div[3]/input")
        elem.send_keys("17")
        
        #Click Apply
        self.driver.find_element_by_xpath("//div[@id='myLogicModal']/div/div/div[2]/div[5]/button[1]").click()
                
        #publish
        self.driver.find_element_by_xpath("//form/div[2]/div[2]/button[1]").send_keys(Keys.RETURN)
        
        Alert(self.driver).accept()
               
        
        time.sleep(10)
        
        form=Form.objects.get(title='FormLogic')
        vers=Version.objects.get(form=form)
        js='{"pages": [{"fields": [{"text": "Age:", "dependencies": {"fields": ["2", "3"], "pages": []}, "tooltip": "", "required": false, "validations": {"max_number": null, "min_number": null}, "answer": [], "field_type": "NumberField", "field_id": 1}, {"text": "Sign in E-mail ADULT:", "dependencies": {"fields": [], "pages": []}, "tooltip": "", "required": false, "validations": {"max_len_text": 255}, "answer": [], "field_type": "EmailField", "field_id": 2}, {"text": "Sign in CI UNDER-AGE", "dependencies": {"fields": [], "pages": []}, "tooltip": "", "required": false, "validations": {}, "answer": [], "field_type": "CIField", "field_id": 3}], "subTitle": ""}], "after_submit": {"mailSender": "", "mailSubject": "", "message": "Thank you. You successfully filled the form!", "redirect": "http://", "sendMail": false, "action": "Show Message", "mailText": "", "mailRecipient": ""}, "logic": {"fields": {"2": {"action": "All", "operation": "Show", "conditions": [{"field": 1, "operatorsList": ["greater_than", "greater_than_or_equal", "equal", "not_equal", "less_than_or_equal", "less_than"], "comparator": "greater_than_or_equal", "value": "18", "field_type": "NumberField", "operandKind": "input"}]}, "3": {"action": "All", "operation": "Show", "conditions": [{"field": 1, "operatorsList": ["greater_than", "greater_than_or_equal", "equal", "not_equal", "less_than_or_equal", "less_than"], "comparator": "less_than_or_equal", "value": "17", "field_type": "NumberField", "operandKind": "input"}]}}, "pages": {}}}'
             
        js = json.loads(js)         
        self.assertEquals(json.loads(vers.json),js)
    
       
    
    def tearDown(self):    
        self.driver.close() 
        

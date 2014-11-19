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


class Forms(LiveServerTestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        self.user = User.objects.create_user('test', 'email', 'test')
        self.user.save()
        
        #form with one version in status PUBLISHED        
        self.f1 = Form.objects.create(title = "new form1", owner= self.user)
        self.f1.save()
        self.v1 = Version.objects.create(json='{"prueba":"valor"}', form=self.f1)
        self.v1.save()
        self.v1.status=PUBLISHED
        self.v1.save()
        #form with one version in status DRAFT
        self.f2 = Form.objects.create(title = "new form2", owner= self.user)
        self.f2.save()
        self.v2 = Version.objects.create(json='{"prueba":"valor"}', form=self.f2)
        self.v2.save()
        #form with one version in status draft
        self.f3 = Form.objects.create(title = "new form3", owner= self.user)
        self.f3.save()
        self.v3 = Version.objects.create(json='{"prueba":"valor"}', form=self.f3)
        self.v3.save()
        
        
    def test_login(self):   
        
#-----LOGIN
        base_url = "http://localhost:8081/inefop/"      
                

        self.driver.get(base_url + "login/")
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("test")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("test")  
        elem.send_keys(Keys.RETURN)
                
        self.assertEqual(self.driver.current_url, 'http://localhost:8081/inefop/main/')
        
#-----  VIEW      
        
        #deploy options 1st form
        self.driver.find_element_by_css_selector('a > div.col-md-1').click() 

        #button view
        self.driver.find_element_by_xpath("//div[@id='collapse1']/div/table/tbody/tr/th[3]/div/a[2]").click()
         
         #Switch to new window opened
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
               
        self.assertEqual(self.driver.current_url, 'http://localhost:8081/inefop/visor?form=1&ver=1')
        
        self.driver.close()
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        
 # ---------DUPLICATE
        
        #deploy options 1st form
        #self.driver.find_element_by_css_selector('a > div.col-md-1').click() 
        
        #button duplicate
        self.driver.find_element_by_xpath("//div[@id='collapse1']/div/table/tbody/tr[1]/th[3]/div/a[4]").click()    
        time.sleep(4)             
        #check-if-form-was-correctly-duplicated
        f1_duplicated = Form.objects.get(title=self.f1.title+"(2)")
        
        #check-if-its+data-is-correct
        versions = Version.objects.filter(form=f1_duplicated)
             
        self.assertEqual(len(versions), 1)
        v = versions[0]
        self.assertEqual(v.status, DRAFT)
        self.assertEqual(v.json, self.v1.json)  
      
 #----------NEW VERSION
      
        #deploy options 1st form
        self.driver.find_element_by_css_selector('a > div.col-md-1').click() 
          
        #button new version
        self.driver.find_element_by_xpath("//div[@id='collapse1']/div/table/tbody/tr[1]/th[3]/div/a[3]").click()
        
        time.sleep(4)
        #check-if-new-version-was-created
        new_version =Version.objects.get(form=self.v1, number=self.v1.number+1)
        #check-if-new-version's-data-is-correct
        self.assertEqual(new_version.form, self.f1)   
        self.assertEqual(new_version.status, DRAFT)
        self.assertEqual(new_version.json, self.v1.json) 
       
#---DELETE VERSION        
        #deploy options 1st form
        self.driver.find_element_by_css_selector('a > div.col-md-1').click() 
        
        #click in discard changes           
        self.driver.find_element_by_xpath("//div[@id='collapse1']/div/table/tbody/tr[1]/th[3]/div/a[5]").click()
        
        time.sleep(4)
         #delete-version1-form-f1
        id=self.f1.id
        f1=Version.objects.filter(id=id)
        self.assertEqual(1,len(f1))
       
    def tearDown(self):    
        self.driver.close() 
   
   
          
        

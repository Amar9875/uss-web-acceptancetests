from selenium import webdriver
import unittest
from Pages.loginpage import LoginPage
from Locators.locators import Locators
from gevent._monitor import thread_sleep
from datetime import datetime

now = datetime.now()
 
print("now =", now)

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
         
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        
    def test_01_login_valid_ActiveMember(self):
        
        driver =self.driver
        driver.get("https://uss-int-cd.azurewebsites.net/")
        login = LoginPage(driver)
        login.click_loginbutton()
        login.enter_emailaddress("digitaltest5001@uss.com")
        login.click_next()
        login.enter_password("Football123*")
        login.enter_pin("775533")
        login.click_login()
        thread_sleep(15)
        driver.save_screenshot('C:/development/LiClipse Workspace/uss-web-acceptancetests1/Screenshots/activelogin.png')
        print("login successful")
        login.click_logoutbutton()        
       
    def test_02_login_valid_DeferredMember(self):
        
        driver =self.driver
        driver.get("https://uss-int-cd.azurewebsites.net/")
        login = LoginPage(driver)
        login.click_loginbutton()
        login.enter_emailaddress("usstestteam+20@gmail.com")
        login.click_next()
        login.enter_password("Football123*")
        login.enter_pin("660384")
        login.click_login()
        thread_sleep(15)
        driver.save_screenshot('C:/development/LiClipse Workspace/uss-web-acceptancetests1/Screenshots/deferredlogin.png')        
        print("login successful")      
        login.click_logoutbutton() 
        
    def test_03_login_valid_Pensioner(self):
        
        driver =self.driver
        driver.get("https://uss-int-cd.azurewebsites.net/")
        login = LoginPage(driver)
        login.click_loginbutton()
        login.enter_emailaddress("usstestteam+99@gmail.com")
        login.click_next()
        login.enter_password("Football123*")
        login.enter_pin("743648")
        login.click_login()
        thread_sleep(15)
        driver.save_screenshot('C:/development/LiClipse Workspace/uss-web-acceptancetests1/Screenshots/pensionerlogin.png')
        print("login successful")       
        login.click_logoutbutton()     
               
    def test_05_login_invalid_username(self):
        
        driver =self.driver
        driver.get("https://uss-int-cd.azurewebsites.net/")
        login = LoginPage(driver)
        login.click_loginbutton()
        login.enter_emailaddress("abc")
        login.click_next()        
        message = driver.find_element_by_xpath(Locators.invalidemailaddress_message_xpath).text
        self.assertEqual(message,"Please enter a valid email")
        print("login failed")
        driver.save_screenshot('C:/development/LiClipse Workspace/uss-web-acceptancetests1/Screenshots/invaliduser.png')
        
    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
        
if __name__ == '__main__':
    unittest.main()      
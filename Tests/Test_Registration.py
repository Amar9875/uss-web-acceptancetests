from selenium import webdriver
import unittest
from Pages.registrationpage import RegistrationPage
from Locators.locators import Locators
from gevent._monitor import thread_sleep
from datetime import datetime



now = datetime.now()
 
print("now =", now)

class RegisterTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
         
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        
    def test_01_Active_Member_Already_Registered(self):
        driver =self.driver
        driver.get("https://uss-int-cd.azurewebsites.net/")
        register = RegistrationPage(driver)
        register.click_registerbutton()
        register.enter_membernumber('48236137')
        register.enter_emailaddress('digitaltest5001@uss.com')
        register.enter_mobile('07757775141')
        register.enter_password('Football123*')    
        register.enter_confirmpassword('Football123*')
        register.security_question('3')
        register.security_answer("Liverpool")
        driver.implicitly_wait(10)
        register.click_next()
        register.enter_nationalinsurance('UV236127d')
        register.enter_surname('Fuchsiayap')
        register.select_gender('male')
        register.enter_day_dateofbirth('02')
        register.enter_month_dateofbirth('01')
        register.enter_year_dateofbirth('1961')
        register.click_terms()
        register.click_completeregistration()  
        thread_sleep(10)      
        driver.save_screenshot('C:/development/LiClipse Workspace/uss-web-acceptancetests1/Screenshots/activeduserregistration.png')
        message = driver.find_element_by_xpath(Locators.registrationunsuccessful_message_xpath).text
        self.assertEqual(message,"Registration unsuccessful")
        print("Registration failed")
            
        
    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
        
if __name__ == '__main__':
    unittest.main()          
from Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from gevent._monitor import thread_sleep

class RegistrationPage():
    
    def __init__(self, driver):
        self.driver = driver
                
        self.registerbutton_button_xpath  =  Locators.registerbutton_button_xpath
        self.membernumber_textbox_xpath   =  Locators.membernumber_textbox_xpath
        self.emailaddress_textbox_xpath   =  Locators.emailaddress_textbox_xpath
        self.mobile_textbox_xpath         =  Locators.mobile_textbox_xpath
        self.password_textbox_xpath       =  Locators.password_textbox_xpath   
        self.confirmpassword_textbox_xpath=  Locators.confirmpassword_textbox_xpath  
        self.securityquestion_dropdown_xpath = Locators.securityquestion_dropdown_xpath
        self.securityanswer_textbox_xpath = Locators.securityanswer_textbox_xpath
        self.next_button_xpath            = Locators.next_button_xpath
        self.nationalinsurance_textbox_xpath = Locators.nationalinsurance_textbox_xpath
        self.surname_textbox_xpath        = Locators.surname_textbox_xpath
        self.gender_radiobutton_male_xpath= Locators.gender_radiobutton_male_xpath
        self.gender_radiobutton_female_xpath = Locators.gender_radiobutton_female_xpath
        self.dateofbirth_date_xpath       = Locators.dateofbirth_date_xpath
        self.dateofbirth_month_xpath      = Locators.dateofbirth_month_xpath
        self.dateofbirth_year_xpath       = Locators.dateofbirth_year_xpath
        self.termsandconditions_checkbox_xpath = Locators.termsandconditions_checkbox_xpath
        self.completeregistration_button_xpath = Locators.completeregistration_button_xpath
        self.registrationunsuccessfull_message_xpath = Locators.registrationunsuccessful_message_xpath
        
    def click_registerbutton(self): 
            self.driver.find_element_by_xpath(self.registerbutton_button_xpath).click()
            
    def enter_membernumber(self, membernumber):
            self.driver.find_element_by_xpath(self.membernumber_textbox_xpath).clear()    
            self.driver.find_element_by_xpath(self.membernumber_textbox_xpath).send_keys(membernumber)
            
    def enter_emailaddress(self, emailaddress):
            self.driver.find_element_by_xpath(self.emailaddress_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.emailaddress_textbox_xpath).send_keys(emailaddress)
            
    def enter_mobile(self, mobile):
            self.driver.find_element_by_xpath(self.mobile_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.mobile_textbox_xpath).send_keys(mobile)
            
    def enter_password(self, password):
            self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
            
    def enter_confirmpassword(self, confirmpassword):
            self.driver.find_element_by_xpath(self.confirmpassword_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.confirmpassword_textbox_xpath).send_keys(confirmpassword)
            
    def security_question(self, Index):
            select = Select(self.driver.find_element_by_xpath(self.securityquestion_dropdown_xpath))
            select.select_by_index(Index)
        
    def security_answer(self, securityanswer):
            self.driver.find_element_by_xpath(self.securityanswer_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.securityanswer_textbox_xpath).send_keys(securityanswer)
            
    def click_next(self):
            self.driver.find_element_by_xpath(self.next_button_xpath).click()
            
    def enter_nationalinsurance(self, nationalinsurance):
            self.driver.find_element_by_xpath(self.nationalinsurance_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.nationalinsurance_textbox_xpath).send_keys(nationalinsurance)
            
    def enter_surname(self, surname):
            self.driver.find_element_by_xpath(self.surname_textbox_xpath).clear()
            self.driver.find_element_by_xpath(self.surname_textbox_xpath).send_keys(surname)
            
    def select_gender(self,value):
            thread_sleep(1)
            if value=='male':
                self.driver.find_element_by_xpath(self.gender_radiobutton_male_xpath).click()  
            elif value=='female':
                self.driver.find_element_by_xpath(self.gender_radiobutton_female_xpath).click()                                 
            
    def enter_day_dateofbirth(self, date):
            self.driver.find_element_by_xpath(self.dateofbirth_date_xpath).clear()
            self.driver.find_element_by_xpath(self.dateofbirth_date_xpath).send_keys(date)
            
    def enter_month_dateofbirth(self, month):
            self.driver.find_element_by_xpath(self.dateofbirth_month_xpath).clear()
            self.driver.find_element_by_xpath(self.dateofbirth_month_xpath).send_keys(month)
            
    def enter_year_dateofbirth(self, year):
            self.driver.find_element_by_xpath(self.dateofbirth_year_xpath).clear()
            self.driver.find_element_by_xpath(self.dateofbirth_year_xpath).send_keys(year)
            
    def click_terms(self):
            thread_sleep(5)
            self.driver.find_element_by_xpath(self.termsandconditions_checkbox_xpath).click()
            
            
    def click_completeregistration(self):   
            thread_sleep(10)
            self.driver.find_element_by_xpath(self.completeregistration_button_xpath).click()      

    def check_registrationsuccessfull(self):   
        msg=self.driver.find_element_by_xpath(self.registrationunsuccessfull_message_xpath).text
        return msg
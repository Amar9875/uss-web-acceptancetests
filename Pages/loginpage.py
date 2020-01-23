from Locators.locators import Locators
from sqlalchemy.sql.expression import false

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.loginbutton_button_xpath   = Locators.loginbutton_button_xpath
        self.emailaddress_textbox_xpath = Locators.emailaddress_textbox_xpath
        self.next_button_xpath          = Locators.next_button_xpath
        self.password_textbox_xpath     = Locators.password_textbox_xpath
        self.pin_digit_one_xpath        = Locators.pin_digit_one_xpath
        self.pin_digit_two_xpath        = Locators.pin_digit_two_xpath
        self.pin_digit_three_xpath      = Locators.pin_digit_three_xpath
        self.login_button_xpath         = Locators.login_button_xpath
        self.invalidemailaddress_message_xpath = Locators.invalidemailaddress_message_xpath
        self.logoutbutton_button_xpath  = Locators.logout_xpath
        
    def click_loginbutton(self):
        self.driver.find_element_by_xpath(self.loginbutton_button_xpath).click()    
    
    def enter_emailaddress(self, emailaddress):
        self.driver.find_element_by_xpath(self.emailaddress_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.emailaddress_textbox_xpath).send_keys(emailaddress)
        
    def click_next(self):
        self.driver.find_element_by_xpath(self.next_button_xpath).click()
        
    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        
    def enter_pin(self, pin):
        pin = list(map(int, str(pin)))
        for i in range(1,4):
            randompin = self.driver.find_element_by_xpath("//legend[contains(text(),'digits from your PIN')]/following::label["+str(i)+"]").text
            randompin = int(randompin[0])
            self.driver.find_element_by_xpath("//legend[contains(text(),'digits from your PIN')]/following::input["+str(i)+"]").send_keys(str(pin[randompin-1]))
      
    def click_logoutbutton(self):
        self.driver.find_element_by_xpath(self.logoutbutton_button_xpath).click()
            
    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        
    def check_invalid_email_address_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidemailaddress_message_xpath).text
        return msg
    
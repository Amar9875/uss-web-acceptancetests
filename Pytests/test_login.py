from selenium import webdriver
import unittest

import pytest
from Pages import loginpage

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginPage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login = loginpage(self.driver)
        
    def test_validlogin_TC001(self):
        self.login.Login()
        result = self.login.verifyLoginSuccessful()   
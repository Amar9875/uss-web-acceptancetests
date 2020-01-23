class HomePage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.welcome_link_xpath = "//h2[contains(text(),'Welcome to My USS')]"
        self.logout_link_xpath = "//body/div[@class='js-wrapper']/header[@class='c-header']/div[@class='c-header__inner']/div[@class='c-header__links']/form[@class='c-header__links-form']/button[1]"
    
    def click_welcome(self):
        self.driver
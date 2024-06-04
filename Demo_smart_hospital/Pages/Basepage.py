from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def _init_(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,30)
        self.action=ActionChains(self.driver)
    
    def for_send_keys(self,element,value):
        element.send_keys(value)

    def for_click(self,element)
        element.click()
    
    def find(self,locator):
        return self.driver.find_element(*locator)
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def init(self,driver):
        self._driver=driver
        self._wait=WebDriverWait(self._driver,20)
        self.action=ActionChains(self._driver)
    
    def for_send_keys(self,element_e,value):
        element = self.find(element_e)
        element.send_keys(value)

    def for_click(self,element_e):
        element = self.find(element_e)
        element.click()
    
    def find(self,locator):
        return self._driver.find_element(*locator)
    
    
    def wait_for_element(self, locator):
        self._wait.until(
            EC.visibility_of_element_located(locator)
        )
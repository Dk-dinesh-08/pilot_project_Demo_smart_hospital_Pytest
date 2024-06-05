from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self._driver=driver
        self._wait=WebDriverWait(self._driver,20)
        self.action=ActionChains(self._driver)
    
    Home_login_button=(By.XPATH,"//ul[@class='top-right']//a")
    Admin_login_button=(By.XPATH,"(//a[@class='forgot pull-right'])[1]")
    Doctor_login_button=(By.XPATH,"(//a[@class='btn btn-primary width100'])[2]")
    Sign_in_button=(By.CSS_SELECTOR,"button[class='btn']")


    def for_send_keys(self,element,value):
       element.send_keys(value)


    def for_click(self,element):
        element.click()
    

    def find(self,locator):
        return self._driver.find_element(*locator)
    

    def wait_for_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))


    def click_Home_login_button(self):
        self.for_click(self.wait_for_element(self.Home_login_button))   


    def click_Admin_login_button(self):
        self.for_click(self.wait_for_element(self.Admin_login_button))


    def click_Doctor_login_button(self):
        self.for_click(self.wait_for_element(self.Doctor_login_button))


    def click_Sign_in_button(self):
        self.for_click(self.wait_for_element(self.Sign_in_button))

    
    def switch_to_window(self):
        self._driver.switch_to.window(self._driver.window_handles[1]) 
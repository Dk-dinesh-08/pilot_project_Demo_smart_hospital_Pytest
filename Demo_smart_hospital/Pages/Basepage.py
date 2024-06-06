from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class BasePage:
    def __init__(self,driver):
        self._driver=driver
        self._wait=WebDriverWait(self._driver,20)
        self.action=ActionChains(self._driver)
    
    Home_login_button=(By.XPATH,"//ul[@class='top-right']//a")
    Admin_login_button=(By.XPATH,"(//a[@class='forgot pull-right'])[1]")
    Doctor_login_button=(By.XPATH,"(//a[@class='btn btn-primary width100'])[2]")
    Sign_in_button=(By.CSS_SELECTOR,"button[class='btn']")
    pofile_icon=By.CSS_SELECTOR,"a[class='dropdown-toggle']"
    profile_name=By.CSS_SELECTOR,"div[class='sstopuser-test'] h5"
    invalid_doctor_button=By.XPATH,"//a[text()='Pharmacist']"
    username_field=By.CSS_SELECTOR,"input[name='username']"
    password_field=By.CSS_SELECTOR,"input[name='password']"
    required_username_message=By.CSS_SELECTOR,"input[name='username']+span>p"
    required_password_message=By.CSS_SELECTOR,"input[name='password']+span>p"
    invalid_credentials_message=By.CSS_SELECTOR,"div[class='alert alert-danger']" 

    def for_send_keys(self,element,value):
        element.send_keys(value)

    def for_click(self,element):
        element.click()

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
        
    def click_invalid_doctorlogin_button(self):
        self.for_click(self.wait_for_element(self.invalid_doctor_button))
      
    def verify_successfull_login(self):
        element=self.wait_for_element(self.pofile_icon)
        element.click()
        element=self.wait_for_element(self.profile_name)
        return element.text
      
    def fill_login_using_login_credentials(self,username,password):
        self.for_send_keys(self.wait_for_element(self.username_field),username)
        self.for_send_keys(self.wait_for_element(self.password_field),password)

    def verify_unsuccessfull_login_using_blank_username(self):
        return (self.wait_for_element(self.required_username_message)).text

    def verify_unsuccessfull_login_using_blank_password(self):
        return (self.wait_for_element(self.required_password_message)).text

    def verify_unsuccessfull_login_using_invalid_credentials(self):
        return (self.wait_for_element(self.invalid_credentials_message)).text
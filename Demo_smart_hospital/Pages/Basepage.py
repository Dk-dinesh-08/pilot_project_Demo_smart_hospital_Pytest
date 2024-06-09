from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self,driver):
        self._driver=driver
        self._wait=WebDriverWait(self._driver,20)
        self.action = ActionChains(self._driver)
    
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


    Admin_signin_button=(By.XPATH,"(//a[@class='btn btn-primary width50'])[1]")
    admin_img_icon = By.XPATH,"//img[@class='topuser-image']"
    admin_text = By.XPATH,"//div[@class='sstopuser-test']/h5"
    expected_text = "Admin"

    username_field = By.XPATH,"//input[@name='username']"
    password_field = By.XPATH,"//input[@name='password']"
    signin_button  = By.XPATH,"//button[@class='btn']"
    
    
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
        assert (self.wait_for_element(self.required_username_message)).text=="The Username field is required."

    def verify_unsuccessfull_login_using_blank_password(self):
        assert (self.wait_for_element(self.required_password_message)).text=="The Password field is required."

    def verify_unsuccessfull_login_using_invalid_credentials(self):
        assert (self.wait_for_element(self.invalid_credentials_message)).text=="Invalid Username or Password"

    def click_Admin_signin_button(self):
        self.for_click(self.wait_for_element(self.Admin_signin_button))


    def select_element_by_visible_text(self,locator,text):
        select = Select(self.wait_for_element(locator))
        select.select_by_visible_text(text)

    def select_element_by_value(self,locator,text):
        select = Select(self.wait_for_element(locator))
        select.select_by_value(text)

    def scroll_upto_element(self,locator):
        element=self._driver.find_element(*locator)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def verify_admin_page_opens(self):
        self.for_click(self.wait_for_element(self.admin_img_icon))
        return self.wait_for_element(self.admin_text).text
    
    def enter_login_details(self,username,password):
        self.for_send_keys(self.wait_for_element(self.username_field),username)
        self.for_send_keys(self.wait_for_element(self.password_field),password)
        self.click_Sign_in_button()

    def click_alert_ok(self):
        try:
            alert = self._wait.until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            print(f"No alert present within ")

    def Double_Click(self, element):
        action = ActionChains(self._driver)
        action.double_click(element).perform()

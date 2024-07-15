from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utility import Consolelogger

log =Consolelogger.get_logger()
class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 20)
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
    admin_page_url = "https://demo.smart-hospital.in/admin/admin/dashboard"
    Home_login_button = (By.XPATH, "//ul[@class='top-right']//a")
    Admin_login_button = (By.XPATH, "(//a[@class='forgot pull-right'])[1]")
    Doctor_login_button = (By.XPATH, "(//a[@class='btn btn-primary width100'])[2]")
    Sign_in_button = (By.CSS_SELECTOR, "button[class='btn']")
    pofile_icon = By.CSS_SELECTOR, "a[class='dropdown-toggle']"
    profile_name = By.CSS_SELECTOR, "div[class='sstopuser-test'] h5"
    invalid_doctor_button = By.XPATH, "//a[text()='Pharmacist']"
    username_field = By.CSS_SELECTOR, "input[name='username']"
    password_field = By.CSS_SELECTOR, "input[name='password']"
    required_username_message = By.CSS_SELECTOR, "input[name='username']+span>p"
    required_password_message = By.CSS_SELECTOR, "input[name='password']+span>p"
    invalid_credentials_message = By.CSS_SELECTOR, "div[class='alert alert-danger']"
    Admin_signin_button = (By.XPATH, "(//a[@class='btn btn-primary width50'])[1]")
    admin_img_icon = By.XPATH, "//img[@class='topuser-image']"
    admin_text = By.XPATH, "//div[@class='sstopuser-test']/h5"
    expected_text = "Admin"
    username_field = By.XPATH, "//input[@name='username']"
    password_field = By.XPATH, "//input[@name='password']"
    signin_button = By.XPATH, "//button[@class='btn']"

    def for_send_keys(self, element, value):
        try:
            element.send_keys(value)
        except Exception as e:
            log.error(f"Exception occurred while sending keys: {e}")

    def for_click(self, element):
        try:
            element.click()
        except Exception as e:
            log.error(f"Exception occurred while clicking element: {e}")


    def wait_for_element(self, locator):
        try:
            return self._wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error(f"Exception occurred while waiting for element: {e}")
            return None



    def wait_for_elements(self, locator):
        try:
            return self._wait.until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            log.error(f"Exception occurred while waiting for elements: {e}")
            return None
    
    def click_Home_login_button(self):
        try:
            self.for_click(self.wait_for_element(self.Home_login_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking Home login button: {e}")

    def click_Admin_login_button(self):
        try:
            self.for_click(self.wait_for_element(self.Admin_login_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking Admin login button: {e}")

    def click_Doctor_login_button(self):
        try:
            self.for_click(self.wait_for_element(self.Doctor_login_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking Doctor login button: {e}")


    def click_Sign_in_button(self):
        try:
            self.for_click(self.wait_for_element(self.Sign_in_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking Sign in button: {e}")

    def switch_to_window(self):
        try:
            self._driver.switch_to.window(self._driver.window_handles[1])
        except Exception as e:
            log.error(f"Exception occurred while switching to window: {e}")

    def click_invalid_doctorlogin_button(self):
        try:
            self.for_click(self.wait_for_element(self.invalid_doctor_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking invalid doctor login button: {e}")

    def verify_successfull_login(self):
        try:
            element = self.wait_for_element(self.pofile_icon)
            element.click()
            element = self.wait_for_element(self.profile_name)
            return element.text
        except Exception as e:
            log.error(f"Exception occurred while verifying successful login: {e}")
            return None


    def clear_login_field(self):
        try:
            self.wait_for_element(self.username_field).clear()
            self.wait_for_element(self.password_field).clear()
        except Exception as e:
            log.error(f"Exception occurred while clearing login fields: {e}")

    def fill_login_using_login_credentials(self, username, password):
        try:
            self.for_send_keys(self.wait_for_element(self.username_field), username)
            self.for_send_keys(self.wait_for_element(self.password_field), password)
        except Exception as e:
            log.error(f"Exception occurred while filling login credentials: {e}")

    def verify_unsuccessfull_login_using_blank_username(self):
        try:
            assert (self.wait_for_element(self.required_username_message)).text == "The Username field is required."
        except Exception as e:
            log.error(f"Exception occurred while verifying unsuccessful login with blank username: {e}")

    def verify_unsuccessfull_login_using_blank_password(self):
        try:
            assert (self.wait_for_element(self.required_password_message)).text == "The Password field is required."
        except Exception as e:
            log.error(f"Exception occurred while verifying unsuccessful login with blank password: {e}")

    def verify_unsuccessfull_login_using_invalid_credentials(self):
        try:
            assert (self.wait_for_element(self.invalid_credentials_message)).text == "Invalid Username or Password"
        except Exception as e:
            log.error(f"Exception occurred while verifying unsuccessful login with invalid credentials: {e}")

    def click_Admin_signin_button(self):
        try:
            self.for_click(self.wait_for_element(self.Admin_signin_button))
        except Exception as e:
            log.error(f"Exception occurred while clicking Admin sign in button: {e}")

    def select_element_by_visible_text(self, locator, text):
        try:
            select = Select(self.wait_for_element(locator))
            select.select_by_visible_text(text)
        except Exception as e:
            log.error(f"Exception occurred while selecting element by visible text: {e}")

    def select_element_by_value(self, locator, text):
        try:
            select = Select(self.wait_for_element(locator))
            select.select_by_value(text)
        except Exception as e:
            log.error(f"Exception occurred while selecting element by value: {e}")

    def scroll_upto_element(self, locator):
        try:
            element = self._driver.find_element(*locator)
            self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            log.error(f"Exception occurred while scrolling to element: {e}")
      
    
    def enter_login_details(self,username,password):
        self.for_send_keys(self.wait_for_element(self.username_field),username)
        self.for_send_keys(self.wait_for_element(self.password_field),password)
        self.click_Sign_in_button()

    def verify_admin_page_opens(self):
        try:
            self.for_click(self.wait_for_element(self.admin_img_icon))
            return self.wait_for_element(self.admin_text).text
        except Exception as e:
            log.error(f"Exception occurred while verifying admin page opens: {e}")
            return None

    def enter_login_details(self, username, password):
        try:
            self.for_send_keys(self.wait_for_element(self.username_field), username)
            self.for_send_keys(self.wait_for_element(self.password_field), password)
            self.click_Sign_in_button()
        except Exception as e:
            log.error(f"Exception occurred while entering login details: {e}")


    def click_alert_ok(self):
        try:
            alert = self._wait.until(EC.alert_is_present())
            alert.accept()
        except (TimeoutException, NoAlertPresentException) as e:
            log.error(f"Exception occurred while clicking alert OK: {e}")

    def Double_Click(self, element):
        action = ActionChains(self._driver)
        action.double_click(element).perform()


    def click_elefunction(self, element):
        try:
            self._driver.execute_script("arguments[0].click()", element)
        except WebDriverException as e:
            log.error(f"Exception occurred while executing click script: {e}")

    def type_text(self, element, input_text):
        try:
            self._driver.execute_script("arguments[0].value='" + input_text + "'", element)
        except WebDriverException as e:
            log.error(f"Exception occurred while typing text: {e}")


    def getting_element(self,element):
        self._driver.execute_script(element)
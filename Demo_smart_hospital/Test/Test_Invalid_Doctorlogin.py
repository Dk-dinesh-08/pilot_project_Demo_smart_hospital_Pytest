import pytest
from Pages.Basepage import BasePage
from Utility import read_config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestInvalidDoctorlogin:
    def test_invalid_doctorlogin_by_clicking_invalid_option(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_invalid_doctorlogin_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")==False
    
    def test_invalidlogin_with_blank_username(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("blank login info","blank_username")
        password=read_config.get_config("invalid login info","doctor_invalid_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_username()
    
    def test_invalidlogin_with_blank_password(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("valid login info","doctor_valid_username")
        password=read_config.get_config("blank login info","blank_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_password()

    def test_invalidlogin_with_invalid_credentials(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("invalid login info","doctor_invalid_username")
        password=read_config.get_config("invalid login info","doctor_invalid_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_invalid_credentials()

    def test_invalidlogin_with_blank_username_and_password(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("blank login info","blank_username")
        password=read_config.get_config("blank login info","blank_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_username()
        Basepage.verify_unsuccessfull_login_using_blank_password()

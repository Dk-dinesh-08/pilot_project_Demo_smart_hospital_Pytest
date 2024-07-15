import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestUserlogin:
    @pytest.mark.smoke
    def test_valid_userlogin_by_default_credentials(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.click_Sign_in_button()
            result=Basepage.verify_successfull_login()
            assert result.__eq__("Patient")
            log.info("User logged in successfully")
        except Exception as e:
            log.error(f"Error occurred in test valid userlogin by default credentialss ")

    @pytest.mark.smoke
    def test_invalidlogin_with_blank_username(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.clear_login_field()
            username=read_config.get_config("blank login info","blank_username")
            password=read_config.get_config("invalid login info","user_invalid_password")
            Basepage.fill_login_using_login_credentials(username,password)
            Basepage.click_Sign_in_button()
            Basepage.verify_unsuccessfull_login_using_blank_username()
            log.info("Invalid user login asserted successfully")
        except Exception :
            log.error(f"Error occurred in test login with invalid credentials ")
    
    @pytest.mark.smoke
    def test_invalidlogin_with_blank_password(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.clear_login_field()
            username=read_config.get_config("valid login info","user_valid_username")
            password=read_config.get_config("blank login info","blank_password")
            Basepage.fill_login_using_login_credentials(username,password)
            Basepage.click_Sign_in_button()
            Basepage.verify_unsuccessfull_login_using_blank_password()
            log.info("Invalid user login asserted successfully")
        except Exception:
            log.error("Error occurred in test login with invalid credentials ")

    @pytest.mark.smoke
    def test_invalidlogin_with_invalid_credentials(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.clear_login_field()
            username=read_config.get_config("invalid login info","user_invalid_username")
            password=read_config.get_config("invalid login info","user_invalid_password")
            Basepage.fill_login_using_login_credentials(username,password)
            Basepage.click_Sign_in_button()
            Basepage.verify_unsuccessfull_login_using_invalid_credentials()
            log.info("Invalid user login asserted successfully")
        except Exception:
            log.error("Error occurred in test login with invalid credentials ")
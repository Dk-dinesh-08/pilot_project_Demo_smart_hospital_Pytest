import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestDoctorlogin:
    @pytest.mark.smoke
    def test_valid_doctorlogin(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        log.info("Doctor logged in successfully")

    @pytest.mark.smoke
    def test_invalid_doctorlogin_by_clicking_invalid_option(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_invalid_doctorlogin_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")==False
        log.info("Invalid doctor login asserted successfully")
    
    @pytest.mark.smoke
    def test_invalidlogin_with_blank_username(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("blank login info","blank_username")
        password=read_config.get_config("invalid login info","doctor_invalid_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_username()
        log.info("Invalid doctor login asserted successfully")
    
    @pytest.mark.smoke
    def test_invalidlogin_with_blank_password(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("valid login info","doctor_valid_username")
        password=read_config.get_config("blank login info","blank_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_password()
        log.info("Invalid doctor login asserted successfully")

    @pytest.mark.smoke
    def test_invalidlogin_with_invalid_credentials(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("invalid login info","doctor_invalid_username")
        password=read_config.get_config("invalid login info","doctor_invalid_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_invalid_credentials()
        log.info("Invalid doctor login asserted successfully")

    @pytest.mark.smoke
    def test_invalidlogin_with_blank_username_and_password(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        username=read_config.get_config("blank login info","blank_username")
        password=read_config.get_config("blank login info","blank_password")
        Basepage.fill_login_using_login_credentials(username,password)
        Basepage.click_Sign_in_button()
        Basepage.verify_unsuccessfull_login_using_blank_username()
        Basepage.verify_unsuccessfull_login_using_blank_password()
        log.info("Invalid doctor login asserted successfully")

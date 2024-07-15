import pytest
from Pages.Adminpage import AdminPage
from Utility import read_config
from Utility import Consolelogger

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestLogin():
    @pytest.mark.smoke
    def test_valid_login(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            log.info("Login with valid username and Password")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            actual_text=admin.verify_admin_page_opens()
            assert actual_text.__eq__(admin.expected_text)
            log.info("Successfully logged in as admin")
        except Exception:
            log.error("Failed in the test valid login")

    @pytest.mark.regression
    def test_invalid_login_with_invalid_data(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()

        try:
            username=read_config.get_config("invalid admin login info","invalid_username")
            password=read_config.get_config("invalid admin login info","invalid_password")
            log.info("Login with invalid data /nUsername: " + username + " and password: " + password)
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.enter_login_details(username,password)
            assert admin.verify_incorrect_admin_login()
            log.info("Verified incorrect admin login")
        except Exception:
            log.error("Failed in the test Invalid login with invalid data")


    @pytest.mark.regression
    def test_login_with_blank_username_and_valid_password(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            username=read_config.get_config("blank admin login info","blank_username")
            password=read_config.get_config("valid admin login info","valid_password")
            log.info("Login with blank username /nUsername: " + username + " and password: " + password)
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.enter_login_details(username,password)
            assert admin.verify_login_with_blank_username_and_valid_password()
            log.info("Verified login with blank username and valid password")
        except Exception:
            log.error("Failed in the test login with blank username and valid password")


    @pytest.mark.regression
    def test_login_with_valid_username_and_blank_password(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            username=read_config.get_config("valid admin login info","valid_username")
            password=read_config.get_config("blank admin login info","blank_password")
            log.info("Login with blank password /nUsername: " + username + " and password: " + password)
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.enter_login_details(username,password)
            assert admin.verify_login_with_valid_username_and_blank_password()
            log.info("Verified login with valid username and blank password")
        except:
            log.error("Failed in the test login with valid username and blank password")


    @pytest.mark.regression
    def test_login_with_blank_username_and_blank_password(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            username=read_config.get_config("blank admin login info","blank_username")
            password=read_config.get_config("blank admin login info","blank_password")
            log.info("Login with blank data /nUsername: " + username + " and password: " + password)
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.enter_login_details(username,password)
            admin.verify_login_with_blank_username_and_blank_password()
            log.info("Verified login with blank username and blank password")
        except Exception:
            log.error("Failed in the test login with blank username blank password")


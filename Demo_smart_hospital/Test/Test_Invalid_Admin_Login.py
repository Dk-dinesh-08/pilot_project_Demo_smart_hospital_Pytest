import pytest
from Pages.Adminpage import AdminPage
from Utility import read_config


@pytest.mark.usefixtures("test_setup_and_setdown")

class TestInvalidAdminLogin():

    def test_invalid_login_with_invalid_data(self):
        admin=AdminPage(self.driver)
        username=read_config.get_config("invalid admin login info","invalid_username")
        password=read_config.get_config("invalid admin login info","invalid_password")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.enter_login_details(username,password)
        assert admin.verify_incorrect_admin_login()

    def test_login_with_blank_username_and_valid_password(self):
        admin=AdminPage(self.driver)
        username=read_config.get_config("blank admin login info","blank_username")
        password=read_config.get_config("valid admin login info","valid_password")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.enter_login_details(username,password)
        assert admin.verify_login_with_blank_username_and_valid_password()

    def test_login_with_valid_username_and_blank_password(self):
        admin=AdminPage(self.driver)
        username=read_config.get_config("valid admin login info","valid_username")
        password=read_config.get_config("blank admin login info","blank_password")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.enter_login_details(username,password)
        assert admin.verify_login_with_valid_username_and_blank_password()

    def test_login_with_blank_username_and_blank_password(self):
        admin=AdminPage(self.driver)
        username=read_config.get_config("blank admin login info","blank_username")
        password=read_config.get_config("blank admin login info","blank_password")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.enter_login_details(username,password)
        admin.verify_login_with_blank_username_and_blank_password()
import pytest
from Pages.Basepage import BasePage
from Utility import read_config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidDoctorlogin:
    def test_valid_doctorlogin(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")

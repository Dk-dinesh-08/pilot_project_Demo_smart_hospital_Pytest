import pytest
from Pages.Basepage import BasePage
from Pages.UserPage import UserPage
from Utility import read_config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidTotalbillcount:
    def test_valid_totalbillcount(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Patient")
        Userpage=UserPage(self.driver)
        Userpage.total_count_of_bill_records_assert()
import pytest
from Pages.Basepage import BasePage
from Pages.UserPage import UserPage
from Utility import read_config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidBillsearch:
    def test_valid_billsearch(self):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Patient")
        Userpage=UserPage(self.driver)
        Userpage.successfull_search_by_bill_number()
        Userpage.verify_successfull_search_by_bill_number()

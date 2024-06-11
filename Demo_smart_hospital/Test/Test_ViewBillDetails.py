import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Pages.UserPage import UserPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestViewBilldetails:
    @pytest.mark.regression
    def test_valid_viewbilldetails(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Patient")
        Userpage=UserPage(self.driver)
        Userpage.successfull_search_by_bill_number()
        Userpage.verify_successfull_search_by_bill_number()
        Userpage.successfull_view_of_bill_details()
        Userpage.verify_successfull_view_bill_details()
        log.info("Bill details viewed successfully")

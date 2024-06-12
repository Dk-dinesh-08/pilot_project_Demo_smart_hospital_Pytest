import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Pages.UserPage import UserPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestBillsearch:
    @pytest.mark.smoke
    def test_valid_billsearch(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.click_Sign_in_button()
            result=Basepage.verify_successfull_login()
            assert result.__eq__("Patient")
            Userpage=UserPage(self.driver)
            result=Userpage.successfull_search_by_bill_number()
            Userpage.verify_successfull_search_by_bill_number()
            log.info(result+" Successfull bill search")
        except TypeError as e:
            print(f"Error occur in test_valid_billsearch : {str(e)}")

    @pytest.mark.smoke
    def test_invalid_billsearch(self):
        log=Consolelogger.get_logger()
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Patient")
        Userpage=UserPage(self.driver)
        Userpage.unsuccessfull_search_by_bill_number()
        Userpage.verify_unsuccessfull_search_by_bill_number()
        log.info("Invalid bill search asserted successfully")


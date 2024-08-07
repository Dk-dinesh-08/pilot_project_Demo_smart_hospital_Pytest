import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Pages.UserPage import UserPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestTotalbillcount:
    @pytest.mark.regression
    def test_valid_totalbillcount(self):
        try:
            Basepage =BasePage(self.driver)
            log=Consolelogger.get_logger()
            Basepage.click_Home_login_button()
            Basepage.click_Sign_in_button()
            result=Basepage.verify_successfull_login()
            assert result.__eq__("Patient")
            Userpage=UserPage(self.driver)
            total=Userpage.total_count_of_bill_records_assert()
            log.info(f"Total bill records:"+total+" Bill records counted successfully")
        except Exception:
            log.error("Error occured in test valid totalbillcount")

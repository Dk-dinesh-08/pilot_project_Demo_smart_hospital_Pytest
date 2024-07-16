import pytest
import time
from Utility import Consolelogger
from Pages.UserPage import UserPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestAppointmentsearch:
    @pytest.mark.regression
    def test_valid_search_user_appointment(self):
        try:
            user_page=UserPage(self.driver)
            log=Consolelogger.get_logger()
            user_page.click_Home_login_button()
            user_page.click_Sign_in_button()
            user_page.click_user_appointment()
            user_page.test_search_record(read_config.get_config("valid_user_search_appointment","user_search_details"))
            user_page.Assert_search_Appointment()
            log.info("Record Search sucessfully")
        except Exception:
                log.error("Error occured in test valid search user appointment")

    @pytest.mark.regression  
    def test_Invalid_search_user_appointment(self):
        try:
            user_page=UserPage(self.driver)
            log=Consolelogger.get_logger()
            user_page.click_Home_login_button()
            user_page.click_Sign_in_button()
            user_page.click_user_appointment()
            user_page.test_search_record(read_config.get_config("Invalid_user_search_appointment","Invalid_user_search_details"))
            user_page.Invalid_Assert_search_Appointment()
            log.info("Invalid Record Search sucessfully")
        except Exception:
                log.error("Error occured in test invalid search user appointment")
    
    
import pytest
from Utility import Consolelogger
from Pages.UserPage import UserPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPayment:
    @pytest.mark.smoke
    def test_valid_Delete_appointment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.click_status_twice()
        user_page.click_delete_button()
        log.info("appointment Delted sucessfully")


   
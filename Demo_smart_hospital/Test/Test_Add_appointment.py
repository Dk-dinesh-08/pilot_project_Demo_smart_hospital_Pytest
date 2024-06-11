import pytest
from Utility import Consolelogger
from Pages.UserPage import UserPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPayment:
    @pytest.mark.smoke
    def test_valid_Add_appointment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.Enter_user_date(read_config.get_config("valid_Add_appointment","valid_date"))
        user_page.Enter_Specialist()
        user_page.Enter_Doctor()
        user_page.Enter_shift()
        user_page.Enter_slot_feild()
        user_page.Enter_Appointment()
        user_page.Enter_Message(read_config.get_config("valid_Add_appointment","valid_message"))
        user_page.Click_live_consultancy()
        user_page.Alternative_address(read_config.get_config("valid_Add_appointment","valid_adress"))
        user_page.click_save_button()
        log.info("Appointment Added sucessfully")
    @pytest.mark.smoke
    def test_Invalid_Add_appointment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.Enter_user_date(read_config.get_config("Invalid_Add_appointment","Invalid_date"))
        user_page.Enter_Specialist()
        user_page.Enter_Doctor()
        user_page.Enter_shift()
        user_page.Enter_slot_feild()
        user_page.click_alert_ok()
        user_page.Enter_Appointment()
        user_page.Enter_Message(read_config.get_config("Invalid_Add_appointment","Invalid_message"))
        user_page.Click_live_consultancy()
        user_page.Alternative_address(read_config.get_config("Invalid_Add_appointment","Invalid_adress"))
        user_page.click_save_button()
        log.info("Invalid Appointment executed sucessfully")
    @pytest.mark.smoke
    def test_empty_Add_appointment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.click_save_button()
        log.info("Appointment Added sucessfully")
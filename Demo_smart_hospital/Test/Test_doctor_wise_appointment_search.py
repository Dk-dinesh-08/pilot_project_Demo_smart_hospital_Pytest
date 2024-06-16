import pytest
from Pages.Adminpage import AdminPage
from Utility import read_config
from Utility import Consolelogger

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestAppointmentSearch():
    @pytest.mark.smoke
    def test_valid_appointment_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test valid appointment search results using doctor info")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_doctor_wise_appointment_search()
        date_entry=read_config.get_config("valid_doctor_wise_appointment_search","date_entry")
        admin.fill_doctorwise_search_form(date_entry)
        verify_text=read_config.get_config("assert_messages","verify_text")
        assert admin.verify_search_results(verify_text)
        log.info("valid appointment search results using doctor info is verified successfully")

    @pytest.mark.smoke
    def test_invalid_appointment_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test invalid appointment search results using doctor info")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_doctor_wise_appointment_search()
        date_entry=read_config.get_config("invalid_doctor_wise_appointment_search","date_entry")
        admin.fill_doctorwise_search_form_without_doctor_field(date_entry)
        invalid_search_text=read_config.get_config("assert_messages","invalid_search_text")
        admin.verify_invalid_search_results(invalid_search_text)
        log.info("Invalid appointment search results using doctor info is verified")




        
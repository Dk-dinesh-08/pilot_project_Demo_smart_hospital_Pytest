import pytest
from Pages.Adminpage import AdminPage
from Utility import read_config
from Utility import Consolelogger

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestAppointmentSearch:
    @pytest.mark.smoke
    def test_valid_appointment_search(self):
        try:
            admin=AdminPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test valid appointment search results using doctor info")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_doctor_wise_appointment_search()
            admin.fill_doctorwise_search_form()
            assert admin.verify_search_results()
            log.info("valid appointment search results using doctor info is verified successfully")
        except Exception:
            log.error(f"Exception occured in TestAppointmentSearch")

    @pytest.mark.smoke
    def test_invalid_appointment_search(self):
        try:
            admin=AdminPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test invalid appointment search results using doctor info")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_doctor_wise_appointment_search()
            admin.fill_doctorwise_search_form_without_doctor_field()
            admin.verify_invalid_search_results()
            log.info("Invalid appointment search results using doctor info is verified")
        except Exception:
            log.error(f"Exception occured in TestAppointmentSearch")





        
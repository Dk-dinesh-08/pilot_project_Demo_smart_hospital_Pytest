import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestPatientSearch():
    @pytest.mark.smoke
    def test_valid_patient_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test search results by patient name")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.enter_patient_name()
        assert admin.verify_patient_search_result()
        log.info("search results by patient name is verified successfully")

    
    @pytest.mark.confirmation
    def test_invalid_patient_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test search results by invalid patient name")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.enter_invalid_patient_name()
        assert admin.verify_invalid_patient_search_result()
        log.info("search results by invalid patient name is verified successfully")
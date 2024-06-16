import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger
from Utility import read_config

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
        patient_name=read_config.get_config("valid_patient_search","patient_name")
        admin.enter_patient_name(patient_name)
        expected_search_text=read_config.get_config("verify_patient_search_result","expected_search_text")
        assert admin.verify_patient_search_result(expected_search_text)
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
        invalid_patient_name=read_config.get_config("invalid_patient_search","invalid_patient_name")
        admin.enter_invalid_patient_name(invalid_patient_name)
        invalid_patient_search_text=read_config.get_config("invalid_patient_search","invalid_patient_search_text")
        assert admin.verify_invalid_patient_search_result(invalid_patient_search_text)
        log.info("search results by invalid patient name is verified successfully")
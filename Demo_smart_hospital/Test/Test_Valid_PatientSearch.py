import pytest
from Pages.Adminpage import AdminPage


@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidPatientSearch():
    def test_valid_patient_search(self):
        admin=AdminPage(self.driver)
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.enter_patient_name()
        assert admin.verify_patient_search_result()
    

import pytest
from Pages.Adminpage import AdminPage



@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidPatientSearch():
    @pytest.mark.confirmation
    def test_invalid_patient_search(self):
        admin=AdminPage(self.driver)
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.enter_invalid_patient_name()
        assert admin.verify_invalid_patient_search_result()
       
    

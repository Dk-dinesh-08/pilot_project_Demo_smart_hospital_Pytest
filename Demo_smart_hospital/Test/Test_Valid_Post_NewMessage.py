import pytest
from Pages.Doctorpage import DoctorPage



@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPostMessage:
    def test_valid_post_new_message(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form()
        Doctor_page.verify_record_saved_successfully()
    

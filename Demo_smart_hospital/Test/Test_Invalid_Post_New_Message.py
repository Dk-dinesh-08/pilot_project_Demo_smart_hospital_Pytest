import pytest
from Pages.DoctorPage import DoctorPage



@pytest.mark.usefixtures("test_setup_and_setdown")
class TestInvalidPostMessage:
    def test_invalid_post_new_message(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form_with_invalid_notification_date()
        Doctor_page.verify_unsucessful_message_for_invalid_notification_date()
    

    def test_invalid_post_new_message_for_msg_body(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form_with_no_message_body()
        Doctor_page.verify_unsucessful_message_for_invalid_message_body()

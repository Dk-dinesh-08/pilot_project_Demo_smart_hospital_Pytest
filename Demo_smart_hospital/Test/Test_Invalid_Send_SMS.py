import pytest
from Pages.DoctorPage import DoctorPage


@pytest.mark.usefixtures("test_setup_and_setdown")
class TestInvalidSendSMS:
    def test_invalid_send_sms_without_sendthrough(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_send_sms_form_without_send_through()
        Doctor_page.verify_unsucessful_message_for_send_through_sms()

    def test_invalid_send_sms_without_title(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_send_sms_form_without_title()
        Doctor_page.verify_unsucessful_message_for_sms_title()
        
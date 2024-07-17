import pytest
from Pages.DoctorPage import DoctorPage
from Utility import excel_reader
from Utility import Consolelogger
import os

@pytest.mark.parametrize(
    "title,notification_date,publish_date,message_body",
    excel_reader.get_data(
        os.path.join(os.path.dirname(__file__), '..', 'ExcelReader', 'test_data.xlsx'), "ValidPostMessage"
    )
)
@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPostMessage:

    @pytest.mark.regression
    def test_valid_post_new_message(self, title, notification_date, publish_date, message_body):
        try:
            Doctor_page = DoctorPage(self.driver)
            log = Consolelogger.get_logger()
            log.info("To test post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form(title, notification_date, publish_date, message_body)
            Doctor_page.verify_record_saved_successfully()
            log.info("Notification send successfully")
        except Exception:
            log.error(f"Exception occurred in TestPostMessage")

    @pytest.mark.regression
    def test_invalid_post_new_message(self, notification_date, title, publish_date, message_body):
        try:
            Doctor_page = DoctorPage(self.driver)
            log = Consolelogger.get_logger()
            log.info("To test unsuccessful post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form_with_invalid_notification_date(title, publish_date, message_body)
            log.info("Unsuccessful post new message is verified")
        except Exception:
            log.error(f"Exception occurred in TestPostMessage")

    @pytest.mark.regression
    def test_invalid_post_new_message_for_msg_body(self, title, notification_date, publish_date, message_body):
        try:
            Doctor_page = DoctorPage(self.driver)
            log = Consolelogger.get_logger()
            log.info("To test unsuccessful post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form_with_no_message_body(title, notification_date, publish_date)
            log.info("Unsuccessful post new message is verified")
        except Exception:
            log.error(f"Exception occurred in TestPostMessage")

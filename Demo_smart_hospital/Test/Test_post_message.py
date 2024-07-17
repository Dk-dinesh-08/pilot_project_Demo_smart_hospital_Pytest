import pytest
from Pages.DoctorPage import DoctorPage
from Utility import excel_reader
from Utility import Consolelogger


@pytest.mark.parametrize("title,notification_date,publish_date,message_body",excel_reader.get_data( "C:\\Project\\Final_Pytest\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","ValidPostMessage"))
@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPostMessage:
    @pytest.mark.regression
    def test_valid_post_new_message(self,title,notification_date,publish_date,message_body):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form(title,notification_date,publish_date,message_body)
            Doctor_page.verify_record_saved_successfully()
            log.info("Notification send successfully")
        except Exception:
            log.error(f"Exception occured in TestPostMessage")
    
    @pytest.mark.regression
    def test_invalid_post_new_message(self,notification_date,title,publish_date,message_body):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test unsucessful post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form_with_invalid_notification_date(title,publish_date,message_body)
            Doctor_page.verify_unsucessful_message_for_invalid_notification_date()
            log.info("unsucessful post new message is verified")
        except Exception:
            log.error(f"Exception occured in TestPostMessage")
    
    @pytest.mark.regression
    def test_invalid_post_new_message_for_msg_body(self,title,notification_date,publish_date,message_body):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test unsucessful post new message functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_post_new_message_form_with_no_message_body(title,notification_date,publish_date)
            Doctor_page.verify_unsucessful_message_for_invalid_message_body()
            log.info("unsucessful post new message is verified")
        except Exception:
            log.error(f"Exception occured in TestPostMessage")

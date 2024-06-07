import pytest
from Pages.DoctorPage import DoctorPage
from Utility import excel_reader


@pytest.mark.parametrize("title,notification_date,publish_date,message_body",excel_reader.get_data( "D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","ValidPostMessage"))
@pytest.mark.usefixtures("test_setup_and_setdown")
class TestInvalidPostMessage:
    def test_invalid_post_new_message(self,notification_date,title,publish_date,message_body):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form_with_invalid_notification_date(title,publish_date,message_body)
        Doctor_page.verify_unsucessful_message_for_invalid_notification_date()
    

    def test_invalid_post_new_message_for_msg_body(self,title,notification_date,publish_date,message_body):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form_with_no_message_body(title,notification_date,publish_date)
        Doctor_page.verify_unsucessful_message_for_invalid_message_body()

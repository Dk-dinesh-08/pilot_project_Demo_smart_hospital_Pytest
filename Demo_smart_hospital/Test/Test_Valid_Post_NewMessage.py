import pytest
from Pages.DoctorPage import DoctorPage
from Utility import excel_reader



@pytest.mark.parametrize("title,notification_date,publish_date,message_body",excel_reader.get_data( "D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","ValidPostMessage"))
@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPostMessage:
    def test_valid_post_new_message(self,title,notification_date,publish_date,message_body):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_post_new_message_form(title,notification_date,publish_date,message_body)
        Doctor_page.verify_record_saved_successfully()
    

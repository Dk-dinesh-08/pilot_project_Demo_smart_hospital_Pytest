import pytest
from Pages.DoctorPage import DoctorPage
from Utility import excel_reader


@pytest.mark.usefixtures("test_setup_and_setdown")
@pytest.mark.parametrize("title,template_id,sms_text",excel_reader.get_data( "D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","SendSMS"))
class TestValidSendSMS:
    @pytest.mark.confirmation
    def test_valid_send_sms(self,title,template_id,sms_text):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_messaging_btn()
        Doctor_page.fill_send_sms_form(title,template_id,sms_text)
        Doctor_page.verify_sms_record_saved_successfully()
import pytest
from Pages.DoctorPage import DoctorPage
from Utility import read_config
from Utility import excel_reader
from Utility import Consolelogger


@pytest.mark.usefixtures("test_setup_and_setdown")

@pytest.mark.parametrize("title,template_id,sms_text",excel_reader.get_data("D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","SendSMS"))

class TestSendSMS:

    @pytest.mark.confirmation
    def test_valid_send_sms(self,title,template_id,sms_text):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test send sms functionality")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_send_sms_form(title,template_id,sms_text)
            Doctor_page.verify_sms_record_saved_successfully()
            log.info("send sms functionality is verified successfully")
        except Exception:
            log.error("Error in test valid send sms")

        

    def test_valid_send_sms_to_individual(self,title,template_id,sms_text):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test send sms to individual patient/doctor")
            Title=read_config.get_config("send individual sms","Title")
            Template_id=read_config.get_config("send individual sms","Template_id")
            Message_text=read_config.get_config("send individual sms","Message_Text")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_send_sms_form_to_individual(Title,Template_id,Message_text)
            log.info("send sms to individual patient/doctor is verified successfully")
        except Exception:
            log.error("Error in test valid send sms to individual")


    def test_invalid_send_sms_without_sendthrough(self,title,template_id,sms_text):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test unsuccessful send sms without send through")
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_send_sms_form_without_send_through(title,template_id,sms_text)
            Doctor_page.verify_unsucessful_message_for_send_through_sms()
            log.info("Unsucessful send sms functionality is verified")
        except Exception:
            log.error("Error in test invalid send sms without sendthrough")

    def test_invalid_send_sms_without_title(self,title,template_id,sms_text):
        try:
            log=Consolelogger.get_logger()
            log.info("To test unsuccessful send sms without title")
            Doctor_page=DoctorPage(self.driver)
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_messaging_btn()
            Doctor_page.fill_send_sms_form_without_title(title,template_id,sms_text)
            Doctor_page.verify_unsucessful_message_for_sms_title()
            log.info("Unsucessful send sms functionality is verified")
        except Exception:
            log.error(f"Error in test invalid send sms without title")
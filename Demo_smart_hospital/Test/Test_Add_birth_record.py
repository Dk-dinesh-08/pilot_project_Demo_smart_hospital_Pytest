import pytest
from Utility import Consolelogger
from Pages.DoctorPage import DoctorPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")      
class TestAddBirthRecord:
    @pytest.mark.regression
    def test_valid_add_birth_record(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.click_add_birth_record()
        Doctor_page.Enter_child_name(read_config.get_config("valid_birth_record","childname"))
        Doctor_page.click_gender()
        Doctor_page.Enter_weight(read_config.get_config("valid_birth_record","weight"))
        Doctor_page.Enter_birth_date(read_config.get_config("valid_birth_record","birth_date"))
        Doctor_page.Enter_contact(read_config.get_config("valid_birth_record","phone"))
        Doctor_page.Enter_address(read_config.get_config("valid_birth_record","Adress"))
        Doctor_page.Enter_case_id(read_config.get_config("valid_birth_record","caseId"))
        Doctor_page.Enter_Father_name(read_config.get_config("valid_birth_record","FatherName"))
        Doctor_page.Enter_report(read_config.get_config("valid_birth_record","report"))
        Doctor_page.click_save_button()
        log.info("Birth Record Added sucessfully")

    @pytest.mark.regression
    def test_Invalid_add_birth_record(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.click_add_birth_record()
        Doctor_page.Enter_child_name(read_config.get_config("Invalid_birth_record","Invalid_childname"))
        Doctor_page.click_gender()
        Doctor_page.Enter_weight(read_config.get_config("Invalid_birth_record","Invalid_weight"))
        Doctor_page.Enter_birth_date(read_config.get_config("Invalid_birth_record","Invalid_birth_date"))
        Doctor_page.Enter_contact(read_config.get_config("Invalid_birth_record","Invalid_phone"))
        Doctor_page.Enter_address(read_config.get_config("Invalid_birth_record","Invalid_Adress"))
        Doctor_page.Enter_case_id(read_config.get_config("Invalid_birth_record","Invalid_caseId"))
        Doctor_page.Assert_patient_not_found()
        Doctor_page.Enter_Father_name(read_config.get_config("Invalid_birth_record","Invalid_FatherName"))
        Doctor_page.Enter_report(read_config.get_config("Invalid_birth_record","Invalid_report"))
        Doctor_page.click_save_button()
        log.info("Invalid birth record Asserted sucessfully")

    @pytest.mark.smoke
    def test_Invalid_case_Id(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.click_add_birth_record()
        Doctor_page.Enter_child_name(read_config.get_config("Invalid_birth_record","Invalid_childname"))
        Doctor_page.click_gender()
        Doctor_page.Enter_weight(read_config.get_config("Invalid_birth_record","Invalid_weight"))
        Doctor_page.Enter_birth_date(read_config.get_config("Invalid_birth_record","Invalid_birth_date"))
        Doctor_page.Enter_contact(read_config.get_config("Invalid_birth_record","Invalid_phone"))
        Doctor_page.Enter_address(read_config.get_config("Invalid_birth_record","Invalid_Adress"))
        Doctor_page.Enter_case_id(read_config.get_config("Invalid_birth_record","variable_case_id"))
        Doctor_page.Assert_variable_id()
        Doctor_page.Enter_Father_name(read_config.get_config("Invalid_birth_record","Invalid_FatherName"))
        Doctor_page.Enter_report(read_config.get_config("Invalid_birth_record","Invalid_report"))
        Doctor_page.click_save_button()
        log.info("Invalid case Id Asserted sucessfully")

    @pytest.mark.regression
    def test_blank_add_birth_data(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.click_add_birth_record()
        Doctor_page.click_save_button()
        Doctor_page.Assert_empty_Field()
        log.info("Empty record Assert Sucessfully")

    


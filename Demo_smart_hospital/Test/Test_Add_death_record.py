import pytest
import time
from Utility import Consolelogger
from Pages.DoctorPage import DoctorPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestAddDeathRecord:
    @pytest.mark.regression
    def test_valid_add_death_record(self):
        try:
            Doctor_page=DoctorPage(self.driver)
            log=Consolelogger.get_logger()
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_Birth_and_death_record()
            Doctor_page.click_death_record()
            Doctor_page.click_add_death_record()
            Doctor_page.Enter_case_id(read_config.get_config("valid_death_record","valid_case_id"))
            Doctor_page.Enter_death_date(read_config.get_config("valid_death_record","Death_date"))
            Doctor_page.Enter_death_report(read_config.get_config("valid_death_record","Death_report"))
            Doctor_page.click_save_button()
            log.info("death record Added sucessfully")
        except Exception:
             log.error("Failed in the test valid death record")

    @pytest.mark.regression
    def test_Invalid_add_death_record(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_Birth_and_death_record()
            Doctor_page.click_death_record()
            Doctor_page.click_add_death_record()
            Doctor_page.Enter_case_id(read_config.get_config("Invalid_death_record","Invalid_case_id"))
            Doctor_page.Assert_patient_not_found()
            Doctor_page.Enter_death_date(read_config.get_config("Invalid_death_record","Invalid_death_date"))
            Doctor_page.Enter_death_report(read_config.get_config("Invalid_death_record","Invalid_Death_report"))
            Doctor_page.click_save_button()
            log.info("Invalid death record Asserted sucessfully")
        except Exception:
             log.error("Failed in the test Invalid death record")

    @pytest.mark.regression
    def test_Invalid_case_Id(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_Birth_and_death_record()
            Doctor_page.click_death_record()
            Doctor_page.click_add_death_record()
            Doctor_page.Enter_case_id(read_config.get_config("Invalid_death_record","variable_case_id"))
            Doctor_page.Assert_variable_id()
            Doctor_page.Enter_death_date(read_config.get_config("Invalid_death_record","Invalid_death_date"))
            Doctor_page.Enter_death_report(read_config.get_config("Invalid_death_record","Invalid_Death_report"))
            Doctor_page.click_save_button()
            log.info("Invalid case ID death record Asserted sucessfully")
        except Exception:
             log.error("Failed in the test Invalid case id")


    @pytest.mark.smoke
    def test_blank_add_birth_data(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        try:
            Doctor_page.click_Home_login_button()
            Doctor_page.click_Admin_login_button()
            Doctor_page.switch_to_window()
            Doctor_page.click_Doctor_login_button()
            Doctor_page.click_Sign_in_button()
            Doctor_page.click_Birth_and_death_record()
            Doctor_page.click_death_record()
            Doctor_page.click_add_death_record()
            Doctor_page.click_save_button()
            Doctor_page.Assert_death_Empty_record()
            log.info("Empty record Assert Sucessfully")
        except Exception:
             log.error("Failed in the test blank death record")


    


import pytest
import time
from Utility import Consolelogger
from Pages.DoctorPage import DoctorPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestBirthSearch:
    @pytest.mark.regression
    def test_valid_birth_search_record(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.search_record(read_config.get_config("valid_birth_search_record","validBirthSearchRecord"))
        Doctor_page.Assert_valid_birth_search_assert()
        log.info("Searched Birth Record Sucessfully")

    @pytest.mark.smoke
    def test_Invalid_birth_search_record(self):
        Doctor_page=DoctorPage(self.driver)
        log=Consolelogger.get_logger()
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.search_record(read_config.get_config("Invalid_birth_search_record","InvalidBirthSearchRecord"))
        Doctor_page.Assert_no_data_availble()
        log.info("Searched Invalid Birth Record asserted Sucessfully")


   
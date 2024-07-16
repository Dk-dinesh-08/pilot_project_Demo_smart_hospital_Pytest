import pytest
from Utility import Consolelogger
from Pages.DoctorPage import DoctorPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestDeathSearch:
    @pytest.mark.regression
    def test_valid_death_search_record(self):
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
            Doctor_page.search_record(read_config.get_config("valid_death_search_record","validDeathSearchRecord"))
            Doctor_page.Assert_valid_death_search_assert()
            log.info("Searched Birth Record Sucessfully")
        except Exception:
                log.error("Error in test valid death search record")

    @pytest.mark.smoke
    def test_Invalid_death_search_record(self):
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
            Doctor_page.search_record(read_config.get_config("Invalid_death_search_record","validDeathSearchRecord"))
            Doctor_page.Assert_no_data_availble()
            log.info("Searched Invalid Birth Record asserted Sucessfully")
        except Exception:
                log.error("Error in test Invalid death search record")


   
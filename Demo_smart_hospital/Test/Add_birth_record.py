import pytest
import time
from Utility import read_config
from Pages.DoctorPage import DoctorPage


@pytest.mark.usefixtures("test_setup_and_setdown")
class TestAddRemove:
    def test_valid_add_birth_record(self):
        Doctor_page=DoctorPage(self.driver)
        Doctor_page.click_Home_login_button()
        Doctor_page.click_Admin_login_button()
        Doctor_page.switch_to_window()
        Doctor_page.click_Doctor_login_button()
        Doctor_page.click_Sign_in_button()
        Doctor_page.click_Birth_and_death_record()
        Doctor_page.click_birth_record()
        Doctor_page.Fill_form_birth_record()
        
    

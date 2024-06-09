import pytest
from Utility import Consolelogger
from Utility import read_config
from Pages.Basepage import BasePage
from Pages.DoctorPage import DoctorPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestUpdateBedstatus:
    @pytest.mark.smoke
    def test_valid_update_bedstatus(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        patient_name=read_config.get_config("bed status patient_name","valid_patient_name")
        Doctorpage.successfull_update_of_the_bedstatus(patient_name)
        Doctorpage.verify_the_successfull_updation_of_the_bedstatus()
        log.info("Bed status updated successfully")

    @pytest.mark.smoke
    def test_invalid_update_bedstatus_with_existing_patient(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        patient_name=read_config.get_config("bed status patient_name","already_existing")
        Doctorpage.unsuccessfull_update_of_the_bedstatus_with_existing_patient(patient_name)
        Doctorpage.verify_the_unsuccessfull_updation_of_the_bedstatus_with_existing_patient()
        log.info("Invalid updation of bed status asserted successfully")

    @pytest.mark.smoke
    def test_invalid_update_bedstatus_without_consultant(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        patient_name=read_config.get_config("bed status patient_name","valid_patient_name1")
        Doctorpage.unsuccessfull_update_of_the_bedstatus_without_consultant(patient_name)
        Doctorpage.verify_the_unsuccessfull_updation_of_the_bedstatus_without_consultant()
        log.info("Invalid updation of bed status asserted successfully")

    @pytest.mark.smoke
    def test_invalid_update_bedstatus_without_appointment_date(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        patient_name=read_config.get_config("bed status patient_name","valid_patient_name1")
        Doctorpage.unsuccessfull_update_of_the_bedstatus_without_appointment_date(patient_name)
        Doctorpage.verify_the_unsuccessfull_updation_of_the_bedstatus_without_appointment_date()
        log.info("Invalid updation of bed status asserted successfully")

    @pytest.mark.smoke
    def test_invalid_update_bedstatus_without_patient(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        Doctorpage.unsuccessfull_update_of_the_bedstatus_without_patient()
        Doctorpage.verify_the_unsuccessfull_updation_of_the_bedstatus_without_patient()
        log.info("Invalid updation of bed status asserted successfully")
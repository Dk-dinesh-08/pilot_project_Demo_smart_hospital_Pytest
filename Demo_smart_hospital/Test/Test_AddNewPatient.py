import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Pages.DoctorPage import DoctorPage
from Utility import read_config
from Utility import excel_reader
import os

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestAddnewpatient:
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number",
        excel_reader.get_data(
            os.path.join(os.path.dirname(__file__), '..', 'ExcelReader', 'NewPatientData.xlsx'), "Valid_data"
        )
    )
    def test_valid_addnewpatient(self, patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number):
        Basepage = BasePage(self.driver)
        log = Consolelogger.get_logger()
        try:
            Basepage.click_Home_login_button()
            Basepage.click_Admin_login_button()
            Basepage.switch_to_window()
            Basepage.click_Doctor_login_button()
            Basepage.click_Sign_in_button()
            result = Basepage.verify_successfull_login()
            assert result == "Doctor"
            Doctorpage = DoctorPage(self.driver)
            Doctorpage.go_to_new_patient_form()
            Doctorpage.fill_new_patient_form(patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number)
            Doctorpage.verify_successfull_addnewpatient()
            log.info("New patient added successfully")
        except Exception:
            log.error("Failed in the test valid new patient")

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number",
        excel_reader.get_data(
            os.path.join(os.path.dirname(__file__), '..', 'ExcelReader', 'NewPatientData.xlsx'), "Invalid_data"
        )
    )
    def test_invalid_addnewpatient_without_patientname(self, patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number):
        Basepage = BasePage(self.driver)
        log = Consolelogger.get_logger()
        try:
            Basepage.click_Home_login_button()
            Basepage.click_Admin_login_button()
            Basepage.switch_to_window()
            Basepage.click_Doctor_login_button()
            Basepage.click_Sign_in_button()
            result = Basepage.verify_successfull_login()
            assert result == "Doctor"
            Doctorpage = DoctorPage(self.driver)
            Doctorpage.go_to_new_patient_form()
            Doctorpage.fill_new_patient_form(patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number)
            Doctorpage.verify_unsuccessfull_addnewpatient_without_patient_name()
        except Exception:
            log.error("Failed in the test Invalid add new patient without patient name")

    @pytest.mark.smoke
    def test_invalid_addnewpatient_without_patient_age(self):
        Basepage = BasePage(self.driver)
        log = Consolelogger.get_logger()
        try:
            Basepage.click_Home_login_button()
            Basepage.click_Admin_login_button()
            Basepage.switch_to_window()
            Basepage.click_Doctor_login_button()
            Basepage.click_Sign_in_button()
            result = Basepage.verify_successfull_login()
            assert result == "Doctor"
            Doctorpage = DoctorPage(self.driver)
            patient_name = read_config.get_config("invalid new patient data", "patient_name")
            guardian_name = read_config.get_config("invalid new patient data", "guardian_name")
            dob = read_config.get_config("invalid new patient data", "dob")
            bloodgroup = read_config.get_config("invalid new patient data", "bloodgroup")
            marital_status = read_config.get_config("invalid new patient data", "marital_status")
            phone_number = read_config.get_config("invalid new patient data", "phone_number")
            email = read_config.get_config("invalid new patient data", "email")
            address = read_config.get_config("invalid new patient data", "address")
            known_allergies = read_config.get_config("invalid new patient data", "known_allergies")
            TPA_Id = read_config.get_config("invalid new patient data", "TPA_Id")
            TPA_Validity = read_config.get_config("invalid new patient data", "TPA_Validity")
            ni_number = read_config.get_config("invalid new patient data", "ni_number")
            alternate_number = read_config.get_config("invalid new patient data", "alternate_number")
            Doctorpage.go_to_new_patient_form()
            Doctorpage.fill_new_patient_form(patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_Id, TPA_Validity, ni_number, alternate_number)
            Doctorpage.verify_unsuccessfull_addnewpatient_without_patient_age()
            log.info("Invalid addition of new patient asserted successfully") 
        except Exception:
            log.error("Failed in the test Invalid add new patient without patient name")

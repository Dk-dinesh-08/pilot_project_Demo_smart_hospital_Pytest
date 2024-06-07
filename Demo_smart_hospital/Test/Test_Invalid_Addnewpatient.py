import pytest
from Pages.Basepage import BasePage
from Pages.DoctorPage import DoctorPage
from Utility import read_config
from Utility import excelReader
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_setdown")
@pytest.mark.parametrize("patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number",excelReader.get_data("C:\\Pytest_Mainproject\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\NewPatientData.xlsx","Invalid_data"))
class TestInvalidAddnewpatient:
    def test_invalid_addnewpatient(self,patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number):
        Basepage =BasePage(self.driver)
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        Doctorpage.go_to_new_patient_form()
        Doctorpage.fill_new_patient_form(patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number)
        Doctorpage.verify_unsuccessfull_addnewpatient()
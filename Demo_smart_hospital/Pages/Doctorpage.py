from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from selenium.webdriver.support.ui import Select
class DoctorPage(BasePage):

    def _init_(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Home page 
    Dashboard=By.CSS_SELECTOR,"i[class='fas fa-television']"
    Appointment=By.XPATH,"//i[@class='fa fa-calendar-check-o']//following-sibling::span"
    IPD_in_patient=By.XPATH,"//i[@class='fas fa-procedures']//parent::a"
    notification_icon=By.XPATH,"//i[@class='fa fa-bell-o']//parent::a"
    language_icon=By.XPATH,"//button[@class='btn dropdown-toggle selectpicker btn-default']"
    betstatus_icon=By.XPATH,"//i[@class='fas fa-bed cal15']//parent::a"

    delete_notification_button=By.XPATH,"//i[@class='fa fa-trash']//parent::button"

    valid_hindi_language=By.XPATH,"//a[normalize-space()='Hindi']"
    invalid_hindi_language=By.XPATH,"//a[normalize-space()='Spanish']"
    #add new patient form
    add_patient_button=By.CSS_SELECTOR,"a[id='addp']"
    new_patient_button=By.CSS_SELECTOR,"a[id='addpip']"
    name_field=By.CSS_SELECTOR,"input[id='name']"
    guardian_name_field=By.CSS_SELECTOR,"div[class='col-lg-6 col-md-6 col-sm-6'] input[name='guardian_name']"
    dob_field=By.XPATH,"//div[@class='col-sm-4']//input[@name='dob']"
    blood_group_field=By.CSS_SELECTOR,"div[class='col-sm-3'] select[name='blood_group']"
    blood_group_field_specific=By.CSS_SELECTOR,"div[class='col-sm-3'] select[name='blood_group'] option"
    marital_status_field=By.CSS_SELECTOR,"div[class='col-sm-3'] select[id='marital_status']"
    phone_number_field=By.CSS_SELECTOR,"input[id='number']"
    email_field=By.CSS_SELECTOR,"input[id='addformemail']"
    address_field=By.CSS_SELECTOR,"input[name='address']"
    remarks=By.CSS_SELECTOR,"textarea[id='note']"
    known_allergies_field=By.CSS_SELECTOR,"div[class='col-lg-12 col-md-12 col-sm-12'] textarea[name='known_allergies']"
    TPA_ID_field=By.CSS_SELECTOR,"input[name='insurance_id']"
    TPA_validity_field=By.CSS_SELECTOR,"input[name='validity']"
    national_identity_number_field=By.CSS_SELECTOR,"input[name='identification_number']"
    alternate_number_field=By.CSS_SELECTOR,"input[id='custom_fields[patient][3]']"
    save_button=By.CSS_SELECTOR,"button[id='formaddpabtn']"

    addnewpatient_validalert=By.CSS_SELECTOR,"div[class='toast-message']"
    addnewpatient_invalidalert=By.CSS_SELECTOR,"div[class='toast-message'] p"
    #betstatus
    bed_145=By.XPATH,"//div[text()='FF - 145']"
    Addmision_date=By.CSS_SELECTOR,"input[id='admission_date']"
    patientSelect_field=By.XPATH,"//span[@class='select2-selection select2-selection--single' and @aria-labelledby='select2-addpatient_id-container']"
    patientinput_field=By.CSS_SELECTOR,"input[class='select2-search__field']"
    consultant_select_field=By.XPATH,"//span[@class='select2-selection select2-selection--single' and @aria-labelledby='select2-consultant_doctor-container']"
    bed_status_save_button=By.CSS_SELECTOR,"button[id='formaddbtn']" 
    doctal_consultant_select=By.XPATH,"//select[@id='consultant_doctor']"
    add_patient_name=By.XPATH,"//li[@class='select2-results__option select2-results__option--highlighted']"

    def successfull_update_of_the_bedstatus(self):
        self.for_click(self.wait_for_element(self.betstatus_icon))
        self.for_click(self.wait_for_element(self.bed_145))
        self.for_click(self.wait_for_element(self.patientSelect_field))
        self.for_send_keys(self.wait_for_element(self.patientinput_field),"Elvio")
        self.for_click(self.wait_for_element(self.add_patient_name))
        self.for_click(self.wait_for_element(self.Addmision_date))
        select_element=self.wait_for_element(self.doctal_consultant_select)
        select=Select(select_element)
        select.select_by_value("11")
        self.for_click(self.wait_for_element(self.bed_status_save_button))

    def verify_the_successfull_updation_of_the_bedstatus(self):
        return (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text
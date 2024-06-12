from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException


class DoctorPage(BasePage):

    def init(self, driver):
        super().__init__(driver)
        self.driver = driver

    Birth_and_death_record=(By.XPATH,"//a/i[@class='fa fa-birthday-cake']")
    Birth_record=(By.XPATH,"//a[text()= ' Birth Record ']")
    Death_record=(By.XPATH,"//a[text()= ' Death Record']")
    Add_birth_record=(By.XPATH,"//a[@class='btn btn-primary btn-sm birthrecord']")
    Add_death_record=(By.XPATH,"//a[@class='btn btn-primary btn-sm deathrecord']")
    Child_name=(By.NAME,"child_name")
    Gender_drop_down=(By.XPATH,"(//select[@class='form-control'])[1]")
    Male_gender_option=(By.XPATH,"//select[@class='form-control']/option[text()='Male                                                ']")
    weight=(By.NAME,"weight")
    birth_date=(By.ID,"birth_date")
    death_date=(By.ID,"death_date")
    contact=(By.ID,"contact")
    adress=(By.ID,"address")
    case_id=(By.ID,"case_id")
    fathers_name=(By.ID,"father_name")
    birth_Report=(By.ID,"birth_report")
    death_report=(By.ID,"death_report")
    save_button=(By.ID,"formaddbtn")
    patient_not_found=(By.CLASS_NAME,"toast-message")
    empty_assert=(By.XPATH,"//div[@class='toast-message']/p[1]")
    search_feild_death_record=(By.XPATH,"//div[@class='toast-message']/p[1]")
    Search_record=(By.CSS_SELECTOR,"input[type='search']")
    no_data_available = (By.XPATH, "//span[@class='text-success bolds']")
    valid_birth_search_assert=(By.XPATH,"//td[text()='BREF62']")
    valid_death_search_assert=(By.XPATH,"//td[text()='DREF50']")

    #Home page 
    Dashboard=By.CSS_SELECTOR,"i[class='fas fa-television']"
    Appointment=By.XPATH,"//i[@class='fa fa-calendar-check-o']//following-sibling::span"
    IPD_in_patient=By.XPATH,"//i[@class='fas fa-procedures']//parent::a"
    notification_icon=By.XPATH,"//i[@class='fa fa-bell-o']//parent::a"
    #language_icon=By.XPATH,"//button[@class='btn dropdown-toggle selectpicker btn-default']"
    language_icon=By.CLASS_NAME,"btn dropdown-toggle selectpicker btn-default"
    betstatus_icon=By.XPATH,"//i[@class='fas fa-bed cal15']//parent::a"
    valid_hindi_language=By.XPATH,"//a[normalize-space()='Hindi']"
    invalid_hindi_language=By.XPATH,"//a[normalize-space()='Spanish']"

    #add new patient form
    new_patient_button=By.CSS_SELECTOR,"a[id='addpip']"
    name_field=By.ID,"name"
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
    TPA_validity_field=By.NAME,"validity"
    national_identity_number_field=By.CSS_SELECTOR,"input[name='identification_number']"
    alternate_number_field=By.CSS_SELECTOR,"input[id='custom_fields[patient][3]']"
    addnewpatient_validalert=By.CSS_SELECTOR,"div[class='toast-message']"
    addnewpatient_invalidalert=By.CSS_SELECTOR,"div[class='toast-message'] p"

    #betstatus
    bed_145=By.LINK_TEXT,"FF - 145"
    bed_146=By.PARTIAL_LINK_TEXT,"146"
    Addmision_date=By.CSS_SELECTOR,"input[id='admission_date']"
    patientSelect_field=By.XPATH,"//span[@class='select2-selection select2-selection--single' and @aria-labelledby='select2-addpatient_id-container']"
    patientinput_field=By.CSS_SELECTOR,"input[class='select2-search__field']"
    consultant_select_field=By.XPATH,"//span[@class='select2-selection select2-selection--single' and @aria-labelledby='select2-consultant_doctor-container']"
    bed_status_save_button=By.CSS_SELECTOR,"button[id='formaddbtn']" 
    doctal_consultant_select=By.XPATH,"//select[@id='consultant_doctor']"
    add_patient_name=By.CSS_SELECTOR,".select2-results__option.select2-results__option--highlighted"
    
    #js locators
    add_patient_button="document.getElementById('addp').click()"
    save_button="document.getElementById('formaddpabtn').click()"
    delete_notification_button="document.getElementsByClassName('btn btn-primary btn-sm checkbox-toggle delete_all')[0].click()"

    #post-msg
    messaging_btn=By.XPATH,"//span[text()='Messaging']"
    post_new_message=By.XPATH,"(//a[@class='btn btn-primary btn-sm'])[1]"
    send_sms=By.XPATH," (//a[@class='btn btn-primary btn-sm'])[2]"

    title_locator = By.XPATH,'//div[@class="col-md-9"]//input[@name="title"]'
    notice_date  = By.XPATH,'(//input[@class="form-control date"])[1]'
    messaging_frame = By.XPATH,'//iframe[@class="wysihtml5-sandbox"]'   
    msg_body = By.XPATH,'//body[@class="form-control wysihtml5-editor"]'
    publish_on =  By.XPATH,'(//input[@class="form-control date"])[2]'
    send_btn =  By.XPATH,'(//div[@class="pull-right"])[2]/button'
    sucess_msg =  By.XPATH,'//div[@class="alert alert-success"]'
    verification_text= "Record Saved Successfully"

    #send_sms
    sms_title =By.XPATH,'//div[@class="form-group"]//input[@name="group_title"]'
    sms_template =By.XPATH,'//input[@name="group_template_id"]'   
    sms_checkbox  =By.XPATH,'(//label[@class="checkbox-inline"]/input)[1]' 
    text_area  =By.XPATH,' //textarea[@name="group_message"]'  
    send_sms_btn  =By.XPATH,'//button[@class="btn btn-primary submit_group"]'  
    admin_check_box  =By.XPATH,'(//input[@type="checkbox"])[4]'   
    doctor_check_box =By.XPATH,'(//input[@type="checkbox"])[6]'   
    Pathologist_check_box  =By.XPATH,'(//input[@type="checkbox"])[8]]'   
    Pharmacist_check_box  =By.XPATH,'(//input[@type="checkbox"])[7]'   
    assert_sms  =By.XPATH,'//div[@class="toast-message"]'   
    required_notice_date=By.XPATH,'(//span[@class="text-danger"])[3]'
    required_msg_body=By.XPATH,'(//span[@class="text-danger"])[2]'
    
    individual_msg=By.XPATH,'(//ul[@class="nav nav-tabs pull-right"]//a)[1]'
    individual_title=By.XPATH,'//input[@name="individual_title"]'
    sendthrough_check_box=By.XPATH,'(//input[@name="individual_send_by[]"])[1]'
    individual_text_area=By.XPATH,'//textarea[@id="individual_msg_text"]'
    individual_template_id=By.XPATH,'//input[@name="individual_template_id"]'
    sms_search_box=By.XPATH,'//input[@id="search-query"]'
    select_send_to=By.XPATH,'(//ul[@class="selector-list"]/li)[1]'
    add_button=By.XPATH,'//button[@class="btn btn-primary btn-searchsm add-btn"]'
    send_sms_individual=By.XPATH,'//button[@class="btn btn-primary submit_individual"]'
    select_msg_group=By.XPATH,'//div[@class="input-group-btn bs-dropdown-to-select-group"]/button'
    select_patient_droup=By.XPATH,'//ul[@class="dropdown-menu"]//a[text()="Patient"]'



    def click_Birth_and_death_record(self):
        try:
            self.for_click(self.wait_for_element(self.Birth_and_death_record))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_Birth_and_death_record: {str(e)}")   

    def click_birth_record(self):
        try:
            self.for_click(self.wait_for_element(self.Birth_record))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_birth_record: {str(e)}")

    def click_death_record(self):
        try:
            self.for_click(self.wait_for_element(self.Death_record))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_death_record: {str(e)}")    

    def click_add_death_record(self):
        try:
            self.for_click(self.wait_for_element(self.Add_death_record))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_add_death_record: {str(e)}")    
        
    def click_add_birth_record(self):
        try:
            self.for_click(self.wait_for_element(self.Add_birth_record))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_add_birth_record: {str(e)}")   

    def Enter_child_name(self,childname):
        try:
            element = self.wait_for_element(self.Child_name)
            self.for_send_keys(element, childname)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_child_name: {str(e)}")
    
    def click_gender(self):
        try:
            self.for_click(self.wait_for_element(self.Gender_drop_down))
            self.for_click(self.wait_for_element(self.Male_gender_option))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_gender: {str(e)}")
    
    def Enter_weight(self,weight):
        try:
            element = self.wait_for_element(self.weight)
            self.for_send_keys(element, weight)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_weight: {str(e)}")

    def Enter_birth_date(self,birthDate):
        try:
            element = self.wait_for_element(self.birth_date)
            self.for_send_keys(element, birthDate)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_birth_date: {str(e)}")

    def Enter_contact(self,phone):
        try:
            element = self.wait_for_element(self.contact)
            self.for_send_keys(element, phone)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_contact: {str(e)}") 
                        
    def Enter_address(self,address):
        try:
            element = self.wait_for_element(self.adress)
            self.for_send_keys(element, address)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_address: {str(e)}")

    def Enter_case_id(self,caseId):
        try:
            element = self.wait_for_element(self.case_id)
            self.for_send_keys(element, caseId)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_case_id: {str(e)}")

    def Enter_Father_name(self,fatherName):
        try:
            element = self.wait_for_element(self.fathers_name)
            self.for_send_keys(element, fatherName)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_Father_name: {str(e)}")

    def Enter_report(self,report):
        try:
            element = self.wait_for_element(self.birth_Report)
            self.for_send_keys(element, report)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_report: {str(e)}")

    def click_save_button(self):
        try:
            self.for_click(self.wait_for_element(self.save_button))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_save_button: {str(e)}")
    
    def Assert_patient_not_found(self):
        try:
            element=self.wait_for_element(self.patient_not_found).text
            assert element.eq("Patient Not Found")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_patient_not_found: {str(e)}")

    def Assert_empty_Field(self):
        try:
            element=self.wait_for_element(self.patient_not_found).text
            assert element.eq("Patient Not Found")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_empty_Field: {str(e)}")
        
    def Assert_variable_id(self):
        try:
            element=self.wait_for_element(self.patient_not_found).text
            assert element.eq("Case Id Not Valid")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_variable_id: {str(e)}")
    
    def Enter_death_date(self,deathDate):
        try:
            element = self.wait_for_element(self.death_date)
            self.for_send_keys(element, deathDate)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_death_date: {str(e)}")

    def Enter_death_report(self,deathreport):
        try:
            element = self.wait_for_element(self.death_report)
            self.for_send_keys(element, deathreport)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in Enter_death_report: {str(e)}")

    def Assert_death_Empty_record(self):
        try:
            element = self.wait_for_element(self.empty_assert).text
            assert element.eq("The Patient field is required.")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_death_Empty_record: {str(e)}")

    def search_record(self,record):
        try:
            element = self.wait_for_element(self.Search_record)
            self.for_send_keys(element,record)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in search_record: {str(e)}")

    def Assert_no_data_availble(self):
        try:
            element = self.wait_for_element(self.no_data_available).text
            assert element.eq("Add new record or search with different criteria.")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_no_data_availble: {str(e)}")

    def Assert_valid_birth_search_assert(self):
        try:
            element = self.wait_for_element(self.valid_birth_search_assert).text
            assert element.eq("BREF62")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_valid_birth_search_assert: {str(e)}")

    def Assert_valid_death_search_assert(self):
        try:
            element = self.wait_for_element(self.valid_death_search_assert).text
            assert element.eq("DREF50")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_valid_death_search_assert: {str(e)}")
        
    def successfull_update_of_the_bedstatus(self,patient_name):
        try:
            self.for_click(self.wait_for_element(self.betstatus_icon))
            self.for_click(self.wait_for_element(self.bed_145))
            self.for_click(self.wait_for_element(self.patientSelect_field))
            self.for_send_keys(self.wait_for_element(self.patientinput_field),patient_name)
            patient=self.wait_for_element(self.add_patient_name)
            self.action.move_to_element(patient).perform()
            self.action.click(patient).perform()
            self.for_click(self.wait_for_element(self.Addmision_date))
            select_element=self.wait_for_element(self.doctal_consultant_select)
            select=Select(select_element)
            select.select_by_value("11")
            self.for_click(self.wait_for_element(self.bed_status_save_button))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in successfull_update_of_the_bedstatus: {str(e)}")
    
    def verify_the_successfull_updation_of_the_bedstatus(self):
        try:
            toast_message_element = self.wait_for_element((By.CSS_SELECTOR, "div[class='toast-message']"))
            actual_message = toast_message_element.text
            print("Actual message:", actual_message)  
            expected_message = "Patient Added Successfully"
            assert actual_message == expected_message, f"Expected message: {expected_message}, Actual message: {actual_message}"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_the_successfull_updation_of_the_bedstatus: {str(e)}")


    def unsuccessfull_update_of_the_bedstatus_with_existing_patient(self,patient_name):
        try:
            self.for_click(self.wait_for_element(self.betstatus_icon))
            self.for_click(self.wait_for_element(self.bed_146))
            self.for_click(self.wait_for_element(self.patientSelect_field))
            self.for_send_keys(self.wait_for_element(self.patientinput_field),patient_name)
            patient=self.wait_for_element(self.add_patient_name)
            self.action.move_to_element(patient).perform()
            self.action.click(patient).perform()
            self.for_click(self.wait_for_element(self.Addmision_date))
            select_element=self.wait_for_element(self.doctal_consultant_select)
            select=Select(select_element)
            select.select_by_value("11")
            self.for_click(self.wait_for_element(self.bed_status_save_button))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in unsuccessfull_update_of_the_bedstatus_with_existing_patient: {str(e)}")
    
    def unsuccessfull_update_of_the_bedstatus_without_consultant(self,patient_name):
        try:
            self.action.click(self.wait_for_element(self.betstatus_icon)).perform()
            self.action.click(self.wait_for_element(self.bed_146)).perform()
            self.action.click(self.wait_for_element(self.patientSelect_field)).perform()
            self.for_send_keys(self.wait_for_element(self.patientinput_field),patient_name)
            self.action.click(self.wait_for_element(self.add_patient_name)).perform()
            self.action.click(self.wait_for_element(self.Addmision_date)).perform()
            self.action.click(self.wait_for_element(self.bed_status_save_button)).perform()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in unsuccessfull_update_of_the_bedstatus_without_consultant: {str(e)}")

    def unsuccessfull_update_of_the_bedstatus_without_appointment_date(self,patient_name):
        try:
            self.action.click(self.wait_for_element(self.betstatus_icon)).perform()
            self.for_click(self.wait_for_element(self.bed_146))
            self.for_click(self.wait_for_element(self.patientSelect_field))
            self.for_send_keys(self.wait_for_element(self.patientinput_field),patient_name)
            self.for_click(self.wait_for_element(self.add_patient_name))
            select_element=self.wait_for_element(self.doctal_consultant_select)
            select=Select(select_element)
            select.select_by_value("11")
            self.for_click(self.wait_for_element(self.bed_status_save_button))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in unsuccessfull_update_of_the_bedstatus_without_appointment_date: {str(e)}")

    def unsuccessfull_update_of_the_bedstatus_without_patient(self):
        try:
            self.action.click(self.wait_for_element(self.betstatus_icon)).perform()
            self.action.click(self.wait_for_element(self.bed_146)).perform()
            select_element=self.wait_for_element(self.doctal_consultant_select)
            select=Select(select_element)
            select.select_by_value("11")
            self.action.click(self.wait_for_element(self.bed_status_save_button)).perform()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in unsuccessfull_update_of_the_bedstatus_without_patient: {str(e)}")

    def verify_the_unsuccessfull_updation_of_the_bedstatus_without_patient(self):
        try:
            assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text=="The Patient field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_the_unsuccessfull_updation_of_the_bedstatus_without_patient: {str(e)}")
    
    def verify_the_unsuccessfull_updation_of_the_bedstatus_with_existing_patient(self):
        try:
            assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text=="Patient already in IPD"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_the_unsuccessfull_updation_of_the_bedstatus_with_existing_patient: {str(e)}")

    def verify_the_unsuccessfull_updation_of_the_bedstatus_without_consultant(self):
        try:
            assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text=="The Consultant Doctor field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_the_unsuccessfull_updation_of_the_bedstatus_without_consultant: {str(e)}")

    def verify_the_unsuccessfull_updation_of_the_bedstatus_without_appointment_date(self):
        try:
            assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text=="The Appointment Date field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_the_unsuccessfull_updation_of_the_bedstatus_without_appointment_date: {str(e)}")

    def successfull_notification_delete(self):
        try:
            self.click_elefunction(self.wait_for_element(self.notification_icon))
            self.getting_element(self.delete_notification_button)
            self.handle_alert()
        except (TimeoutException, NoSuchElementException,NoSuchWindowException) as e:
            print(f"Error in successfull_notification_delete: {str(e)}")

    def verify_successfull_notification_delete(self):
        try:
            self.action.click(self.wait_for_element(self.notification_icon)).perform()
            assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='alert alert-danger']"))).text=="No Record Found"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_successfull_notification_delete: {str(e)}")
    
    def go_to_new_patient_form(self):
        try:
            ipd_in_patient_element = self.wait_for_element(self.IPD_in_patient)
            self.action.move_to_element(ipd_in_patient_element).perform()
            self.action.click(ipd_in_patient_element).perform()
            self.getting_element(self.add_patient_button)
            new_patient_button_element = self.wait_for_element(self.new_patient_button)
            self.action.click(new_patient_button_element).perform()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in go_to_new_patient_form: {str(e)}")
    
    def fill_new_patient_form(self, patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number):
        try:
            self.type_text(self.wait_for_element(self.name_field), patient_name)
            self.type_text(self.wait_for_element(self.guardian_name_field), guardian_name)
            self.for_send_keys(self.wait_for_element(self.dob_field), dob)
            self.for_send_keys(self.wait_for_element(self.phone_number_field), phone_number)
            self.type_text(self.wait_for_element(self.email_field), email)
            self.type_text(self.wait_for_element(self.address_field), address)
            self.type_text(self.wait_for_element(self.known_allergies_field), known_allergies)
            self.for_send_keys(self.wait_for_element(self.TPA_ID_field), TPA_ID)
            self.type_text(self.wait_for_element(self.TPA_validity_field), TPA_Validity)
            self.for_send_keys(self.wait_for_element(self.national_identity_number_field), ni_number)
            self.for_send_keys(self.wait_for_element(self.alternate_number_field), alternate_number)
            self.getting_element(self.save_button)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_new_patient_form: {str(e)}")


    def verify_successfull_addnewpatient(self):
        try:
            result_element=self.wait_for_element(self.addnewpatient_validalert).text
            expected_text="Record Saved Successfully"
            print(result_element)
            assert result_element==expected_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_successfull_addnewpatient: {str(e)}")

        
    def verify_unsuccessfull_addnewpatient_without_patient_name(self):
        try:
            result_element=self.wait_for_element(self.addnewpatient_invalidalert).text
            expected_text="The Name field is required."
            print(result_element)
            assert result_element==expected_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsuccessfull_addnewpatient_without_patient_name: {str(e)}")


    def verify_unsuccessfull_addnewpatient_without_patient_age(self):
        try:
            result_element=self.wait_for_element(self.addnewpatient_invalidalert).text
            expected_text="The Age field is required.The Year field is required.The Month field is required.The Day field is required."
            print(result_element)
            assert result_element in expected_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsuccessfull_addnewpatient_without_patient_age: {str(e)}")


    def click_messaging_btn(self):
        try:
            self.scroll_upto_element(self.messaging_btn)
            self.for_click(self.wait_for_element(self.messaging_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in click_messaging_btn: {str(e)}")

    def fill_post_new_message_form(self,title,notification_date,publish_date,message_body):
        try:
            self.for_click(self.wait_for_element(self.post_new_message))
            self.for_send_keys(self.wait_for_element(self.title_locator),title)
            self.for_send_keys(self.wait_for_element(self.notice_date),notification_date)
            self.for_send_keys(self.wait_for_element(self.publish_on),publish_date)
            self._driver.switch_to.frame(self.wait_for_element(self.messaging_frame))
            self.for_send_keys(self.wait_for_element(self.msg_body),message_body)
            self._driver.switch_to.default_content()
            self.for_click(self.wait_for_element(self.send_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_post_new_message_form: {str(e)}")


    def verify_record_saved_successfully(self):
        try:
            self.wait_for_element(self.sucess_msg)
            search_result_text = self.wait_for_element(self.sucess_msg).text
            return search_result_text == self.verification_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_record_saved_successfully: {str(e)}")

    
    
    def verify_sms_record_saved_successfully(self):
        try:
            self.wait_for_element(self.assert_sms)
            search_result_text = self.wait_for_element(self.assert_sms).text
            return search_result_text == self.verification_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_sms_record_saved_successfully: {str(e)}")

    
    
    def fill_send_sms_form(self,title,template_id,sms_text):
        try:
            self.for_click(self.wait_for_element(self.send_sms))
            self.for_send_keys(self.wait_for_element(self.sms_title),title)
            self.for_send_keys(self.wait_for_element(self.sms_template),template_id)
            self.for_click(self.wait_for_element(self.sms_checkbox))
            self.for_send_keys(self.wait_for_element(self.text_area),sms_text)
            self.for_click(self.wait_for_element(self.admin_check_box))
            self.for_click(self.wait_for_element(self.doctor_check_box))
            self.for_click(self.wait_for_element(self.Pharmacist_check_box))
            self.for_click(self.wait_for_element(self.send_sms_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_send_sms_form: {str(e)}")

    

    def fill_send_sms_form_to_individual(self,Title,Template_id,Message_text):
        try:
            self.for_click(self.wait_for_element(self.send_sms))
            self.for_click(self.wait_for_element(self.individual_msg))
            self.for_send_keys(self.wait_for_element(self.individual_title),Title)
            self.for_click(self.wait_for_element(self.sendthrough_check_box))
            self.for_send_keys(self.wait_for_element(self.individual_template_id),Template_id)
            self.for_send_keys(self.wait_for_element(self.individual_text_area),Message_text)
            self.for_click(self.wait_for_element(self.select_msg_group))
            self.for_click(self.wait_for_element(self.select_patient_droup))
            self.for_click(self.wait_for_element(self.sms_search_box))
            self.for_send_keys(self.wait_for_element(self.sms_search_box),"Olivier")
            self.for_click(self.wait_for_element(self.select_send_to))
            self.for_click(self.wait_for_element(self.add_button))
            self.scroll_upto_element(self.send_sms_individual)
            self.for_click(self.wait_for_element(self.send_sms_individual))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_send_sms_form_to_individual: {str(e)}")

    

    def verify_sms_send_to_individual_patient(self):
        try:
            search_result_text = self.wait_for_element(self.assert_sms).text
            return search_result_text == "Message sent successfully"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_sms_send_to_individual_patient: {str(e)}")

    

    def verify_unsucessful_message_for_send_through_sms(self):
        try:
            search_result_text = self.wait_for_element(self.assert_sms).text
            return search_result_text == "The Send Through field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsucessful_message_for_send_through_sms: {str(e)}")

    
    def fill_send_sms_form_without_title(self,title,template_id,sms_text):
        try:
            self.for_click(self.wait_for_element(self.send_sms))
            self.for_send_keys(self.wait_for_element(self.sms_template),template_id)
            self.for_send_keys(self.wait_for_element(self.text_area),sms_text)
            self.for_click(self.wait_for_element(self.sms_checkbox))
            self.for_click(self.wait_for_element(self.admin_check_box))
            self.for_click(self.wait_for_element(self.Pharmacist_check_box))
            self.for_click(self.wait_for_element(self.send_sms_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_send_sms_form_without_title: {str(e)}")


    def verify_unsucessful_message_for_sms_title(self):
        try:
            search_result_text = self.wait_for_element(self.assert_sms).text
            return search_result_text == "The Title field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsucessful_message_for_sms_title: {str(e)}")

    def fill_post_new_message_form_with_invalid_notification_date(self,title,publish_date,message_body):
        try:
            self.for_click(self.wait_for_element(self.post_new_message))
            self.for_send_keys(self.wait_for_element(self.title_locator),title)
            self.for_send_keys(self.wait_for_element(self.publish_on),publish_date)
            self._driver.switch_to.frame(self.wait_for_element(self.messaging_frame))
            self.for_send_keys(self.wait_for_element(self.msg_body),message_body)
            self._driver.switch_to.default_content()
            self.for_click(self.wait_for_element(self.send_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_post_new_message_form_with_invalid_notification_date: {str(e)}")


    def verify_unsucessful_message_for_invalid_notification_date(self):
        try:
            search_result_text = self.wait_for_element(self.required_notice_date).text
            return search_result_text == "The Notice Date field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsucessful_message_for_invalid_notification_date: {str(e)}")


    def fill_post_new_message_form_with_no_message_body(self,title,notification_date,publish_date):
        try:
            self.for_click(self.wait_for_element(self.post_new_message))
            self.for_send_keys(self.wait_for_element(self.title_locator),title)
            self.for_send_keys(self.wait_for_element(self.notice_date),notification_date)
            self.for_send_keys(self.wait_for_element(self.publish_on),publish_date)
            self.for_click(self.wait_for_element(self.send_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_post_new_message_form_with_no_message_body: {str(e)}")

    def verify_unsucessful_message_for_invalid_message_body(self):
        try:
            self.scroll_upto_element(self.required_msg_body)
            search_result_text = self.wait_for_element(self.required_msg_body).text
            return search_result_text == "The Message field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsucessful_message_for_invalid_message_body: {str(e)}")

    
    def fill_send_sms_form_without_send_through(self,title,template_id,sms_text):
        try:
            self.for_click(self.wait_for_element(self.send_sms))
            self.for_send_keys(self.wait_for_element(self.sms_title),title)
            self.for_send_keys(self.wait_for_element(self.sms_template),template_id)
            self.for_send_keys(self.wait_for_element(self.text_area),sms_text)
            self.for_click(self.wait_for_element(self.admin_check_box))
            self.for_click(self.wait_for_element(self.doctor_check_box))
            self.for_click(self.wait_for_element(self.Pharmacist_check_box))
            self.for_click(self.wait_for_element(self.send_sms_btn))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error in fill_send_sms_form_without_send_through: {str(e)}")

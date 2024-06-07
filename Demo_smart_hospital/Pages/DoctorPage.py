from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from selenium.webdriver.support.ui import Select

class DoctorPage(BasePage):

    def init(self, driver):
        super()._init_(driver)
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
    add_patient_name=By.XPATH,"//li[@class='select2-results_option select2-results_option--highlighted']"

    
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
    def click_Birth_and_death_record(self):
        self.for_click(self.wait_for_element(self.Birth_and_death_record))   

    def click_birth_record(self):
        self.for_click(self.wait_for_element(self.Birth_record))   

    def click_death_record(self):
        self.for_click(self.wait_for_element(self.Death_record))   

    def click_add_death_record(self):
        self.for_click(self.wait_for_element(self.Add_death_record))   
        
    def click_add_birth_record(self):
        self.for_click(self.wait_for_element(self.Add_birth_record))   

    def Enter_child_name(self,childname):
        element = self.wait_for_element(self.Child_name)
        self.for_send_keys(element, childname)
      
    def click_gender(self):
        self.for_click(self.wait_for_element(self.Gender_drop_down))
        self.for_click(self.wait_for_element(self.Male_gender_option))
    
    def Enter_weight(self,weight):
        element = self.wait_for_element(self.weight)
        self.for_send_keys(element, weight)

    def Enter_birth_date(self,birthDate):
        element = self.wait_for_element(self.birth_date)
        self.for_send_keys(element, birthDate)

    def Enter_contact(self,phone):
        element = self.wait_for_element(self.contact)
        self.for_send_keys(element, phone)
                           
    def Enter_address(self,address):
        element = self.wait_for_element(self.adress)
        self.for_send_keys(element, address)

    def Enter_case_id(self,caseId):
        element = self.wait_for_element(self.case_id)
        self.for_send_keys(element, caseId)

    def Enter_Father_name(self,fatherName):
        element = self.wait_for_element(self.fathers_name)
        self.for_send_keys(element, fatherName)

    def Enter_report(self,report):
        element = self.wait_for_element(self.birth_Report)
        self.for_send_keys(element, report)

    def click_save_button(self):
        self.for_click(self.wait_for_element(self.save_button))
      
    def Assert_patient_not_found(self):
        element=self.wait_for_element(self.patient_not_found).text
        assert element.eq("Patient Not Found")

    def Assert_empty_Field(self):
        element=self.wait_for_element(self.patient_not_found).text
        assert element.eq("Patient Not Found")
        
    def Assert_variable_id(self):
        element=self.wait_for_element(self.patient_not_found).text
        assert element.eq("Case Id Not Valid")
    
    def Enter_death_date(self,deathDate):
        element = self.wait_for_element(self.death_date)
        self.for_send_keys(element, deathDate)

    def Enter_death_report(self,deathreport):
        element = self.wait_for_element(self.death_report)
        self.for_send_keys(element, deathreport)

    def Assert_death_Empty_record(self):
        element = self.wait_for_element(self.empty_assert).text
        assert element.eq("The Patient field is required.")

    def search_record(self,record):
        element = self.wait_for_element(self.Search_record)
        self.for_send_keys(element,record)

    def Assert_no_data_availble(self):
        element = self.wait_for_element(self.no_data_available).text
        assert element.eq("Add new record or search with different criteria.")

    def Assert_valid_birth_search_assert(self):
        element = self.wait_for_element(self.valid_birth_search_assert).text
        assert element.eq("BREF62")

    def Assert_valid_death_search_assert(self):
        element = self.wait_for_element(self.valid_death_search_assert).text
        assert element.eq("DREF50")
        
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
        assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text=="Patient Added Successfully"
    
    def unsuccessfull_update_of_the_bedstatus(self):
        self.for_click(self.wait_for_element(self.betstatus_icon))
        self.for_click(self.wait_for_element(self.bed_145))
        self.for_click(self.wait_for_element(self.patientSelect_field))
        self.for_send_keys(self.wait_for_element(self.patientinput_field),"Jamesh Wood")
        self.for_click(self.wait_for_element(self.add_patient_name))
        self.for_click(self.wait_for_element(self.Addmision_date))
        select_element=self.wait_for_element(self.doctal_consultant_select)
        select=Select(select_element)
        select.select_by_value("11")
        self.for_click(self.wait_for_element(self.bed_status_save_button))
    
    def verify_the_unsuccessfull_updation_of_the_bedstatus(self):
        assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='toast-message']"))).text!="Patient Added Successfully"
    
    def successfull_notification_delete(self):
        self.for_click(self.wait_for_element(self.notification_icon))
        self.for_click(self.wait_for_element(self.delete_notification_button))
        self.handle_alert()
    
    def verify_successfull_notification_delete(self):
        self.for_click(self.wait_for_element(self.notification_icon))
        assert (self.wait_for_element((By.CSS_SELECTOR,"div[class='alert alert-danger']"))).text=="No Record Found"
    
    def go_to_new_patient_form(self):
        self.for_click(self.wait_for_element(self.IPD_in_patient))
        self.for_click(self.wait_for_element(self.add_patient_button))
        self.for_click(self.wait_for_element(self.new_patient_button))
        
    def fill_new_patient_form(self,patient_name, guardian_name, dob, bloodgroup, marital_status, phone_number, email, address, known_allergies, TPA_ID, TPA_Validity, ni_number, alternate_number):
        self.for_send_keys(self.wait_for_element(self.name_field),patient_name)
        self.for_send_keys(self.wait_for_element(self.guardian_name_field),guardian_name)
        self.for_send_keys(self.wait_for_element(self.dob_field),dob)
        self.for_send_keys(self.wait_for_element(self.phone_number_field),phone_number)
        self.for_send_keys(self.wait_for_element(self.email_field),email)
        self.for_send_keys(self.wait_for_element(self.address_field),address)
        self.for_send_keys(self.wait_for_element(self.known_allergies_field),known_allergies)
        self.for_send_keys(self.wait_for_element(self.TPA_ID_field),TPA_ID)
        self.for_send_keys(self.wait_for_element(self.TPA_validity_field),TPA_Validity)
        self.for_send_keys(self.wait_for_element(self.national_identity_number_field),ni_number)
        self.for_send_keys(self.wait_for_element(self.alternate_number_field),alternate_number)
        self.for_click(self.wait_for_element(self.save_button))
    
    def verify_successfull_addnewpatient(self):
        result_element=self.wait_for_element(self.addnewpatient_validalert).text
        expected_text="Record Saved Successfully"
        assert result_element==expected_text
    
    def verify_unsuccessfull_addnewpatient(self):
        result_element=self.wait_for_element(self.addnewpatient_invalidalert).text
        expected_text="The Name field is required."
        assert result_element==expected_text

    def click_messaging_btn(self):
        self.scroll_upto_element(self.messaging_btn)
        self.for_click(self.wait_for_element(self.messaging_btn))

    def fill_post_new_message_form(self):
        self.for_click(self.wait_for_element(self.post_new_message))
        self.for_send_keys(self.wait_for_element(self.title_locator),"Hii all")
        self.for_send_keys(self.wait_for_element(self.notice_date),"25/06/2024")
        self.for_send_keys(self.wait_for_element(self.publish_on),"30/06/2024")
        self._driver.switch_to.frame(self.wait_for_element(self.messaging_frame))
        self.for_send_keys(self.wait_for_element(self.msg_body),"sample message to all")
        self._driver.switch_to.default_content()
        self.for_click(self.wait_for_element(self.send_btn))

    def verify_record_saved_successfully(self):
        self.wait_for_element(self.sucess_msg)
        search_result_text = self.wait_for_element(self.sucess_msg).text
        return search_result_text == self.verification_text
    
    
    def verify_sms_record_saved_successfully(self):
        self.wait_for_element(self.assert_sms)
        search_result_text = self.wait_for_element(self.assert_sms).text
        return search_result_text == self.verification_text
    
    
    def fill_send_sms_form(self):
        self.for_click(self.wait_for_element(self.send_sms))
        self.for_send_keys(self.wait_for_element(self.sms_title),"Hiii")
        self.for_send_keys(self.wait_for_element(self.sms_template),"0001")
        self.for_click(self.wait_for_element(self.sms_checkbox))
        self.for_send_keys(self.wait_for_element(self.text_area),"hello everyone")
        self.for_click(self.wait_for_element(self.admin_check_box))
        self.for_click(self.wait_for_element(self.doctor_check_box))
        self.for_click(self.wait_for_element(self.Pharmacist_check_box))
        self.for_click(self.wait_for_element(self.send_sms_btn))
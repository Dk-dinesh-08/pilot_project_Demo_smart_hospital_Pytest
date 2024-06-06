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
    
    def successfull_update_of_the_bedstatus(self):
        self.click_element(self.betstatus_icon)
        self.click_element(self.bed_145)
        self.click_element(self.patientSelect_field)
        self.for_send_keys(self.patientinput_field,"Elvio")
        self.click_element(self.add_patient_name)
        self.click_element(self.Addmision_date)
        select_element=self.find(self.doctal_consultant_select)
        select=Select(select_element)
        select.select_by_value("11")
        self.click_element(self.bed_status_save_button)
        
    def verify_the_successfull_updation_of_the_bedstatus(self):
        return self.find_element_text((By.CSS_SELECTOR,"div[class='toast-message']"))

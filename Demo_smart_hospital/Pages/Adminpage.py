import pytest
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("test_setup_and_teardown")
class AdminPage(BasePage):  

    appointment_link=By.XPATH,'//ul[@class="sidebar-menu verttop"]//li[3]/a'
    doctor_wise_appionment_btn=By.XPATH,'//a[@class="btn btn-primary btn-sm"][1]'
    date_locator=By.XPATH,'//input[@name="date"]'
    doctor_field=By.XPATH,'//span[@class="select2-selection__rendered"]'
    select_doctor_option=By.XPATH,"//ul[@class='select2-results__options']/li[contains(text(),'Amit  Singh (9009)')]"
    search_button=By.XPATH,'//button[@class="btn btn-primary btn-sm pull-right"]'
    doctor_name="Sonia Bush (9002)"
    date_entry="05/16/2024"
    verify_text="Records: 1 to 1 of 1"
    search_result =By.XPATH,'//div[@class="dataTables_info"]'  
    admin_login_btn =By.XPATH,' //i[@class="fa fa-user ispace"]//parent::a'
    queue_search_button=By.XPATH,'//a[@class="btn btn-primary btn-sm"][2]'
    doctor_locator=By.XPATH, "//div[@class='form-group']//select[@id='doctor']"
    queue_search=By.XPATH,'//button[@class="btn btn-primary btn-sm"]'
    select_shift="Morning"
    select_slot="06:00 AM - 09:00 AM"                                          
    shift_locator=By.XPATH, "//div[@class='form-group']//select[@id='global_shift']"
    slot_locator=By.XPATH,"//div[@class='form-group']//select[@class='form-control']"
    slot_option=By.XPATH,"//select[@id='slot']//option[2]"


    patient_search=By.XPATH,'//input[@class="form-control search-form search-form3"]'
    patient_search_button=By.XPATH,'(//button[@class="btn btn-flat"]/i)[1]'
    table_value=By.XPATH,'(//a[@class="btn btn-default btn-xs"])[1]'
    patient_name="Ananya Sarma "
    patient_search_result=By.XPATH,'//a[text()="Ananya Sarma (1070)"]'
    expected_search_text="Ananya Sarma (1070)"
    invalid_patient_name="@123"
    invalid_search_result=By.XPATH,'//div[@id="DataTables_Table_0_info"]'
    invalid_patient_search_text="Records: 0 to 0 of 0"

    inventory=By.XPATH,'//i[@class="fas fa-luggage-cart"]//parent::a'
    add_item_stock=By.XPATH,'//a[@class="btn btn-primary btn-sm additemstock"]'
    item_category=By.XPATH,'(//div[@class="form-group"])[1]//select[@name="item_category_id"]'
    item=By.XPATH,'(//div[@class="form-group"])[2]//select[@name="item_id"]'
    store=By.XPATH,'(//div[@class="form-group"])[4]//select[@name="store_id"]'
    supplier=By.XPATH,'(//div[@class="form-group"])[3]//select[@name="supplier_id"]'
    quantity=By.XPATH,'(//input[@class="form-control miplusinput"])[1]'
    puchase_price=By.XPATH,'(//input[@name="purchase_price"])[1]'
    save_btn=By.XPATH,'//button[@id="form1btn"]'
    table_result=By.XPATH,'//table[@id="DataTables_Table_0"]//tbody/tr[@class="odd"][1]/td/a'

    verify_invalid_login=(By.XPATH,"//div[@class='alert alert-danger']")
    verification_text="Invalid Username or Password"


    invalid_search_loc=  By.XPATH,'(//span[@class="text-danger"])[1]'    
    invalid_search_text= "The Doctor field is required."

    invalid_slot_field=By.XPATH,'(//span[@class="text-danger"])[4]'
    invalid_slot_field_text="The Slot field is required."


    def __init__(self, driver):
        super().__init__(driver)


    def fill_queue_searchform(self,):
        self.select_element_by_visible_text(self.doctor_locator,self.doctor_name)
        self.select_element_by_visible_text(self.shift_locator,self.select_shift)
        self.for_send_keys(self.wait_for_element(self.date_locator),self.date_entry)
        self.for_click(self.wait_for_element(self.slot_locator))
        self.for_click(self.wait_for_element(self.slot_option))
        self.for_click(self.wait_for_element(self.queue_search))
       
    def fill_queue_searchform_with_invalid_details(self,):
        self.select_element_by_visible_text(self.doctor_locator,self.doctor_name)
        self.select_element_by_visible_text(self.shift_locator,self.select_shift)
        self.for_send_keys(self.wait_for_element(self.date_locator),self.date_entry)
        self.for_click(self.wait_for_element(self.queue_search))


    def click_doctor_wise_appointment_search(self):
        self.for_click(self.wait_for_element(self.appointment_link))
        self.for_click(self.wait_for_element(self.doctor_wise_appionment_btn))

    def click_queue_search(self):
        self.for_click(self.wait_for_element(self.appointment_link))
        self.for_click(self.wait_for_element(self.queue_search_button))

    def fill_doctorwise_search_form(self):
        
        self.for_click(self.wait_for_element(self.doctor_field))
        self.for_click(self.wait_for_element(self.select_doctor_option))
        self.for_send_keys(self.wait_for_element(self.date_locator),self.date_entry)
        self.for_click(self.wait_for_element(self.search_button))
    

    def fill_doctorwise_search_form_without_doctor_field(self):
        self.for_send_keys(self.wait_for_element(self.date_locator),self.date_entry)
        self.for_click(self.wait_for_element(self.search_button))
        


    def verify_search_results(self):
        self.wait_for_element(self.search_result)
        search_result_text = self.wait_for_element(self.search_result).text
        return search_result_text == self.verify_text
    
    def verify_invalid_search_results(self):
        self.wait_for_element(self.invalid_search_loc)
        search_result_text = self.wait_for_element(self.invalid_search_loc).text
        return search_result_text == self.invalid_search_text
    

    def enter_patient_name(self):
        self.for_send_keys(self.wait_for_element(self.patient_search),self.patient_name)
        self.for_click(self.wait_for_element(self.patient_search_button))

    def verify_patient_search_result(self):
        search_result_text = self.wait_for_element(self.patient_search_result).text
        return search_result_text == self.expected_search_text
    
    def enter_invalid_patient_name(self):
        self.for_send_keys(self.wait_for_element(self.patient_search),self.invalid_patient_name)
        self.for_click(self.wait_for_element(self.patient_search_button))

    def verify_invalid_patient_search_result(self):
        search_result_text = (self.wait_for_element(self.invalid_search_result)).text
        return search_result_text == self.invalid_patient_search_text
    
    def click_inventory_button(self):
        self.scroll_upto_element(self.inventory)
        self.for_click(self.wait_for_element(self.inventory))
        self.for_click(self.wait_for_element(self.add_item_stock))
    
    def fill_add_stock_item_form(self):
        self.for_send_keys(self.wait_for_element(self.item_category),"Bed Sheets")
        self.select_element_by_visible_text(self.item,"Bed Sheet")
        self.for_send_keys(self.wait_for_element(self.supplier),"VK Supplier")
        self.for_send_keys(self.wait_for_element(self.store),"Vinay Pharmacy")
        self.for_send_keys(self.wait_for_element(self.quantity),"13")
        self.for_send_keys(self.wait_for_element(self.puchase_price),"250")
        self.for_click(self.wait_for_element(self.save_btn))
       
    def verify_successful_additionof_stock(self):
        search_result_text = self.wait_for_element(self.table_result).text
        return search_result_text == "Bed Sheet"
    
    def verify_invalid_admin_login(self):
        search_result_text = self.wait_for_element(self.verify_invalid_login).text
        return search_result_text == self.verification_text
    
    def verify_invalid_queue_search_result(self):
        search_result_text = self.wait_for_element(self.invalid_slot_field).text
        return search_result_text == self.invalid_slot_field_text
import pytest
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utility import Consolelogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException



log=Consolelogger.get_logger()

@pytest.mark.usefixtures("test_setup_and_teardown")


class AdminPage(BasePage):  

    def __init__(self, driver):
        super().__init__(driver)

    
    appointment_link=By.XPATH,'//ul[@class="sidebar-menu verttop"]//li[3]/a'
    doctor_wise_appionment_btn=By.XPATH,'//a[@class="btn btn-primary btn-sm"][1]'
    date_locator='input[name="date"]'
    doctor_field=By.XPATH,'//span[@id="select2-doctor-container"]'
    select_doctor_option=By.XPATH,"//ul[@class='select2-results__options']/li[contains(text(),'Amit  Singh (9009)')]"
    search_button=By.XPATH,'//button[@class="btn btn-primary btn-sm pull-right"]'
    search_result =By.XPATH,'//div[@class="dataTables_info"]'  
    admin_login_btn =By.XPATH,' //i[@class="fa fa-user ispace"]//parent::a'
    queue_search_button=By.XPATH,'//a[@class="btn btn-primary btn-sm"][2]'
    doctor_locator=By.XPATH, "//div[@class='form-group']//select[@id='doctor']"
    queue_search=By.XPATH,'//button[@class="btn btn-primary btn-sm"]'
                                       
    shift_locator=By.XPATH, "//div[@class='form-group']//select[@id='global_shift']"
    slot_locator=(By.XPATH,"//div[@class='form-group']//select[@class='form-control']")
    slot_option=(By.XPATH,"//select[@id='slot']//option[2]")
    queue_date_locator=By.XPATH,'//input[@name="date"]'


    patient_search=By.XPATH,'//input[@class="form-control search-form search-form3"]'
    patient_search_button=By.XPATH,'(//button[@class="btn btn-flat"]/i)[1]'
    table_value=By.XPATH,'(//a[@class="btn btn-default btn-xs"])[1]'
    patient_search_result=By.XPATH,'//a[text()="Ananya Sarma (1070)"]'
    invalid_search_result=By.XPATH,'//div[@id="DataTables_Table_0_info"]'

    inventory=By.XPATH,'//i[@class="fas fa-luggage-cart"]//parent::a'
    add_item_stock=By.XPATH,'//a[@class="btn btn-primary btn-sm additemstock"]'
    item_category=By.XPATH,'//form[@id="form1"]//select[@name="item_category_id"]'
    item=By.XPATH,'(//div[@class="form-group"])[2]//select[@name="item_id"]'
    store=By.XPATH,'(//div[@class="form-group"])[4]//select[@name="store_id"]'
    supplier=By.XPATH,'(//div[@class="form-group"])[3]//select[@name="supplier_id"]'
    quantity=By.XPATH,'(//input[@class="form-control miplusinput"])[1]'
    puchase_price=By.ID,'purchase_price'
    save_btn=By.XPATH,'//button[@id="form1btn"]'
    table_result=By.XPATH,'//table[@id="DataTables_Table_0"]//tbody/tr[@class="odd"][1]/td/a'
    assert_suppiler_required=By.XPATH,'//div[@class="toast-message"]'

    verify_invalid_login=(By.XPATH,"//div[@class='alert alert-danger']")
    invalid_search_loc=  By.XPATH,'(//span[@class="text-danger"])[1]'    
    invalid_slot_field=By.XPATH,'(//span[@class="text-danger"])[4]'
    incorrect_admin_login=By.CSS_SELECTOR,'div[class="alert alert-danger"]'
    required_username_field=By.XPATH,'(//span[@class="text-danger"])[1]'
    required_password_field=By.XPATH,'(//span[@class="text-danger"])[2]'

    


    def queue_select_slot(self,element):
        try:
            slot_element = self.wait_for_element(element)
            self.action.move_to_element(slot_element).click().perform()
            customOption = self._driver.find_element(By.XPATH, value="//option[text()='06:00 AM - 07:00 AM']")
            self.for_click(customOption)
        except  (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in select_slot: {e}")
    
    def fill_queue_searchform(self,doctor_name,select_shift,date_entry):
        try:
            self.select_element_by_visible_text(self.doctor_locator,doctor_name)
            self.select_element_by_visible_text(self.shift_locator,select_shift)
            self.for_send_keys(self.wait_for_element(self.queue_date_locator),date_entry)
            self.queue_select_slot(self.slot_locator)
            self.click_elefunction(self.wait_for_element(self.queue_search))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in queue search form: {e}")

       
    def fill_queue_searchform_with_invalid_details(self,doctor_name,select_shift,date_entry):
        try:
            self.select_element_by_visible_text(self.doctor_locator,doctor_name)
            self.select_element_by_visible_text(self.shift_locator,select_shift)
            self.for_send_keys(self.wait_for_element(self.queue_date_locator),date_entry)
            self.click_elefunction(self.wait_for_element(self.queue_search))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in fill_queue_searchform_with_invalid_details: {e}")


    def click_doctor_wise_appointment_search(self):
        try:
            self.click_elefunction(self.wait_for_element(self.appointment_link))
            self.click_elefunction(self.wait_for_element(self.doctor_wise_appionment_btn))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in click_doctor_wise_appointment_search: {e}")


    def click_queue_search(self):
        try:
            self.click_elefunction(self.wait_for_element(self.appointment_link))
            self.click_elefunction(self.wait_for_element(self.queue_search_button))

        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in click_queue_search: {e}")


    def fill_doctorwise_search_form(self,date_entry):
        try:
            self.action.move_to_element(self.wait_for_element(self.doctor_field)).perform()
            self.action.click(self.wait_for_element(self.doctor_field)).perform()
            self.action.click(self.wait_for_element(self.select_doctor_option)).perform()
            self.enter_date_in_appointment_search(self.date_locator,date_entry)
            self.action.click(self.wait_for_element(self.search_button)).perform()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in fill_doctorwise_search_form: {e}")
    

    def fill_doctorwise_search_form_without_doctor_field(self,date_entry):
        try:
            self.enter_date_in_appointment_search(self.date_locator,date_entry)
            self.action.click(self.wait_for_element(self.search_button)).perform()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in fill_doctorwise_search_form_without_doctor_field: {e}")
        

    def verify_search_results(self,verify_text):
        try:
            search_result_text = self.wait_for_element(self.search_result).text
            return search_result_text == verify_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying verifying the search results: {str(e)}")

    def verify_invalid_search_results(self,invalid_search_text):
        try:
            search_result_text = self.wait_for_element(self.invalid_search_loc).text
            return search_result_text == invalid_search_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying invalid sarch results: {str(e)}")


    def enter_patient_name(self,patient_name):
        try:
            self.type_text(self.wait_for_element(self.patient_search),patient_name)
            self.click_elefunction(self.wait_for_element(self.patient_search_button))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
           log.error(f"Error in entering the patient name: {str(e)}")

    def verify_patient_search_result(self,expected_search_text):
        try:
            search_result_text = self.wait_for_element(self.patient_search_result).text
            return search_result_text == expected_search_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying the patient search result: {str(e)}")

    def enter_invalid_patient_name(self,invalid_patient_name):
        try:
            self.for_send_keys(self.wait_for_element(self.patient_search),invalid_patient_name)
            self.action.click(self.wait_for_element(self.patient_search_button)).perform()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in entering invalid patient name: {str(e)}")

    def verify_invalid_patient_search_result(self,invalid_patient_search_text):
        try:
            search_result_text = (self.wait_for_element(self.invalid_search_result)).text
            return search_result_text == invalid_patient_search_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying invalid patient search result: {str(e)}")

    def click_inventory_button(self):
        try:
            self.scroll_upto_element(self.inventory)
            self.click_elefunction(self.wait_for_element(self.inventory))
            self.click_elefunction(self.wait_for_element(self.add_item_stock))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in clicking the inventory button: {str(e)}")

    def fill_add_stock_item_form(self,ItemCategory,Item,Supplier,Store,Quantity,Price):
        try:
            self.select_element_by_visible_text(self.item_category,ItemCategory)
            self.select_element_by_visible_text(self.item,Item)
            self.select_element_by_visible_text(self.supplier,Supplier)
            self.select_element_by_visible_text(self.store, Store)
            self.type_text(self.wait_for_element(self.quantity), Quantity)
            self.type_text(self.wait_for_element(self.puchase_price), Price)
            self._driver.execute_script("document.getElementById('form1btn').click();")
           
        except ElementNotInteractableException:
            log.error("Select Element is not interactable")
        except Exception as e:
            log.error(f"Error in fill_add_stock_item_form: {str(e)}")

    def fill_add_stock_item_form_with_invalid_supplier(self,ItemCategory,Item,Supplier,Store,Quantity,Price):
        try:
            self.for_click(self.wait_for_element(self.item_category))
            self.select_element_by_visible_text(self.item_category,ItemCategory)
            self.select_element_by_visible_text(self.item,Item)
            self.select_element_by_visible_text(self.store,Store)
            self.type_text(self.wait_for_element(self.quantity),Quantity)
            self.type_text(self.wait_for_element(self.puchase_price),Price)
            self._driver.execute_script("document.getElementById('form1btn').click();")
        except Exception as e:
            log.error(f"Error in fill_add_stock_item_form_with_invalid_supplier: {str(e)}")


    def verify_supplier_field_required_msg_in_additionof_stock(self):
        try:
            self.wait_for_element(self.table_result)
            search_result_text = (self.wait_for_element(self.assert_suppiler_required)).text
            return search_result_text == "The Supplier field is required."
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in  verifying the supplier field required msg in additionof stock: {str(e)}")

    def verify_stock_list_page_opens(self,url):
        try:
            page_url = str(self._driver.execute_script("return document.URL"))
            return page_url.__eq__(url)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying stock list page opens : {str(e)}")

    def verify_invalid_admin_login(self):
        try:
            search_result_text = self.wait_for_element(self.verify_invalid_login).text
            return search_result_text == self.verification_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
           log.error(f"Error in verifying invalid admin login: {str(e)}")

    def verify_invalid_queue_search_result(self,invalid_slot_field_text):
        try:
            search_result_text = self.wait_for_element(self.invalid_slot_field).text
            return search_result_text == invalid_slot_field_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
           log.error(f"Error in verifying invalid queue search result: {str(e)}")


    def verify_incorrect_admin_login(self,incorrect_admin_login_txt):
        try:
            search_result_text = self.wait_for_element(self.incorrect_admin_login).text
            return search_result_text == incorrect_admin_login_txt
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
           log.error(f"Error in verifying incorrect_admin_login: {str(e)}")

    def verify_login_with_blank_username_and_valid_password(self,required_username_text):
        try:
            search_result_text = self.wait_for_element(self.required_username_field).text
            return search_result_text == required_username_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
           log.error(f"Error in verifying login_with_blank_username_and_valid_password: {str(e)}")

    
    def verify_login_with_valid_username_and_blank_password(self,required_password_text):
        try:
            search_result_text = self.wait_for_element(self.required_password_field).text
            return search_result_text == required_password_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying the login with valid username and blank password: {str(e)}")

    def verify_login_with_blank_username_and_blank_password(self,required_username_text,required_password_text):
        try:
            search_result_text_username = self.wait_for_element(self.required_username_field).text
            search_result_text_password = self.wait_for_element(self.required_password_field).text
            assert search_result_text_username == required_username_text
            assert search_result_text_password == required_password_text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Error in verifying the login with blank username and blank password : {str(e)}")


    def enter_date_in_appointment_search(self,date_locator,date_entry):
        try:
            self._driver.execute_script(f"document.querySelector('{date_locator}').value = '{date_entry}';")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
             log.error(f"Error in entering date in appointment earch: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.Basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

class UserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    User_my_appointment = (By.CSS_SELECTOR, "i[class='fas fa-hospital-alt']+span")
    User_appointment_search = (By.CSS_SELECTOR, "input[type='search']")
    table_xpath = (By.XPATH, "//div[@id='DataTables_Table_0_wrapper']//table")
    next_page_button = (By.CSS_SELECTOR, "a[class='paginate_button next']>i[class='fa fa-angle-right']")
    user_assert_search = (By.XPATH, "//td[contains(text(),'APPNO6234')]")
    no_data_availbale_assert = (By.CSS_SELECTOR,"td[class='dataTables_empty']")
    Add_appointment_search = (By.CSS_SELECTOR,"div[class='box-tools pull-right']>a")
    Add_appointment_button = (By.CSS_SELECTOR,"div[class='box-tools pull-right']>a")
    User_Appointment_date = (By.ID,"dates")
    User_Appointment_speacilist = (By.ID,"specialist")
    User_Appointment_Doctor = (By.ID,"doctor")
    User_Appointment_Shift_feild = (By.XPATH,"(//select[@class='form-control select2'])[1]")
    User_Appointment_slot = (By.ID,"shift_id")
    User_Appointment_priority = (By.NAME,"priority")
    User_Appointment_Message = (By.ID,"message")
    User_Appointment_live_consultant = (By.ID,"live_consult")                    
    User_Appointemnt_Adress = (By.XPATH,"//textarea[@name='custom_fields[appointment][4]']")
    User_Available_slots = (By.ID,"slot_0")
    User_Appointment_save_button = (By.ID,"formaddbtn")
    user_Appointment_pay_button = (By.XPATH,"(//a[@class='btn btn-info btn-xs']/i)[1]")
    user_Appointment_pay_with_card = (By.CSS_SELECTOR,"button[class='stripe-button-el']")
    user_Appointment_payment_email = (By.ID,"email")
    user_Appointment_payment_Card = (By.ID,"card_number")  
    user_Appointment_payment_month_year = (By.CSS_SELECTOR,"input[placeholder='MM / YY']")  
    user_Appointment_payment_cvv = (By.CSS_SELECTOR,"input[placeholder='CVC']")  
    user_Appointment_payment_pincode = (By.ID,"billing-zip")
    user_Appointment_payment_pay_button = (By.CLASS_NAME,"iconTick")
    user_Appointment_status = (By.XPATH,"//th[@aria-controls='DataTables_Table_0' and text()='Status']")
    user_Appointment_delete_button = (By.CSS_SELECTOR,"i[class='fa fa-trash']")
    user_Appointment_assert=(By.XPATH,"(//div[@class='toast-message']/p)[1]")
    payment_frame = (By.CLASS_NAME,"stripe_checkout_app")

    pharmacy_bill_search_field = (By.CSS_SELECTOR,"input[type='search']")
    show_field = (By.CSS_SELECTOR,"i[class='fa fa-reorder']")
    pay_button = (By.CSS_SELECTOR,"button[class='btn btn-primary btn-xs']")
    view_payment_option = (By.CSS_SELECTOR,"a[class='btn btn-default view_payment btn-xs']")
    payment_amount_field = (By.CSS_SELECTOR,"input[id='amount_total_paid']")
    add_pay_button = (By.CSS_SELECTOR,"button[id='pay_button']")
    paywithcard_button = (By.CSS_SELECTOR,"button[class='stripe-button-el']")
    payment_email_field = (By.CSS_SELECTOR,"div[class='emailInput input'] input[id='email']")
    payment_cardnumber_field = (By.CSS_SELECTOR,"input[id='card_number']")
    card_expiry_date_field = (By.CSS_SELECTOR,"input[id='cc-exp']")
    card_cvv_field = (By.CSS_SELECTOR,"input[id='cc-csc']")
    final_pay_button = (By.CSS_SELECTOR,"button[id='submitButton']")
    pharmacy_option = (By.XPATH,"//i[@class='fas fa-mortar-pestle']//parent::a")
    pharmacy_bill_record_assert = (By.CSS_SELECTOR,"div[id='DataTables_Table_0_info']")
    pharmacy_view_details = (By.XPATH,"//a[@class='btn btn-default btn-xs']")
    view_detail_assert = (By.XPATH,"//h5[text()='Bill No : PHARMAB307']")
    norecord = (By.XPATH,"//td[@class='dataTables_empty']")
    card_pincode = (By.CSS_SELECTOR,"input[id='billing-zip']")
    bill_records = (By.XPATH,"//tbody//tr[@role='row']")

    def test_next_page_button(self):
        try:
            element = self.wait_for_element(self.next_page_button)
            self.click_elefunction(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in test_next_page_button: {str(e)}")

    def test_search_record(self, searchRecord):
        try:
            element = self.wait_for_element(self.User_appointment_search)
            self.type_text(element, searchRecord)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in test_search_record: {str(e)}")

    def click_user_appointment(self):
        try:
            element = self.wait_for_element(self.User_my_appointment)
            self.click_elefunction(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_user_appointment: {str(e)}")

    def Assert_search_Appointment(self):
        try:
            element = self.wait_for_element(self.user_assert_search).text
            element = element.strip()
            expected_text = "APPNO6234"
            assert element == expected_text, f"Expected '{expected_text}', but got '{element}'"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Assert_search_Appointment: {str(e)}")

    def Invalid_Assert_search_Appointment(self):
        try:
            element = self.wait_for_element(self.no_data_availbale_assert).text
            assert element == "No matching records found"
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Invalid_Assert_search_Appointment: {str(e)}")

    def Click_usert_Add_appointment(self):
        try:
            element = self.wait_for_element(self.Add_appointment_search)
            self.for_click(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Click_usert_Add_appointment: {str(e)}")

    def Click_Add_appointment(self):
        try:
            element = self.wait_for_element(self.Add_appointment_button)
            self.click_elefunction(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Click_Add_appointment: {str(e)}")

    def Enter_user_date(self, date):
        try:
            self.driver.execute_script(f"document.getElementById('dates').value = '{date}'")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in enter_user_date: {str(e)}")

    def Enter_Specialist(self):
        try:
            element = self.wait_for_element(self.User_Appointment_speacilist)
            select = Select(element)
            select.select_by_index(2)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_Specialist: {str(e)}")

    def Enter_Doctor(self):
        try:
            element = self.wait_for_element(self.User_Appointment_Doctor)
            select = Select(element)
            select.select_by_value("12")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_Doctor: {str(e)}")

    def Enter_shift(self):
        try:
            element = self.wait_for_element(self.User_Appointment_Shift_feild)
            select = Select(element)
            select.select_by_value("1")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_shift: {str(e)}")

    def Enter_slot_feild(self):
        try:
            element = self.wait_for_element(self.User_Appointment_slot)
            select = Select(element)
            select.select_by_visible_text("06:00 AM - 09:00 AM")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_slot_feild: {str(e)}")

    def Enter_Appointment(self):
        try:
            element = self.wait_for_element(self.User_Appointment_priority)
            select = Select(element)
            select.select_by_index(3)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_Appointment: {str(e)}")

    def Enter_Message(self, message):
        try:
            element = self.wait_for_element(self.User_Appointment_Message)
            self.for_send_keys(element, message)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_Message: {str(e)}")

    def Click_live_consultancy(self):
        try:
            element = self.wait_for_element(self.User_Appointment_live_consultant)
            select = Select(element)
            select.select_by_value("yes")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Click_live_consultancy: {str(e)}")

    def Alternative_address(self, Address):
        try:
            element = self.wait_for_element(self.User_Appointemnt_Adress)
            self.type_text(element, Address)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Alternative_address: {str(e)}")

    def click_user_appointment_slot(self):
        try:
            element = self.wait_for_element(self.User_Available_slots)
            self.for_click(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_user_appointment_slot: {str(e)}")

    def click_save_button(self):
        try:
            element = self.wait_for_element(self.User_Appointment_save_button)
            self.click_elefunction(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_save_button: {str(e)}")

    def successfull_search_by_bill_number(self):
        try:
            self.for_click(self.wait_for_element(self.pharmacy_option))
            self.for_send_keys(self.wait_for_element(self.pharmacy_bill_search_field), "PHARMAB307")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in successfull_search_by_bill_number: {str(e)}")

    def unsuccessfull_search_by_bill_number(self):
        try:
            self.for_click(self.wait_for_element(self.pharmacy_option))
            self.for_send_keys(self.wait_for_element(self.pharmacy_bill_search_field), "dfghjk")
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in unsuccessfull_search_by_bill_number: {str(e)}")

    def verify_successfull_search_by_bill_number(self):
        try:
            result_element = self.wait_for_element(self.pharmacy_bill_record_assert)
            assert "Records: 0 to 0 of 0" not in result_element.text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_successfull_search_by_bill_number: {str(e)}")

    def verify_unsuccessfull_search_by_bill_number(self):
        try:
            result_element = self.wait_for_element(self.pharmacy_bill_record_assert)
            expected_text = "Records: 0 to 0 of 0 (filtered from 12 total records)"
            assert result_element.text == expected_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_unsuccessfull_search_by_bill_number: {str(e)}")

    def successfull_view_of_bill_details(self):
        try:
            self.click_elefunction(self.wait_for_element(self.pharmacy_view_details))
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in successfull_view_of_bill_details: {str(e)}")

    def verify_successfull_view_bill_details(self):
        try:
            detail_element = self.wait_for_element(self.view_detail_assert)
            expected_text = "Bill No : PHARMAB307"
            assert detail_element.text == expected_text
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in verify_successfull_view_bill_details: {str(e)}")

    def Add_new_appointment_assert(self):
        try:
            element = self.wait_for_element(self.user_Appointment_assert).text
            assert element == "The Date field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Add_new_appointment_assert: {str(e)}")

    def switch_to_payment_iframe(self):
        try:
            self._wait.until(EC.frame_to_be_available_and_switch_to_it(self.payment_frame))
        except TimeoutException:
            print(f"Iframe with class name '{self.payment_frame[1]}' was not found within the timeout period")

    def Click_User_payment_button(self):
        try:
            element = self.wait_for_element(self.user_Appointment_pay_button)
            self.for_click(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Click_User_payment_button: {str(e)}")
        
    def click_pay_with_card(self):
        try:
            element = self.wait_for_element(self.user_Appointment_pay_with_card)
            self.for_click(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_pay_with_card: {str(e)}")

    def Enter_email(self, mailId):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_email)
            self.for_send_keys(element, mailId)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_email: {str(e)}")

    def Enter_card_number(self, Cardnum):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_Card)
            self.type_text(element, Cardnum)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_card_number: {str(e)}")

    def Enter_payment_month(self, month):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_month_year)
            self.for_send_keys(element, month)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_payment_month: {str(e)}")

    def Enter_payment_cvv(self, cvv):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_cvv)
            self.for_send_keys(element, cvv)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_payment_cvv: {str(e)}")

    def Enter_pincode(self, pincode):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_pincode)
            self.type_text(element, pincode)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in Enter_pincode: {str(e)}")

    def click_pay_button_in_payment_page(self):
        try:
            element = self.wait_for_element(self.user_Appointment_payment_pay_button)
            self.for_click(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_pay_button_in_payment_page: {str(e)}")

    def click_status_twice(self):
        try:
            status_element = self.wait_for_element(self.user_Appointment_status)
            self.Double_Click(status_element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_status_twice: {str(e)}")

    def click_delete_button(self):
        try:
            element = self.wait_for_element(self.user_Appointment_delete_button)
            self.click_elefunction(element)
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error in click_delete_button: {str(e)}")

    def total_count_of_bill_records_assert(self):
        try:
            self.for_click(self.wait_for_element(self.pharmacy_option))
            rows = self.wait_for_element(self.bill_records)
            total_records = len(rows)
            print("Total number of bills:", total_records)
            assert total_records > 0
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in total_count_of_bill_records_assert: {str(e)}")

    def Empty_assert(self):
        try:
            element = self.wait_for_element(self.user_Appointment_assert).text
            assert element == "The Date field is required."
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            print(f"Error in Invalid_Assert_search_Appointment: {str(e)}")


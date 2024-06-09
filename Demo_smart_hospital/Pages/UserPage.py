from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.Basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class UserPage(BasePage):

    def init(self, driver):
        super()._init_(driver)
        self.driver = driver

        
    User_my_appointment = (By.CSS_SELECTOR, "i[class='fas fa-hospital-alt']+span")
    User_appointment_search = (By.CSS_SELECTOR, "input[type='search']")
    table_xpath = (By.XPATH, "//div[@id='DataTables_Table_0_wrapper']//table")
    next_page_button = (By.CSS_SELECTOR, "a[class='paginate_button next']>i[class='fa fa-angle-right']")
    user_assert_search=(By.XPATH, "//td[contains(text(),'APPNO6234')]")
    no_data_availbale_assert=(By.CSS_SELECTOR,"td[class='dataTables_empty']")
    Add_appointment_search=(By.CSS_SELECTOR,"div[class='box-tools pull-right']>a")
    Add_appointment_button=(By.CSS_SELECTOR,"div[class='box-tools pull-right']>a")
    User_Appointment_date=(By.ID,"dates")
    User_Appointment_speacilist=(By.ID,"specialist")
    User_Appointment_Doctor=(By.ID,"doctor")
    User_Appointment_Shift_feild=(By.XPATH,"(//select[@class='form-control select2'])[1]")
    User_Appointment_slot=(By.ID,"shift_id")
    User_Appointment_priority=(By.NAME,"priority")
    User_Appointment_Message=(By.ID,"message")
    User_Appointment_live_consultant=(By.ID,"live_consult")                    
    User_Appointemnt_Adress=(By.XPATH,"//textarea[@name='custom_fields[appointment][4]']")
    User_Available_slots=(By.ID,"slot_0")
    User_Appointment_save_button=(By.ID,"formaddbtn")
    user_Appointment_pay_button=(By.XPATH,"(//a[@class='btn btn-info btn-xs']/i)[1]")
    user_Appointment_pay_with_card=(By.CSS_SELECTOR,"button[class='stripe-button-el']")
    user_Appointment_payment_email=(By.ID,"email")
    user_Appointment_payment_Card=(By.ID,"card_number")  
    user_Appointment_payment_month_year=(By.CSS_SELECTOR,"input[placeholder='MM / YY']")  
    user_Appointment_payment_cvv=(By.CSS_SELECTOR,"input[placeholder='CVC']")  
    user_Appointment_payment_pincode=(By.ID,"billing-zip")
    user_Appointment_payment_pay_button=(By.CLASS_NAME,"iconTick")
    user_Appointment_status=(By.XPATH,"//th[@aria-controls='DataTables_Table_0' and text()='Status']")
    user_Appointment_delete_button=(By.CSS_SELECTOR,"i[class='fa fa-trash']")
    payment_frame=(By.CLASS_NAME,"stripe_checkout_app")


    pharmacy_bill_search_field=By.CSS_SELECTOR,"input[type='search']"
    show_field=By.CSS_SELECTOR,"i[class='fa fa-reorder']"
    pay_button=By.CSS_SELECTOR,"button[class='btn btn-primary btn-xs']"
    view_payment_option=By.CSS_SELECTOR,"a[class='btn btn-default view_payment btn-xs']"
    payment_amount_field=By.CSS_SELECTOR,"input[id='amount_total_paid']"
    add_pay_button=By.CSS_SELECTOR,"button[id='pay_button']"
    paywithcard_button=By.CSS_SELECTOR,"button[class='stripe-button-el']"
    payment_email_field=By.CSS_SELECTOR,"div[class='emailInput input'] input[id='email']"
    payment_cardnumber_field=By.CSS_SELECTOR,"input[id='card_number']"
    card_expiry_date_field=By.CSS_SELECTOR,"input[id='cc-exp']"
    card_cvv_field=By.CSS_SELECTOR,"input[id='cc-csc']"
    final_pay_button=By.CSS_SELECTOR,"button[id='submitButton']"
    pharmacy_option=By.XPATH,"//i[@class='fas fa-mortar-pestle']//parent::a"
    pharmacy_bill_record_assert=By.CSS_SELECTOR,"div[id='DataTables_Table_0_info']"
    pharmacy_view_details=By.XPATH,"//a[@class='btn btn-default btn-xs']"
    view_detail_assert=By.XPATH,"//h5[text()='Bill No : PHARMAB307']"
    norecord=By.XPATH,"//td[@class='dataTables_empty']"
    card_pincode=By.CSS_SELECTOR,"input[id='billing-zip']"
    addnewappointment_invalidalert=By.CSS_SELECTOR,"div[class='toast-message'] p"

    def test_next_page_button(self):
        element = self.wait_for_element(self.next_page_button)
        self.for_click(element)

    def test_search_record(self, searchRecord):
        element = self.wait_for_element(self.User_appointment_search)
        self.for_send_keys(element, searchRecord)

    def click_user_appointment(self):
        element = self.wait_for_element(self.User_my_appointment)
        self.for_click(element)

    def Assert_search_Appointment(self):
        element = self.wait_for_element(self.user_assert_search).text
        element = element.strip()
        expected_text = "APPNO6234"
        assert element == expected_text, f"Expected '{expected_text}', but got '{element}'"

    def Invalid_Assert_search_Appointment(self):
        element = self.wait_for_element(self.no_data_availbale_assert).text
        assert element._eq_("No matching records found")
    
    def Click_usert_Add_appointment(self):
        element = self.wait_for_element(self.Add_appointment_search)
        self.for_click(element)
    
    def Click_Add_appointment(self):
        element=self.wait_for_element(self.Add_appointment_button)
        self.for_click(element)

    def Enter_user_date(self,Date):
        element = self.wait_for_element(self.User_Appointment_date)
        self.for_send_keys(element,Date)

    def Enter_Specialist(self):
        element = self.wait_for_element(self.User_Appointment_speacilist)
        select = Select(element)
        select.select_by_index(2)

    def Enter_Doctor(self):
        element = self.wait_for_element(self.User_Appointment_Doctor)
        select = Select(element)
        select.select_by_value("12")

    def Enter_shift(self):
        element = self.wait_for_element(self.User_Appointment_Shift_feild)
        select = Select(element)
        select.select_by_value("1")


    def Enter_slot_feild(self):
        element = self.wait_for_element(self.User_Appointment_slot)
        select = Select(element)
        select.select_by_visible_text("06:00 AM - 09:00 AM")


    def Enter_Appointment(self):
        element = self.wait_for_element(self.User_Appointment_priority)
        select = Select(element)
        select.select_by_index(3)


    def Enter_Message(self,message):
        element =self.wait_for_element(self.User_Appointment_Message)
        self.for_send_keys(element,message)

    def Click_live_consultancy(self):
        element = self.wait_for_element(self.User_Appointment_live_consultant)
        select = Select(element)
        select.select_by_value("yes")

    def Alternative_address(self,Address):
        element =self.wait_for_element(self.User_Appointemnt_Adress)
        self.for_send_keys(element,Address)

    def click_user_appointment_slot(self):
        element = self.wait_for_element(self.User_Available_slots)
        self.for_click(element)

    def click_save_button(self):
        element = self.wait_for_element(self.User_Appointment_save_button)
        self.for_click(element)


    def successfull_search_by_bill_number(self):
        self.for_click(self.wait_for_element(self.pharmacy_option))
        self.for_send_keys(self.wait_for_element(self.pharmacy_bill_search_field),"PHARMAB307")

    def unsuccessfull_search_by_bill_number(self):
        self.for_click(self.wait_for_element(self.pharmacy_option))
        self.for_send_keys(self.wait_for_element(self.pharmacy_bill_search_field),"dfghjk")

    def verify_successfull_search_by_bill_number(self):
        result_element = self.wait_for_element(self.pharmacy_bill_record_assert)
        assert "Records: 0 to 0 of 0" not in result_element.text
    
    def verify_unsuccessfull_search_by_bill_number(self):
        result_element = self.wait_for_element(self.pharmacy_bill_record_assert)
        expected_text = "Records: 0 to 0 of 0 (filtered from 12 total records)"
        assert result_element.text == expected_text

    def successfull_view_of_bill_details(self):
        self.for_click(self.wait_for_element(self.pharmacy_view_details))

    def verify_successfull_view_bill_details(self):
        detail_element = self.wait_for_element(self.view_detail_assert)
        expected_text = "Bill No : PHARMAB307"
        assert detail_element.text == expected_text

    def Add_new_appointment_assert(self):
        element=self.wait_for_element(self.addnewappointment_invalidalert).text
        assert element.__eq__("The Date field is required.")

    def switch_to_payment_iframe(self):
        try:
            self._wait.until(EC.frame_to_be_available_and_switch_to_it(self.payment_frame))
        except TimeoutException:
            print(f"Iframe with class name '{self.payment_frame[1]}' was not found within the timeout period")

    def Click_User_payment_button(self):
        element = self.wait_for_element(self.user_Appointment_pay_button)
        self.for_click(element)
        
    def click_pay_with_card(self):
        element = self.wait_for_element(self.user_Appointment_pay_with_card)
        self.for_click(element)

    def Enter_email(self,mailId):
        element = self.wait_for_element(self.user_Appointment_payment_email)
        self.for_send_keys(element,mailId)

    def Enter_card_number(self,Cardnum):
        element = self.wait_for_element(self.user_Appointment_payment_Card)
        self.for_send_keys(element,Cardnum)

    def Enter_payment_month(self,month):
        element = self.wait_for_element(self.user_Appointment_payment_month_year)
        self.for_send_keys(element,month)

    def Enter_payment_cvv(self,cvv):
        element = self.wait_for_element(self.user_Appointment_payment_cvv)
        self.for_send_keys(element,cvv)

    def Enter_pincode(self,pincode):
        element = self.wait_for_element(self.user_Appointment_payment_pincode)
        self.for_send_keys(element,pincode)

    def click_pay_button_in_payment_page(self):
        element = self.wait_for_element(self.user_Appointment_payment_pay_button)
        self.for_click(element)

    def click_status_twice(self):
        status_element = self.wait_for_element(self.user_Appointment_status)
        self.Double_Click(status_element)

    def click_delete_button(self):
        element=self.wait_for_element(self.user_Appointment_delete_button)
        self.for_click(element)
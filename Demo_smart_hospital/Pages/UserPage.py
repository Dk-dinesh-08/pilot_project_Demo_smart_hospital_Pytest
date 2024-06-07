from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from selenium.webdriver.support.ui import Select

class UserPage(BasePage):
    def _init_(self, driver):
        super().__init__(driver)
        self.driver = driver

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
    bill_records=By.XPATH,"//tbody//tr[@role='row']"


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

    def total_count_of_bill_records_assert(self):
        self.for_click(self.wait_for_element(self.pharmacy_option))
        rows = self.wait_for_elements(self.bill_records)
        total_records = len(rows)
        print("Total number of bills:", total_records)
        assert total_records >0
from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage

class DoctorPage(BasePage):

    def _init_(self, driver):
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
        assert element.__eq__("Patient Not Found")

    def Assert_empty_Field(self):
        element = self.wait_for_element(self.empty_assert).text
        assert element.__eq__("The Child Name field is required.")
        
    def Assert_variable_id(self):
        element=self.wait_for_element(self.patient_not_found).text
        assert element.__eq__("Case Id Not Valid")
    
    def Enter_death_date(self,deathDate):
        element = self.wait_for_element(self.death_date)
        self.for_send_keys(element, deathDate)

    def Enter_death_report(self,deathreport):
        element = self.wait_for_element(self.death_report)
        self.for_send_keys(element, deathreport)

    def Assert_death_Empty_record(self):
        element = self.wait_for_element(self.empty_assert).text
        assert element.__eq__("The Patient field is required.")

    def search_record(self,record):
        element = self.wait_for_element(self.Search_record)
        self.for_send_keys(element,record)

    def Assert_no_data_availble(self):
        element = self.wait_for_element(self.no_data_available).text
        assert element.__eq__("Add new record or search with different criteria.")

    def Assert_valid_birth_search_assert(self):
        element = self.wait_for_element(self.valid_birth_search_assert).text
        assert element.__eq__("BREF62")

    def Assert_valid_death_search_assert(self):
        element = self.wait_for_element(self.valid_death_search_assert).text
        assert element.__eq__("DREF50")

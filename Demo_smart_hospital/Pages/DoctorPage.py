from selenium.webdriver.common.by import By
from Utility import read_config
from Pages.Basepage import BasePage
class DoctorPage(BasePage):

    def __init__(self, driver):
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
    contact=(By.ID,"contact")
    adress=(By.ID,"address")
    case_id=(By.ID,"case_id")
    fathers_name=(By.ID,"father_name")
    Report=(By.ID,"birth_report")
    save_button=(By.ID,"formaddbtn")

    def click_Birth_and_death_record(self):
        self.for_click(self.wait_for_element(self.Birth_and_death_record))   

    def click_birth_record(self):
        self.for_click(self.wait_for_element(self.Birth_record))   

    def click_death_record(self):
        self.for_click(self.wait_for_element(self.Death_record))   

    def Fill_form_birth_record(self):
        self.for_click(self.wait_for_element(self.Add_birth_record))   
        self.for_send_keys(self.wait_for_element(self.Child_name),read_config.get_config("birth_record","childname"))
        self.for_click(self.wait_for_element(self.Gender_drop_down))
        self.for_click(self.wait_for_element(self.Male_gender_option))
      
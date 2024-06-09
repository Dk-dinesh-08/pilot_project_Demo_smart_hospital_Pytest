import pytest
from Utility import Consolelogger
from Pages.UserPage import UserPage
from Utility import read_config

@pytest.mark.usefixtures("test_setup_and_setdown")
class TestPayment:
    @pytest.mark.smoke
    def test_valid_Payment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.click_status_twice()
        user_page.Click_User_payment_button()
        user_page.click_pay_with_card()
        user_page.switch_to_payment_iframe()
        user_page.Enter_email(read_config.get_config("payment_page","email"))
        user_page.Enter_card_number(read_config.get_config("payment_page","card_number"))
        user_page.Enter_payment_month(read_config.get_config("payment_page","month_year"))
        user_page.Enter_payment_cvv(read_config.get_config("payment_page","cvv"))
        user_page.Enter_pincode(read_config.get_config("payment_page","zip_code"))
        user_page.click_pay_button_in_payment_page()
        log.info("Payment sucessfully")

    @pytest.mark.smoke
    def test_Invalid_Payment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.click_status_twice()
        user_page.Click_User_payment_button()
        user_page.click_pay_with_card()
        user_page.switch_to_payment_iframe()
        user_page.Enter_email(read_config.get_config("Invalid_payment_page","Invalid_email"))
        user_page.Enter_card_number(read_config.get_config("Invalid_payment_page","Invalid_card_number"))
        user_page.Enter_payment_month(read_config.get_config("Invalid_payment_page","Invalid_month_year"))
        user_page.Enter_payment_cvv(read_config.get_config("Invalid_payment_page","Invalid_cvv"))
        user_page.click_pay_button_in_payment_page()
        log.info("Invalid Payment sucessfully")

    @pytest.mark.smoke
    def test_empty_Payment(self):
        user_page=UserPage(self.driver)
        log=Consolelogger.get_logger()
        user_page.click_Home_login_button()
        user_page.click_Sign_in_button()
        user_page.click_user_appointment()
        user_page.click_status_twice()
        user_page.Click_User_payment_button()
        user_page.click_pay_with_card()
        user_page.switch_to_payment_iframe()
        user_page.click_pay_button_in_payment_page()
        log.info("Empty Payment sucessfully")

   
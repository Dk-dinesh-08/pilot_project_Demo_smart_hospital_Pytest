import pytest
from Utility import Consolelogger
from Pages.Basepage import BasePage
from Pages.DoctorPage import DoctorPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestNotificationDelete:
    @pytest.mark.regression
    def test_valid_notification_delete(self):
        Basepage =BasePage(self.driver)
        log=Consolelogger.get_logger()
        Basepage.click_Home_login_button()
        Basepage.click_Admin_login_button()
        Basepage.switch_to_window()
        Basepage.click_Doctor_login_button()
        Basepage.click_Sign_in_button()
        result=Basepage.verify_successfull_login()
        assert result.__eq__("Doctor")
        Doctorpage=DoctorPage(self.driver)
        Doctorpage.successfull_notification_delete()
        Doctorpage.verify_successfull_notification_delete()
        log.info("All notification deleted  successfully")
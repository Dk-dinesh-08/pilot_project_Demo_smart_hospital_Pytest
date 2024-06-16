import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger
from Utility import read_config


@pytest.mark.usefixtures("test_setup_and_setdown")

class TestQueueSearch():
    @pytest.mark.regression
    def test_valid_queue_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test valid Queue search results")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_queue_search()
        doctor_name=read_config.get_config("fill_queue_searchform","doctor_name")
        select_shift=read_config.get_config("fill_queue_searchform","select_shift")
        date_entry=read_config.get_config("fill_queue_searchform","date_entry")
        admin.fill_queue_searchform(doctor_name,select_shift,date_entry)
        log.info("valid queue search results is verified successfully")

    @pytest.mark.smoke
    def test_invalid_queue_search(self):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test invalid Queue search results")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_queue_search()
        doctor_name=read_config.get_config("fill_queue_searchform_invalid","doctor_name")
        select_shift=read_config.get_config("fill_queue_searchform_invalid","select_shift")
        date_entry=read_config.get_config("fill_queue_searchform_invalid","date_entry")
        admin.fill_queue_searchform_with_invalid_details(doctor_name,select_shift,date_entry)
        invalid_slot_field_text=read_config.get_config("assert_messages","invalid_slot_field_text")
        admin.verify_invalid_queue_search_result(invalid_slot_field_text)
        log.info("Invalid Queue search results is verified successfully")

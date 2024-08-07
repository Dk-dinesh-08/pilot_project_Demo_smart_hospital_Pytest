import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger
from Utility import read_config


@pytest.mark.usefixtures("test_setup_and_setdown")

class TestQueueSearch:
    @pytest.mark.regression
    def test_valid_queue_search(self):
        try:
            admin=AdminPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test valid Queue search results")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_queue_search()
            admin.fill_queue_searchform()
            log.info("valid queue search results is verified successfully")
        except Exception:
            log.error(f"Exception occured in TestQueueSearch")

    @pytest.mark.smoke
    def test_invalid_queue_search(self):
        try:
            admin=AdminPage(self.driver)
            log=Consolelogger.get_logger()
            log.info("To test invalid Queue search results")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_queue_search()
            admin.fill_queue_searchform_with_invalid_details()
            admin.verify_invalid_queue_search_result()
            log.info("Invalid Queue search results is verified successfully")
        except Exception:
            log.error(f"Exception occured in TestQueueSearch")


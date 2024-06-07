import pytest
from Pages.Adminpage import AdminPage


@pytest.mark.usefixtures("test_setup_and_setdown")

class TestAppointmentSearch():
    def test_valid_appointment_search(self):
        admin=AdminPage(self.driver)
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_queue_search()
        admin.fill_queue_searchform_with_invalid_details()
        admin.verify_invalid_queue_search_result()

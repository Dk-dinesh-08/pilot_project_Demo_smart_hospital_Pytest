import pytest
from Pages.Adminpage import AdminPage



@pytest.mark.usefixtures("test_setup_and_setdown")

class TestLogin():
    @pytest.mark.confirmation
    def test_valid_login(self):

        admin=AdminPage(self.driver)
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        actual_text=admin.verify_admin_page_opens()
        assert actual_text.__eq__(admin.expected_text)
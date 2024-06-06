import pytest
from Pages.Adminpage import AdminPage

@pytest.mark.usefixtures("test_setup_and_setdown")

class TestValidAddStockItem():
    def test_valid_add_stock_item(self):
        admin=AdminPage(self.driver)
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_inventory_button()
        admin.fill_add_stock_item_form()
        assert admin.verify_successful_additionof_stock()
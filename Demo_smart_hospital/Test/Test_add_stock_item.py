import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger
from Utility import excel_reader
from Utility import read_config
import os

@pytest.mark.usefixtures("test_setup_and_setdown")
@pytest.mark.parametrize(
    "ItemCategory,Item,Supplier,Store,Quantity,Price",
    excel_reader.get_data(
        os.path.join(os.path.dirname(__file__), '..', 'ExcelReader', 'test_data.xlsx'), "AddStock"
    )
)
class TestAddStockItem:

    @pytest.mark.smoke
    def test_valid_add_stock_item(self, ItemCategory, Item, Supplier, Store, Quantity, Price):
        admin = AdminPage(self.driver)
        log = Consolelogger.get_logger()
        try:
            log.info("To test add stock item")
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_inventory_button()
            admin.fill_add_stock_item_form(ItemCategory, Item, Supplier, Store, Quantity, Price)
            assert admin.verify_stock_list_page_opens(read_config.get_config("assert_valid_stock_item", "stock_list_page_url"))
            log.info("Stock item is added successfully")
        except Exception:
            log.error("Failed in the test valid add stock item")

    @pytest.mark.smoke
    def test_invalid_add_stock_item(self, ItemCategory, Item, Supplier, Store, Quantity, Price):
        admin = AdminPage(self.driver)
        log = Consolelogger.get_logger()
        log.info("To test unsuccessful addition of stock item")
        try:
            admin.click_Home_login_button()
            admin.click_Admin_login_button()
            admin.switch_to_window()
            admin.click_Admin_signin_button()
            admin.click_Sign_in_button()
            admin.click_inventory_button()
            admin.fill_add_stock_item_form_with_invalid_supplier(ItemCategory, Item, Supplier, Store, Quantity, Price)
            assert admin.verify_supplier_field_required_msg_in_additionof_stock()
            log.info("Unsuccessful addition of stock item is verified")
        except Exception:
            log.error("Failed in the test invalid add stock item")

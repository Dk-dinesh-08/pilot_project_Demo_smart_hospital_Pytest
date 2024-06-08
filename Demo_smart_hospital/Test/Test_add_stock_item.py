import pytest
from Pages.Adminpage import AdminPage
from Utility import Consolelogger
from Utility import excel_reader

@pytest.mark.usefixtures("test_setup_and_setdown")
@pytest.mark.parametrize("ItemCategory,Item,Supplier,Store,Quantity,Price",excel_reader.get_data( "D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\ExcelReader\\test_data.xlsx","AddStock"))

class TestAddStockItem():

    def test_valid_add_stock_item(self,ItemCategory,Item,Supplier,Store,Quantity,Price):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test add stock item")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_inventory_button()
        admin.fill_add_stock_item_form(ItemCategory,Item,Supplier,Store,Quantity,Price)
        assert admin.verify_successful_additionof_stock()
        log.info("Stock item is added sucessfully")

    def test_invalid_add_stock_item(self,ItemCategory,Item,Supplier,Store,Quantity,Price):
        admin=AdminPage(self.driver)
        log=Consolelogger.get_logger()
        log.info("To test unsuccessfull addition of stock item")
        admin.click_Home_login_button()
        admin.click_Admin_login_button()
        admin.switch_to_window()
        admin.click_Admin_signin_button()
        admin.click_Sign_in_button()
        admin.click_inventory_button()
        admin.fill_add_stock_item_form_with_invalid_supplier(ItemCategory,Item,Supplier,Store,Quantity,Price)
        assert admin.verify_supplier_field_required_msg_in_additionof_stock
        log.info("unsuccessfull addition of stock item is verified")
import pytest
from selenium import webdriver
from Utility import read_config
from selenium.webdriver.common.by import By
@pytest.fixture()
def test_setup_and_setdown(request):
    browser=read_config.get_config("basic info","browser")
    driver=None
    if browser._eq_("chrome"):
        driver=webdriver.Chrome()
    elif browser._eq_("firefox"):
        driver=webdriver.Firefox
    elif browser._eq_("edge"):
        driver=webdriver.Edge
    else:
        print("Other browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    app_url=read_config.get_config("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()
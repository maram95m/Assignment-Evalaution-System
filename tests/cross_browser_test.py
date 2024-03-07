import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.base_page import read_config,base_page


# Read configuration
config = read_config()

@pytest.fixture(params=["chrome", "firefox"])  # Parameterized fixture for browsers
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    
    yield driver
    driver.quit()

def test_login(driver):
    """
    Test cross-browser compatibility.

    This test verifies that the application works correctly across different web browsers.
    It executes the same set of actions and assertions on multiple browsers,
    ensuring consistent behavior and functionality.
    The test aims to identify any browser-specific issues or inconsistencies.
    """
    login = base_page(driver)
    login.navigate_to_login_page(base_page.BASE_URL)
    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.click_login_button()
    assert driver.current_url == login.get_current_url()
   
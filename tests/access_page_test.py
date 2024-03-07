from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Pages.base_page import base_page

from Pages.base_page import read_config,base_page


# Read configuration
config = read_config()
base_page.set_up()

@pytest.fixture
def test_access_page(browser):
# Input valid employee credentials and login
   employee_username = "test-employee4"
   employee_password = "45622"
   employee_login_form =browser.find_element(By.XPATH, '//*[@id="myform"]/button')
   browser.find_element(By.NAME,"username").send_keys(employee_username)
   browser.find_element(By.NAME,"password").send_keys(employee_password)
   employee_login_form.click()

# Verify successful login for employee
   assert "Employee " in browser.title

# Logout employee
# (Implementation depends on how logout functionality is implemented)
# Example:
# driver.find_element_by_id("logout-button").click()

# Input valid manager credentials and login
   manager_username = "test-supervisor3"
   manager_password = "45622"
   manager_login_form = browser.find_element(By.XPATH, '//*[@id="myform"]/button')
   browser.find_element(By.NAME,"username").send_keys(manager_username)
   browser.find_element(By.NAME,"password").send_keys(manager_password)
   manager_login_form.click()

# Verify successful login for manager 
   assert "Manager " in browser.title



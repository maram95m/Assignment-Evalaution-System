import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import base_page
from Pages.base_page import read_config
from Pages.elements import ElementLocators

import json
import os

# Read configuration
config = read_config()
base_page.set_up()

@pytest.fixture





def read_users_data():
    # Read user data from JSON file
        script_directory = os.path.dirname(os.path.realpath(__file__))
        config_file_path = os.path.join(script_directory, 'user_data.json')
        
        with open(config_file_path, 'r') as f:
          users_data = json.load(f)
        return users_data["users"]

@pytest.mark.parametrize("user_type", read_users_data())
def test_login_and_create_evaluation(driver, login, user_data):
    
    """
    Test logging in with different user types.

    This test logs in with different user types (employee and manager) using Selenium WebDriver.
    It reads login credentials from a JSON configuration file and asserts successful login for each user type.
    """
   
    # Navigate to the login page
    login.navigate_to_login_page(user_data["login_url"])
    
    # Enter username, password, and click login button
    login.enter_username(user_data["username"])
    login.enter_password(user_data["password"])
    login.submit_login_form()

    # Assert that the user is redirected to the dashboard page
    assert "dashboard" in driver.current_url

    # Navigate to the evaluation page
    driver.get(user_data["eval_url"])

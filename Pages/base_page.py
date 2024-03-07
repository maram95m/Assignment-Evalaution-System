from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import requests
from elements import ElementLocators
from selenium import webdriver


class base_page:
    
    """
    Login class for handling user authentication.

    This class provides methods for logging in the application.
    It encapsulates the login functionality, making it reusable across different test cases.
    The class abstracts away the details of the login process
    """   
    BASE_URL = "http://172.22.1.141:8089/"  # Base URL of your application
    evaluation_date = "12%2F01%2F2023%2000%3A00%3A00"  # URL-encoded date

    
    def __init__(self, driver):
        self.driver = driver
      
    def read_config(self):
        
        # Get the absolute path to the config.json file
        script_directory = os.path.dirname(os.path.realpath(__file__))
        config_file_path = os.path.join(script_directory, 'config.json')
                # Read the JSON configuration file
        # with open('config.json', 'r') as config_file:
        #     self.config_data = json.load(config_file)
        
        with open(config_file_path, 'r') as config_file:
         self.config_data = json.load(config_file)
        return self.config_data

    def set_up():
  
    # Initialize the WebDriver
     driver = webdriver.Chrome()
     driver.maximize_window()
    # Set implicit wait time to wait for elements to appear
     driver.implicitly_wait(10)
    
    # Yield the driver instance to the test
     yield driver
    
    # Quit the driver after the test
     driver.quit()

    def navigate_to_login_page(self, login_url):
        self.driver.get(login_url)

    def enter_username(self, username):
        username_input = self.driver.find_element_by_name(ElementLocators.EMPLOYEE_NAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element_by_name(ElementLocators.EMPLOYEE_PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def submit_login_form(self):
        submit_button = self.driver.find_element_by_xpath(ElementLocators.LOGIN_BUTTON)
        submit_button.click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        

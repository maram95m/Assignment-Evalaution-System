
import json
import unittest
from selenium import webdriver
from Pages.base_page import base_page
from allure import feature,story
import os
import allure
from Pages.base_page import read_config
from Pages.elements import ElementLocators
# login_page_test.py

"""
Test cases related to user authentication functionality.
"""

# Read configuration
config = read_config()
base_page.set_up()


@feature("Login Feature")
class test_login_page():

 @story("Successful Login")
    # @severity(severity_level="NORMAL")
 def test_successful_login_as_employee(self):
     
         """
    Test the login as employee functionality.

    This test verifies that only the employee user can successfully log in to the system.
    It navigates to the login page, enters valid credentials for a user from config json file, and submits the login form.
    
    """
           # Initialize the LoginPage object
         login = base_page(self.driver)
         credentials = config["employee"]
         self.execute_login_test(credentials)

 @story("Failed Login")
    # @severity(severity_level="NORMAL")
 def test_failed_login(self):
     
          """
    Test invalid login attempts.

    This test verifies that users cannot log in with invalid credentials.
    It navigates to the login page, enters invalid username and password combination,
    and submits the login form. The test checks that an error message is displayed
    indicating that the login attempt failed.
     """
          credentials = config["invalid_credentials"]
          self.execute_login_test(credentials)

 @allure.step("Execute Login Test")
 def execute_login_test(self, credentials):
        login_url = config["login_url"]

                # Navigate to the login page
        self.login.navigate_to_login_page(login_url)

        # Input username and password
        self.login.enter_username(credentials["username"])
        self.login.enter_password(credentials["password"])

        # Submit the login form
        self.login.submit_login_form()

        # Check the result
        if "successful" in credentials["expected_result"]:
            self.assertIn("Employee", self.login.get_current_url()) 
        else:
            # Customize this assertion based on how your login failure is handled
            self.assertIn(login_url, self.login.get_current_url())

if __name__ == '__main__':
    unittest.main()
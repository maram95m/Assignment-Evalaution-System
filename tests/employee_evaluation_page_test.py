import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.employee_page import employee_page
from Pages.base_page import base_page
from Pages.base_page import read_config
from Pages.elements import ElementLocators


# evaluation_page_test.py

"""
Test cases related to evaluation system functionality.
"""
@pytest.fixture(scope="session")
def base_page():
    # Read configuration
    config = read_config()
    # Set up base page
    base = base_page(config)
    yield base,config
    # Teardown operations can be performed here if needed


   
 
def test_random_checkboxes_in_table(browser,base,config):
            """
    Test the evaluation system functionality.

    This test verifies that the evaluation system works correctly.
    It navigates to the evaluation page, fills out the evaluation form with random data,
    submits the form, and checks that the evaluation is successfully recorded in the system.
 
            """
        # Access base page instance via fixture
            base.set_up()
        # Initialize the LoginPage object
            
            login = base_page(browser)
            credentials = config["employee"]
            login_url = config["login_url"]


        # Navigate to the login page
            login.navigate_to_login_page(login_url)
            login.enter_username(credentials['username'])
            login.enter_password(credentials['password'])
            login.submit_login_form()
            
        # Initialize the EvaluationPage object
            evaluation =employee_page(browser)
            evaluation.navigate_to_evaluation(base_page.evaluation_date)
    
           

                # Check if the employee page is reached
            assert evaluation.is_employee_page(), "Login failed. Employee page not reached."
            
            evaluation.find_checkbox_by_id()
            evaluation.enter_rating(rating_value=6)
            evaluation.enter_feedback_comments('team collaboration','rotation days','raises on salary')
            evaluation.submit_evaluation()
            evaluation.confirm()
            evaluation.clear_ratings()

    

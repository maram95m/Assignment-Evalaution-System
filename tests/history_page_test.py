
import json
import pytest
from selenium import webdriver
from Pages.history_page import history_page
from Pages.base_page import base_page
from Pages.employee_page import employee_page
from allure import feature,story
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from Pages.base_page import base_page
from Pages.base_page import read_config
from Pages.elements import ElementLocators


# history_page_test.py

"""
Test cases related to history data to ensure that the traceability is correct.
"""
# Read configuration
config = read_config()
base_page.set_up() 

@pytest.fixture
def test_check_history_data(browser):

    """
    Test the history functionality.

    This test verifies that the history page displays the correct data.
    It navigates to the history page, retrieves the displayed data,
    and compares it with the expected data from previous page.
    The test ensures that the displayed data matches the user's evaluation page.
    """
    
        # Initialize the HistoryPage object      
    history = history_page(browser)
  
       
        # Initialize the LoginPage object
    login = base_page(browser)
    evaluation =employee_page(browser)
            
    evaluation.navigate_to_evaluation(base_page.evaluation_date)      
        # Navigate to history page
    history.navigate_to_history(base_page.evaluation_date)
  


    login.enter_username(config['username'])
    login.enter_password(config['password'])
    login.submit_login_form()
    
    history.navigate_to_history(base_page.evaluation_date)
    history.reach_target_page()
    history.fetching_past_transactions()
   
    
    
def test_textarea_text(browser):
    
        history = history_page(browser)

        # Call the get_textarea_texts() function to retrieve textarea texts
        textarea_texts = history.check_employee_feedback()

        # Define expected textarea texts
        expected_texts = ["wMs99kD2KP", "dOdSWSnayY", "GHf5WuVXcd"] 
        
        # Assert the retrieved textarea texts against expected values
        assert textarea_texts == expected_texts, "Textarea texts do not match expected values"
        
        
def test_checkbox_verification(browser):
        # Assume you have initialized your driver and navigated to the appropriate page
        history = history_page(browser)

        
        # Perform actions to get the selected checkboxes and all checkboxes
        selected_checkboxes = [...]  # Selected checkboxes IDs
        checkboxes = [...]  # List of checkbox elements

        # Verify checkboxes
        result = history.verify_checkboxes(history.fetching_past_transactions())
        assert result, "Checkbox verification failed"

     
     
    
    
    



      


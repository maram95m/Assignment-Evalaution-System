from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import read_config
from Pages.elements import ElementLocators
from base_page import base_page
from Pages.employee_page import evaluation_page
from selenium.common.exceptions import StaleElementReferenceException

class history_page:
    BASE_URL = "http://172.22.1.141:8089"

    """
    History class for accessing user transaction history.

    """
    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to_history(self, evaluation_date):
        url = f"{self.BASE_URL}/Employee/EditEvaluation?EvaluationDate={evaluation_date}"
        self.driver.get(url)
        
        
    def reach_target_page(self):
                #  navigate to another page
     
      WebDriverWait(self.driver, 10).until(EC.url_contains("Employee"))

      assert "Employee" in self.driver.title, "Login failed. Employee page not reached."
      target_page_link = self.driver.find_element_by_xpath(ElementLocators.TARGET_PAGE_LINK)
      target_page_link.click()
      
 
            
    def fetching_past_transactions(self):
            checkboxes = self.driver.find_elements_by_xpath(ElementLocators.CHECKBOXES)
            selected_checkboxes = []
            evaluation =evaluation_page(self.driver)

           # Check all checkboxes
            for checkbox in checkboxes:
             checkbox.click()
              
           # Simulate selecting checkboxes in the table
             if checkbox.is_selected():
              selected_checkboxes.append(checkbox.get_attribute("id"))

            # Submit the form or navigate to another page where the history data is stored
   
            submit_button = self.driver.find_element_by_ID(ElementLocators.SUBMIT_BUTTON)
            submit_button.click()
            # Wait for the page with history data to load
            target_page_link_history = self.driver.find_element_by_xpath(ElementLocators.TARGET_PAGE_HISTORY)
            target_page_link_history.click()
            WebDriverWait(self.driver, 10).until(EC.url_contains("EvaluationHistory"))
           
           
           
            view_btn = self.driver.find_element_by_xpath(ElementLocators.VIEW_BUTTON)
            view_btn.click()
           
            WebDriverWait(self.driver, 10).until(EC.url_contains(evaluation.navigate_to_evaluation(base_page.evaluation_date) ))

            # Find all history data elements
            history_data_elements = self.driver.find_elements_by_xpath(ElementLocators.HISTORY_DATA_ELEMENTS)

          # Extract the values of the history data elements
            history_data_values = [element.text for element in history_data_elements]
     
      
          # Compare the extracted values with the IDs of the selected checkboxes
            for checkbox_id in selected_checkboxes:
              try:
                         
                assert checkbox_id in history_data_values, f"Checkbox {checkbox_id} is not found in history data"
  
              except StaleElementReferenceException:
                continue
                
          # Verify that all checkboxes are checked
            for checkbox in checkboxes:
              assert checkbox.is_selected(), f"Checkbox {checkbox.get_attribute('id')} is not checked"
              
            return checkboxes,selected_checkboxes
              
              
    def verify_checkboxes(self, selected_checkboxes, checkboxes):
        history_data_values = [checkbox.get_attribute('id') for checkbox in checkboxes]

        all_checkboxes_found = all(checkbox_id in history_data_values for checkbox_id in selected_checkboxes)

        all_checkboxes_checked = all(checkbox.is_selected() for checkbox in checkboxes)

        return all_checkboxes_found and all_checkboxes_checked
              
              

    

    def check_employee_feedback(self):
             
        textarea_texts = []
        for locator in ElementLocators.textarea_locators:
            textarea = self.driver.find_element(*locator)
            textarea_texts.append(textarea.text)
        return textarea_texts

 
  
     
        
        
      
      
      
      
        
        

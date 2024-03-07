from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import read_config
from Pages.elements import ElementLocators
import urllib
class employee_page:
  
  
    """
    EvaluationClass for managing evaluation processes.

    This class provides methods for conducting evaluations within the system.
    It encapsulates functionality related to creating, submitting, and analyzing evaluations,
    making it reusable and modular across different components of the application.
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://172.22.1.141:8089"
        
    def navigate_to_evaluation(self, evaluation_date):
        evaluation_path = "/Employee/CreateEvaluation"
        encoded_date = urllib.parse.quote(evaluation_date)  # Encode evaluation date if needed
        full_url = f"{self.base_url}{evaluation_path}?EvaluationDate={encoded_date}"
        self.driver.get(full_url)  

    def navigate_to_evaluation_history(self):
        # Assuming there's a link/button to navigate to the evaluation history page
        history_link = self.driver.find_element(By.ID, "evaluation_history_link")
        history_link.click()

    def get_evaluation_data(self):
        # Implement logic to retrieve evaluation data from the history page
        # For example, if evaluations are listed in a table, you might scrape the data from the table cells
        evaluation_data = []
        evaluation_elements = self.driver.find_elements_by_id(ElementLocators.CHECKBOX_TABLE)
        for element in evaluation_elements:
            evaluation_data.append(element.text)
        return evaluation_data

       # Define page elements
    def find_checkbox_by_id(self):
        return self.driver.find_elements_by_id(ElementLocators.CHECKBOX_ID)

    
    def enter_feedback_comments(self, like,dislike,improv):
           like_comments = self.driver.find_element_by_id(ElementLocators.TEXTAREA_LIKE)
           dislike_comments = self.driver.find_element_by_id(ElementLocators.TEXTAREA_DISLIKE)
           improvments = self.driver.find_element_by_id(ElementLocators.IMPROVMENTS)
      

           like_comments.send_keys(like)
           dislike_comments.send_keys(dislike)
           improvments.send_keys(improv)
          
        # # Verify that the text was inserted into the textarea
        #    assert comments.get_attribute("value") == text_to_insert
           
    def submit_evaluation(self):
        submit_button = self.driver.find_element_by_xpath(ElementLocators.SAVE_BUTTTON)
        submit_button.click()
        
        
        # Define methods for actions
    def enter_rating(self, value):
               # Find all checkboxes in the table
            checkboxes = self.driver.find_elements_by_xpath(ElementLocators.CHECKBOX_TABLE)

         # Check all checkboxes
            # for checkbox in checkboxes:
            #   checkbox.click()
            for index, checkbox in enumerate(checkboxes):
             if index + 1 == value:  # Assuming rating values start from 1
                checkbox.click()
                break
              
              
    def clear_ratings(self):
        checkboxes = self.driver.find_elements_by_id(ElementLocators.CHECKBOXES)
        for checkbox in checkboxes:
            if checkbox.is_selected():
                checkbox.click()
                
            

           
           
         #  navigate to another page
         # Find and click the link/button that leads to the target page
         
            
    def is_employee_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains("Employee"))
        target_page_link = self.driver.find_element_by_xpath(ElementLocators.TARGET_PAGE_LINK)
        target_page_link.click()
        
        return "Employee" in self.driver.title
            
            
    def confirm(self):
        # Wait for the confirmation alert
        confirmation_alert = self.driver.switch_to.alert

# Get the text of the confirmation alert
        alert_text = confirmation_alert.text
        print("Confirmation alert text:", alert_text)

# Accept the confirmation (i.e., click OK)
        confirmation_alert.accept()
        


   
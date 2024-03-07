from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Pages.elements import ElementLocators
from selenium.webdriver.support import expected_conditions as EC
import urllib
import time

class manager_page:


    def __init__(self, driver):
        self.driver = driver
        
  
        
    def reach_team_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains("Employee"))
        target_page_link = self.driver.find_element_by_xpath(ElementLocators.TEAM_PAGE)
        target_page_link.click()
        
    def open_evalution(self):
        open_evaluation = self.driver.find_element_by_class_name(ElementLocators.OPEN_STATUS)
        open_evaluation.click()
        
    def navigate_to_manager_evalution(self,evaluation_date):
        evaluation_path = "/Supervisor/EditEvaluation"
        encoded_date = urllib.parse.quote(evaluation_date)  # Encode evaluation date if needed
        full_url = f"{self.base_url}{evaluation_path}?EvaluationDate={encoded_date}"
        self.driver.get(full_url) 
        
    def edit_evalution(self):
        
        edit_evaluation = self.driver.find_element_by_xpath(ElementLocators.EDIT_EVALUATION)
        edit_evaluation.click()
        
        # Add a wait to ensure the redirect to the edit page is complete
        time.sleep(2)  # Adjust the time as neede 
        
        checkboxes  = self.driver.find_element_by_xpath(ElementLocators.CHECKBOX_TABLE)
        # Iterate through each checkbox
        for checkbox in checkboxes:
        # Check if the checkbox is not checked
        
         if  checkbox.is_selected():
    # If not checked, mark it as checked
          checkbox.click()
         else:
               # If not selected, select it or choose another option
        # Here you can implement logic to choose another option
        # For simplicity, we just click to select it
          checkbox.click()
        

        save_evaluation = self.driver.find_element_by_xpath(ElementLocators.SAVE_EDIT)
        save_evaluation.click()
        
        
    def close_evalution(self):
        close_evaluation = self.driver.find_element_by_xpath(ElementLocators.CLOSE_EVALUATION)
        close_evaluation.click()
        
        
        
        
        
    
        
    
        
        
        
        
        
        
        
        
        
        



    
    
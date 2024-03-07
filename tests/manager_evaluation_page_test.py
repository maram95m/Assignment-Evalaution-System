import unittest
from selenium import webdriver
from Pages.manager_page import manager_page
from Pages.employee_page import employee_page
from Pages.base_page import base_page
from Pages.base_page import read_config

class TestManagerEvaluation(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
        self.manager_page = manager_page(self.driver)
        self.employee_page = employee_page(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_manager_evaluation(self):
        # 1. Login as Manager
        
        # Initialize the LoginPage object
        login = base_page(self.driver)
        # Read configuration
        config = read_config()
        
        credentials = config["manager"]
          
        login_url = config["login_url"]

        # Navigate to the login page
        login.navigate_to_login_page(login_url)
        login.enter_username(credentials['username'])
        login.enter_password(credentials['password'])
        login.submit_login_form()
            
        evaluation_manager_as_employee = employee_page(self.driver)
        evaluation_manager_as_employee.navigate_to_evaluation(base_page.evaluation_date)
        # Initialize the EvaluationPage object
        evaluation_manager =manager_page(self.driver)
        # 2. Navigate to Evaluation Page
        evaluation_manager.navigate_to_manager_evalution(base_page.evaluation_date)
        

     
    
        # 3. Provide Ratings and Comments
        evaluation_manager_as_employee.enter_rating(rating_value=5)
        evaluation_manager_as_employee.enter_feedback_comments(comment1="Great work!",comment2="bad ",comment3="need to be")

        # 4. Submit Evaluation
        evaluation_manager_as_employee.submit_evaluation()
        # 5. Verify Evaluation Reflects in Employee's History
        # Navigate to employee's evaluation history page
        evaluation_manager_as_employee.confirm()
        
        self.employee_page.navigate_to_evaluation_history()

        # Assert that manager's evaluation reflects in the history
        evaluation_data = self.employee_page.get_evaluation_data()
        self.assertIn("Great work!", evaluation_data, "Manager's evaluation comment not found in employee's history")
        
        
        evaluation_manager.navigate_to_manager_evalution(base_page.evaluation_date)
        evaluation_manager.reach_team_page()
        evaluation_manager.open_evalution()
        evaluation_manager.edit_evalution()
        evaluation_manager.close_evalution()
        
        

if __name__ == "__main__":
    unittest.main()

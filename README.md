
# Respository: 
https://github.com/maram95m/Project

# Branches:
main
# Install dependencies:
pip install pytest 


## Usage
# Run the command in terminal 
#To run the tests, use the following command:


# pytest(e.g)
python -m pytest .\test_login.py


# pytest with report:

python -m pytest  --alluredir=./allure-results
allure serve allure-results


# unittest with report:

python -m unittest .\tests\login_page_test.py


## Configuration

Before running the tests, make sure to configure the following config, data json files:
  - 'config.json' : using to store all the variable on and read it from this json file
  - 'config.json' : contains the data of users


## Test Structure

The tests are organized as follows:

# `tests/`
  
  - `login_page_test`: Contains test cases for the login functionality.
  - 'employee_evaluation_page_test': to test the employee evaultion & submition
  - 'manager_evaluation_page_test': to test the manager evaultion & open/edit/close operation
  - 'history_page_test' : to check that all the checked checkboxes in the table are stored correctly in another page as history data
  - 'cross_browser_test' : verifies that the website works correctly across different web browsers.
  - 'user_roles_test' : to check the user validation as (login as employee or manager)
  - 'allure-report' folders: generate the reposrt using allure library.
  - 'config.json' : using to store all the variable on and read it from this json file
  - 'config.json' : contains the data of users
  
## Classes Structure

the pages directory contains multiple files:
- login_page:   The class abstracts away the details of the login process
- history_page:   The class contains functionality needs for history process 
- evaluation_page: The class contains functionality needs for evaluation process 
- cross_browser: to ensure consistent behavior and functionality across multiple platforms.


  ## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

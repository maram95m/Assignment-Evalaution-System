from selenium.webdriver.common.by import By
class ElementLocators:
    EMPLOYEE_NAME_INPUT = "username"
    EMPLOYEE_PASSWORD_INPUT = "password" 
    LOGIN_BUTTON ='//*[@id="myform"]/button'
    TARGET_PAGE_LINK = '/html/body/div[3]/div[1]/div/ul/li[2]/a/span[1]'
    TEAM_PAGE = '/html/body/div[3]/div[1]/div/ul/li[4]/a/span[1]'
    CHECKBOXES = "//table[@id='assets-data-table']//input[@id='Outstanding']"
    CHECKBOX_TABLE = '//*[@id="assets-data-table"]'
    CHECKBOX_ID = 'Outstanding'
    SUBMIT_BUTTON = 'saveButton'
    TARGET_PAGE_HISTORY = '/html/body/div[3]/div[1]/div/ul/li[3]/a'
    VIEW_BUTTON =  "//*[@id='view']"
    HISTORY_DATA_ELEMENTS =  "//div[@class='checked']"
    TEXTAREA_LIKE = "Likes"
    TEXTAREA_DISLIKE = "Dislikes"
    IMPROVMENTS = "Improvements"
    OPEN_STATUS = 'btn btn-sm btn-circle btn-info'
    NOT_ANSWER ='bootbox-body'
    EDIT_EVALUATION = '/html/body/div[3]/div[2]/div/div[7]/button[1]'
    CLOSE_EVALUATION = '//*[@id="CLOSEbtn"]'
    SAVE_BUTTTON = '//*[@id="saveButton"]'
    SAVE_EDIT = '//*[@id="SaveReview"]'
    textarea_locators = [
        (By.ID, '"Likes"'),
        (By.ID, 'Dislikes'),
        (By.ID,'Improvements')
       
    ]
   
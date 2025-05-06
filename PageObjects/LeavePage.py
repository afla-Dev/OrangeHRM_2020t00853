from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    leave_header_xpath = '//h6[text()="Leave"]'
    leave_page_title = "OrangeHRM"
    
    # Actions
    def is_leave_header_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.leave_header_xpath))).is_displayed()
        except:
            return False
    
    def get_leave_page_title(self):
        return self.driver.title
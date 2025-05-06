from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    dashboard_header_xpath = '//h6[text()="Dashboard"]'
    my_leave_icon_xpath = '//button[@title="My Leave"]'
    user_dropdown_xpath = '//span[@class="oxd-userdropdown-tab"]'
    logout_link_xpath = '//a[text()="Logout"]'
    
    dashboard_page_title = "OrangeHRM"
    
    # Actions
    def is_dashboard_header_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dashboard_header_xpath))).is_displayed()
        except:
            return False
    
    def click_my_leave_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.my_leave_icon_xpath))).click()
    
    def click_user_dropdown(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_dropdown_xpath))).click()
    
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath))).click()
    
    def get_dashboard_page_title(self):
        return self.driver.title
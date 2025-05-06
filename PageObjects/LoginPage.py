from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = '//button[@type="submit"]'
    login_page_title = "OrangeHRM"
    
    # Actions
    def set_username(self, username):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.textbox_username_name))).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
    
    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    
    def get_login_page_title(self):
        return self.driver.title
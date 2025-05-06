import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Utilities.readProperties import ReadConfig
import time

class Test_001_Login:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    
    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        
        actual_title = self.login_page.get_login_page_title()
        self.driver.close()
        
        assert actual_title == "OrangeHRM", f"Title mismatch. Expected: OrangeHRM, Actual: {actual_title}"
    
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        
        dashboard_visible = self.dashboard_page.is_dashboard_header_visible()
        self.driver.close()
        
        assert dashboard_visible, "Login failed or Dashboard not loaded"

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
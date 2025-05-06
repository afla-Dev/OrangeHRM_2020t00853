import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
from Utilities.readProperties import ReadConfig
import time

class Test_002_Leave:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    
    def test_leave_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        
        # Login
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        
        # Go to Leave page
        self.dashboard_page = DashboardPage(self.driver)
        self.dashboard_page.click_my_leave_icon()
        
        # Verify Leave page
        self.leave_page = LeavePage(self.driver)
        leave_visible = self.leave_page.is_leave_header_visible()
        
        # Logout
        self.dashboard_page.click_user_dropdown()
        self.dashboard_page.click_logout()
        
        self.driver.close()
        
        assert leave_visible, "Leave page not loaded properly"

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
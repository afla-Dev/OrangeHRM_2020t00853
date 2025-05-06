import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Utilities.readProperties import ReadConfig

class Test_003_Logout:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.fixture()
    def setup(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        
        # Login first
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()

        # Verify login success
        self.dashboard_page = DashboardPage(self.driver)
        assert self.dashboard_page.is_dashboard_header_visible(), "Login failed"

        # Logout
        self.dashboard_page.click_user_dropdown()
        self.dashboard_page.click_logout()

        # Verify logout success
        assert "login" in self.driver.current_url.lower(), "Logout failed - Not redirected to login page"
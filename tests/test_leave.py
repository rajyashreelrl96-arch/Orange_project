from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

from utils.config import (USERNAME, PASSWORD)

class TestLeave:
    def test_assign_leave(self, driver):
        login = LoginPage(driver)
        login.login(USERNAME, PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.open_leave()

        leave = LeavePage(driver)
        leave.assign_leave("Ravi M B")
        assert "leave" in \
               driver.current_url.lower()
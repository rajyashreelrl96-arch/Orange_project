from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from utils.config import (USERNAME, PASSWORD)
from utils.data_generator import (random_username)

class TestAdminPage:

    def test_create_user(self, driver):
        login = LoginPage(driver)
        login.login(USERNAME, PASSWORD)
        dashboard = DashboardPage(driver)

        username = random_username()
        dashboard.open_admin()

        admin = AdminPage(driver)

        admin.create_user("Ravi M B",
                          username,
                         "rajya123"
        )

        admin.search_user(
            username
        )

        assert admin.user_exists(
            username)
   
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD

class TestLogin:
    @pytest.mark.parametrize(
        "user,pwd",
        [
            (USERNAME, PASSWORD),
            ("wrongAdmin", "wrong123")
        ]
    )

    def test_login(self, driver, user, pwd):
        login = LoginPage(driver)
        login.login(user, pwd)

        if pwd == PASSWORD:
            dashboard = DashboardPage(driver)
            assert dashboard.dashboard_visible()
        else:

            assert "Invalid" in \
                   login.get_error_message()


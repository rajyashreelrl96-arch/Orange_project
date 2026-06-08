from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage
from utils.config import (USERNAME, PASSWORD)

class TestMyInfo:
     def test_open_myinfo(self, driver):
         login = LoginPage(driver)
         login.login(USERNAME, PASSWORD)

         dashboard = DashboardPage(driver)
         dashboard.open_my_info()

         my_info = MyInfoPage(driver)
         assert my_info.verify_sections()
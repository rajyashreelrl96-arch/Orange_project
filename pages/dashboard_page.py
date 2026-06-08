from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    dashboard_menu = (By.XPATH,  "//span[text()='Dashboard']")
    admin_menu = (By.XPATH,  "//span[text()='Admin']")
    leave_menu = (By.XPATH,  "//span[text()='Leave']")
    my_info_menu = (By.XPATH,  "//span[text()='My Info']")
    logout_icon = (By.XPATH,   "//i[contains(@class,'userdropdown-icon')]")
    logout_btn = (By.XPATH,   "//a[text()='Logout']")

    def dashboard_visible(self):
        return self.is_visible(
            self.dashboard_menu
        )

    def open_admin(self):
        self.click(
            self.admin_menu
        )

    def open_leave(self):
        self.click(
            self.leave_menu
        )

    def open_my_info(self):
        self.click(
            self.my_info_menu
        )

    def logout(self):
        self.click(
            self.logout_icon
        )

        self.click(
            self.logout_btn
        )
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username = (By.NAME, "username")
    password = (By.NAME, "password")

    login_btn = (By.XPATH, "//button[@type='submit']")
    error_msg = (By.XPATH, "//p[contains(@class,'alert-content-text')]")
    success_msg = (By.XPATH, "//*[contains(text(),'Reset Password link sent successfully')]")

    def login(self, user, pwd):
        self.enter_text(
            self.username,
            user
        )

        self.enter_text(
            self.password,
            pwd
        )

        self.click(
            self.login_btn
        )

    def forgot_password(self, username):
        self.click(
            self.forgot_pwd
        )

        self.enter_text(
            self.username,
            username
        )

        self.click(
            self.login_btn
        )

    def get_error_message(self):
        return self.get_text(
            self.error_msg
        )

    def get_success_message(self):
        return self.get_text(
            self.success_msg
        )



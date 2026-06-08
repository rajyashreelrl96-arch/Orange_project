from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AdminPage(BasePage):

    add_btn = (By.XPATH,   "//button[contains(@class,'oxd-button') and normalize-space()='Add']")
    username_field = (By.XPATH,  "//label[text()='Username']/following::input[1]")
    save_btn = (By.XPATH,  "//button[@type='submit']")
    success_pop = (By.XPATH, "//p[.='Successfully Saved']")
    search_username_field =  (By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    search_btn = (By.XPATH,  "//button[normalize-space()='Search']")

    def create_user(self, employee_name, username, password):

        self.click(self.add_btn)

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h6[text()='Add User']"
                )
            )
        )

        # USER ROLE

        self.click((
            By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]"

        ))

        self.click((
            By.XPATH, "//div[@role='listbox']//span[text()='Admin']"

        ))

        # EMPLOYEE NAME

        employee_field = (By.XPATH, "//input[@placeholder='Type for hints...']")

        self.enter_text(employee_field, employee_name)

        #wait until the loading option disappears
        self.wait.until_not(EC.text_to_be_present_in_element(
            (By.XPATH, "//div[@role='option']"),
        "Searching")
        )
        #wait for actual employee suggestion

        employee_option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@role='option' and not(contains(.,'No Records Found'))]"
                )
            )
        )

        print("Employee found:", employee_option.text)

        employee_option.click()


        # STATUS

        self.click((
            By.XPATH,  "//label[text()='Status']//following::div[contains(@class,'oxd-select-text')][1]"
        ))

        self.click((
            By.XPATH,
            "//span[text()='Enabled']"
        ))

        # USERNAME

        self.enter_text(
            self.username_field,
            username
        )

        # PASSWORD

        self.enter_text(
            (
                By.XPATH,  "//label[text()='Password']/following::input[1]"
            ),
            password
        )
        #CONFIRM PASSWORD
        self.enter_text(
            (
                By.XPATH,  "//label[text()='Confirm Password']/following::input[1]"
            ),
            password
        )

        self.click(
            self.save_btn
        )


        # WAIT SUCCESS

        self.wait.until(
            EC.presence_of_element_located(
                self.success_pop
            )
        )

    def search_user(self, username):
        self.enter_text(
            self.search_username_field,
            username
        )
        self.click(
            self.search_btn
        )
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'oxd-loading-spinner')]")
            )
        )

    def user_exists(self, username):
        locator = (
            By.XPATH, f"//div[contains(@class,'oxd-table-card')]//*[contains(text(),'{username}')]"
            # By.XPATH, f"//div[@role='row']//div[contains(text(),'{username}')]"
        )

        return self.is_visible(locator)
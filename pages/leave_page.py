from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from pages.base_page import BasePage

class LeavePage(BasePage):

    assign_leave_menu = (By.XPATH,  "//a[text()='Assign Leave']")
    assign_btn = (By.XPATH,  "//button[normalize-space()='Assign']")
    ok_btn = (By.XPATH,  "//button[normalize-space()='Ok']")

    def assign_leave(self, employee_name):
        self.click(
            self.assign_leave_menu
        )
        employee = (By.XPATH,  "//input[@placeholder='Type for hints...']")

        self.enter_text(
            employee,
            employee_name
        )

        employee_option = self.wait.until(EC.element_to_be_clickable
                                          ((By.XPATH, "//div[@role='option' and not(contains(.,'No Records Found'))]")))
        print("Employee:", employee_option.text)
        employee_option.click()

        # Leave Type

        self.click((
            By.XPATH,
            "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]"))

        # self.click((By.XPATH, "//div[contains(text(), 'CAN - Matternity')]"))

        self.click((By.XPATH, "//span[contains(text(),'CAN')]"))

        # FROM DATE

        from_date = self.wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[1]")))

        from_date.send_keys(
            Keys.CONTROL + "a"
        )

        from_date.send_keys(
            "2026-30-04"
        )

        # TO DATE

        to_date = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")))

        to_date.send_keys(
            Keys.CONTROL + "a"
        )

        to_date.send_keys(
            "2026-30-04"
        )

        self.click(self.assign_btn)
        print("Assign clicked")


        self.click(
            self.assign_btn
        )
        print("OK clicked")


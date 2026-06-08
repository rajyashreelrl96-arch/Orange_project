from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ClaimPage(BasePage):

    def initiate_claim(self, amount, reason):

        # Claim menu
        self.click((By.XPATH,"//a[contains(@href,'Claim')]"))

        # Submit Claim
        self.click((By.XPATH,"//a[contains(.,'Submit Claim')]"))

        # Event dropdown
        self.click((
            By.XPATH,
            "(//div[contains(@class,'oxd-select-text')])[1]"
        ))

        self.click((
            By.XPATH,
            "//span[text()='Accommodation']"
        ))

        # Currency dropdown
        self.click((
            By.XPATH,
            "(//div[contains(@class,'oxd-select-text')])[6]"
        ))

        # Select first currency option
        currency = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "(//div[@role='listbox']//span)[1]"
            ))
        )

        currency.click()

        # Click CREATE FIRST
        self.click((
            By.XPATH,
            "//button[normalize-space()='Create']"
        ))

        submit = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[@type='button'][.=' Submit ']"
            )))

        # Submit
        submit.click()

        # back
        back = self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "//button[@type='button'][.=' Back ']")))
        back.click()


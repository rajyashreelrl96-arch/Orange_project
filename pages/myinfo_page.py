from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyInfoPage(BasePage):

    personal_details = (By.XPATH,  "//*[contains(text(),'Personal Details')]")
    contact_details = (By.XPATH,  "//*[contains(text(),'Contact Details')]")
    emergency_contacts = (By.XPATH, "//*[contains(text(),'Emergency Contacts')]")
    dependents = (By.XPATH, "//*[contains(text(),'Dependents')]")
    qualifications = (By.XPATH,   "//*[contains(text(),'Qualifications')]")

    def verify_sections(self):
        return all([

            self.is_visible(
                self.personal_details
            ),

            self.is_visible(
                self.contact_details
            ),

            self.is_visible(
                self.emergency_contacts
            ),

            self.is_visible(
                self.dependents
            ),

            self.is_visible(
                self.qualifications
            )
        ])



from pages.login_page import LoginPage
from pages.claim_page import ClaimPage
from utils.config import (USERNAME, PASSWORD)

class TestClaim:

    def test_claim(self, driver):
        login = LoginPage(driver)
        login.login(USERNAME, PASSWORD)

        claim = ClaimPage(driver)

        claim.initiate_claim(
            "2500",
            "Accommodation"
        )
        print(driver.current_url)
        print(driver.title)

        # assert claim.claim_submitted()
        #
        # assert claim.claim_history_visible()
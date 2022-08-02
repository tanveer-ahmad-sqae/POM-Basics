from tests.basetest import BaseTest
from pages.page_signup import SignupPage
import time


class SignupTestCases(BaseTest):

    def setUp(self):
        super().setUp()
        self.signup = SignupPage(self.driver)

    def signup_successfully(self):
        time.sleep(3)
        self.signup.enterName('rubeet Husnain')

    def tearDown(self):
        self.driver.quit()


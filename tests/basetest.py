import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://www.google.com"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.base_url)


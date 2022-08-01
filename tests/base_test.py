import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    base_url = "https://seleniumautomation.inone.useinsider.com/"

    def setUp(self):
        driver_location = "/usr/bin/chromedriver"
        binary_location = "/usr/bin/google-chrome"
        option = webdriver.ChromeOptions()
        #option.add_argument("--incognito")
        option.add_argument("--allow-running-insecure-content")
        option.binary_location = binary_location
        self.driver = webdriver.Chrome(executable_path=driver_location, options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.close()

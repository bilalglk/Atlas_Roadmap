from datetime import datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.date = datetime.now()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def enter(self, text, *locator):
        self.find_element(*locator).send_keys(text)

        return self

    def click(self, *locator):
        self.find_element(*locator).click()

    def hover(self, element="", *locator):
        if locator == "":
            element = self.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            ActionChains(self.driver).move_to_element(element).perform()
        return self

    def find_elements(self, index, *locator):
        return self.driver.find_elements(*locator)[index]

    def wait_for_element_clickable(self, locator, message=""):
        return self.wait.until(ec.element_to_be_clickable(locator), message)

    class SwitchFrame:
        def __init__(self, driver, element):
            self.driver = driver
            self.element = element

        def __enter__(self):
            self.driver.switch_to.frame(self.element)

        def __exit__(self, type, value, traceback):
            self.driver.switch_to.parent_frame()

    def switch_frame(self, locator):
        return self.SwitchFrame(self.driver, self.wait_for_element_visible(locator))

    def wait_for_element_visible(self, locator, message=""):
        return self.wait.until(ec.visibility_of_element_located(locator), message)

    def generate_campaign_name(self):
        given_name = "%s%s%s" % ("Test", "-", self.date.second)

        return str(given_name)

    def scroll(self, *locator):
        self.enter(Keys.END, *locator)
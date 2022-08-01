from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.panel_page import PartnerPage


class LoginPage(BasePage):
    EMAIL_AREA = (By.ID, 'email')
    PASSWORD_AREA = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    RESET_PASSWORD = (By.ID, 'reset-password')

    def login_button_loaded(self):
        self.wait_for_element_clickable(self.LOGIN_BUTTON)
        self.wait_for_element_clickable(self.RESET_PASSWORD)

    def entering_email_password(self, email, password):
        self.enter(email, *self.EMAIL_AREA)
        self.enter(password, *self.PASSWORD_AREA)

    def clicking_login_button(self):
        self.wait_for_element_clickable(self.LOGIN_BUTTON).click()

        return PartnerPage(self.driver)
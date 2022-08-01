from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.test_link_page import InstoryPage


class PartnerPage(BasePage):
    OPTIMIZE = (By.XPATH, '//span[text()="Optimize"]')
    INSTORY = (By.XPATH, '//span[text()="InStory"]')
    WAITING_SIDE_MENU_ELEMENTS = (By.CLASS_NAME, 'in-sidebar-wrapper__groups')
    WAITING_AB_PERSONALIZATION = (By.ID, 'ab-redirect-button-icon')
    WAITING_GRAPHS = (By.ID, 'custom-line')

    def waited_elements(self):
        self.wait_for_element_visible(self.WAITING_SIDE_MENU_ELEMENTS, "Side menu elements are not visible on Partner page")
        self.wait_for_element_visible(self.WAITING_GRAPHS, "Graphs are not visible on Partner page")
        self.wait_for_element_visible(self.WAITING_AB_PERSONALIZATION, "A/B Personalization is not visible on Partner page")

    def select_experience_on_side_menu(self):
        self.wait_for_element_clickable(self.WAITING_SIDE_MENU_ELEMENTS)
        self.wait_for_element_clickable(self.find_elements(2, *self.WAITING_SIDE_MENU_ELEMENTS)).click()
        self.select_experience_sub_menu_items()

        return InstoryPage(self.driver)

    def select_experience_sub_menu_items(self):
        self.wait_for_element_clickable(self.OPTIMIZE).click()
        self.select_optimize_sub_menu_items()

    def select_optimize_sub_menu_items(self):
        self.click(*self.INSTORY)
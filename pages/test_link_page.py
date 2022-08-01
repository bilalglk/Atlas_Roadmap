import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.action_builder_page import ActionBuilderPage
from pages.base_page import BasePage


class InstoryPage(BasePage):
    CREATE_BUTTON = (By.ID, 'create-mobile-campaign')
    CAMPAIGN_NAME_TEXT_AREA = (By.ID, 'campaign-name')
    SELECTED_PLATFORM = (By.XPATH, "//button[@value='web']")
    ACCEPT_BUTTON = (By.ID, 'accept')
    PAGE_RULES = (By.XPATH, './/*[contains(@class, "page-rules")]')
    CONDITION_LIST = (By.ID, 'conditionList0')
    CONDITION_SEARCHING_AREA = (By.ID, 'conditionList0-search')
    OPERATOR_LIST = (By.ID, 'operatorList0')
    OPERATOR_SELECTION = "//*[contains(@class, 'in-dropdown')]//a[text() = ' {} ']"
    SAVE_AND_CONTINUE_BUTTON = (By.ID, 'save-and-next')
    ADD_NEW_VARIANT_BUTTON = (By.ID, 'add-new-variation')
    SALES_GOAL = (By.XPATH, "//*[@for='0']")
    WAITING_EXISTING_VARIANT = (By.ID, 'choose-existing-variation')
    LANGUAGE_LIST_SELECTION = (By.ID, 'personalization-language')
    ACTIVATION_TIME_SELECTION = (By.XPATH, "//*[@for='Never Ends']")
    DISPLAY_SETTINGS = (By.XPATH, './/*[contains(@class, "qa-accordion")]//p[contains(text(), "DISPLAY SETTINGS")]')
    WHEN_ACTIVE_DAYS = (By.XPATH, "//*[@for = 'When active, display the personalization only on selected days.']")
    ADVANCE_SETTINGS = (By.XPATH, './/*[contains(@class, "qa-accordion")]//p[contains(text(), " Advanced Settings ")]')
    SELECT_DAY = (By.XPATH, "//*[@for='Monday']")
    PRIORITY = (By.ID, 'priority')
    PRIORITY_SELECT = 'priority-{}'
    BODY = (By.TAG_NAME, 'body')
    ACTIVATION_STATUS = (By.XPATH, '//*[@for="Test"]')
    CAMPAIGN_DETAILS = (By.XPATH, "//*[contains(@class, 'vuetable-body')]//*[contains(text(), 'Details')]")
    NOTE_TEXT_BOX = (By.ID, 'note')
    LAUNCH_CAMPAIGN = (By.ID, 'save-and-next')
    SEARCH_INPUT = (By.ID, 'search-value')
    CAMP_STATUS = (By.XPATH, './/*[contains(@class, "camp-status")]')
    TEST_LINK = (By.XPATH, '//td[contains(@class, "test-link")]')
    CAMP_NAME = (By.CLASS_NAME, 'in-modal-wrapper__title')
    CAMP_PRIORITY = (By.ID, 'priority-value')
    CAMP_RULES = (By.CLASS_NAME, 'personalization-rule-0')
    CAMP_NOTE = (By.CLASS_NAME, 'personalization-note')
    DETAIL_CLOSE = (By.CLASS_NAME, 'qa-close')
    TEST_LINK_VARIATION_GROUP_BUTTONS = (By.CSS_SELECTOR, '.in-box .clearfix')
    TEST_LINK_DOMAIN_URL = (By.CSS_SELECTOR, '.in-box .clearfix a')
    USER_SETTINGS = (By.CSS_SELECTOR, 'li:nth-child(6) > a')
    GENERATE = (By.LINK_TEXT, 'Generate')
    CAMPAIGN_VISIBILITY = (By.CLASS_NAME, 'inspector-personalization-visible')
    CAMPAIGN_ID = (By.CSS_SELECTOR, 'td.personalization-id span')
    CAMPAIGN_CLASS = '//div[contains(@class, "{}")]'

    def __init__(self, driver):
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.CREATE_BUTTON) else False

    def create_campaign(self, campaign_name):
        self.click(*self.CREATE_BUTTON)
        self.enter_campaign_name(campaign_name)

    def enter_campaign_name(self, campaign_name):
        self.enter(campaign_name, *self.CAMPAIGN_NAME_TEXT_AREA)
        self.select_platform()
        self.create_button()

    def select_platform(self):
        self.click(*self.SELECTED_PLATFORM)

    def create_button(self):
        self.click(*self.ACCEPT_BUTTON)

    def navigating_to_rule_section(self):
        time.sleep(3)
        self.click_save_and_continue()
        time.sleep(5)
        self.wait_for_element_clickable(self.PAGE_RULES).click()

        return self

    def select_condition(self, condition):
        self.click(*self.CONDITION_LIST)
        self.enter(condition, *self.CONDITION_SEARCHING_AREA).enter(Keys.ENTER, *self.CONDITION_SEARCHING_AREA)

        return self

    def select_operator(self, operator):
        self.click(*self.OPERATOR_LIST)
        self.click(By.XPATH, self.OPERATOR_SELECTION.format(operator))

    def click_save_and_continue(self):
        time.sleep(5)
        self.wait_for_element_clickable(self.SAVE_AND_CONTINUE_BUTTON).click()

        return self

    def adding_new_variant(self):
        self.wait_for_element_visible(self.WAITING_EXISTING_VARIANT)
        self.click(*self.ADD_NEW_VARIANT_BUTTON)
        time.sleep(15)

        return ActionBuilderPage(self.driver)

    def select_goal(self):
        time.sleep(6)
        self.wait_for_element_clickable(self.SALES_GOAL).click()

    def select_personalization_language(self, language):
        self.click(*self.LANGUAGE_LIST_SELECTION)
        self.click(By.LINK_TEXT, '{}'.format(language))

    def select_activation_time(self):
        self.wait_for_element_clickable(self.ACTIVATION_TIME_SELECTION).click()

    def adjusting_display_settings(self):
        self.scroll(*self.BODY)
        time.sleep(5)
        self.wait_for_element_clickable(self.DISPLAY_SETTINGS).click()
        time.sleep(5)
        self.wait_for_element_clickable(self.WHEN_ACTIVE_DAYS).click()
        time.sleep(5)
        self.wait_for_element_clickable(self.SELECT_DAY).click()

    def adjusting_priority(self, priority):
        self.scroll(*self.BODY)
        time.sleep(3)
        self.wait_for_element_clickable(self.ADVANCE_SETTINGS).click()
        self.wait_for_element_clickable(self.PRIORITY).click()
        self.wait_for_element_clickable((By.CLASS_NAME, self.PRIORITY_SELECT.format(priority))).click()

    def adjusting_activation_status(self):
        time.sleep(3)
        self.wait_for_element_clickable(self.ACTIVATION_STATUS).click()

    def adding_note(self, note):
        self.enter(note, *self.NOTE_TEXT_BOX)

    def launching_campaign(self):
        time.sleep(3)
        self.wait_for_element_clickable(self.LAUNCH_CAMPAIGN).click()

    def searching_campaign(self, name):
        self.wait_for_element_clickable(self.SEARCH_INPUT)
        self.enter(name, *self.SEARCH_INPUT)
        time.sleep(2)

    def getting_campaign_status(self):
        return self.wait_for_element_visible(self.CAMP_STATUS).text

    def test_link_is_present(self):
        return self.wait_for_element_clickable(self.TEST_LINK)

    def go_to_campaign_details(self):
        self.wait_for_element_clickable(self.CAMPAIGN_DETAILS).click()

        return self

    def get_campaign_name(self):
        return self.wait_for_element_visible(self.CAMP_NAME).text

    def get_campaign_priority(self):
        return self.wait_for_element_visible(self.CAMP_PRIORITY).text

    def get_campaign_rules(self):
        return self.wait_for_element_visible(self.CAMP_RULES).text

    def get_campaign_note(self):
        return self.wait_for_element_visible(self.CAMP_NOTE).text

    def close_detail_side_menu(self):
        self.click(*self.DETAIL_CLOSE)

    def click_test_link(self):
        time.sleep(1)
        self.wait_for_element_clickable(self.TEST_LINK).click()

    def go_to_test_link(self):
        self.wait_for_element_clickable(self.TEST_LINK_VARIATION_GROUP_BUTTONS)
        self.hover(self.find_elements(0, *self.TEST_LINK_VARIATION_GROUP_BUTTONS))
        self.driver.get(self.find_elements(0, *self.TEST_LINK_DOMAIN_URL).get_attribute('href'))

        return self

    def generating_campaign(self):
        i = 0
        while i < 3:
            self.wait_for_element_clickable(self.USER_SETTINGS).click()
            self.wait_for_element_clickable(self.GENERATE).click()
            time.sleep(14)
            i = i + 1

    def get_campaign_visibility(self):
        return self.wait_for_element_visible(self.CAMPAIGN_VISIBILITY).text

    def get_campaign_id(self):
        return self.find_elements(0, *self.CAMPAIGN_ID).text

    def is_present_campaign_class(self, campaign_id):
        return self.wait_for_element_clickable((By.XPATH, self.CAMPAIGN_CLASS.format(campaign_id)))

    def test_link_campaign_control(self, campaign_id):
        time.sleep(2)
        camp_local_storage = self.driver.execute_script("return spApi.storageData('sp-camp-{}')".format(campaign_id))
        if camp_local_storage:
            return camp_local_storage
        else:
            return ''
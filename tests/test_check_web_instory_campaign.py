from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestCheckWebInstoryCampaign(BaseTest):
    """
    1. Log in the panel, select Optimize and go to Desktop Instory
    2. Create Instory campaign
    3. Fill all steps till Launch step
    4. Change campaign language, date&time, display settings, add priority and notes
    5. Go to do list and check campaign status is Test and is present in Test link menu
    6. Open campaign's details and check all information that was filled during launch is present there
    7. Go to website with the test link of the campaign
    8. Verify that campaign is visible in storage and class existence control
    """

    EMAIL = "-----"
    PASSWORD = "-------"
    condition = "Page Type"
    operator = "is"
    language = "All Languages"
    page_condition = "All Pages"
    priority = "0"
    note = "Atlas Roadmap, 9th Homework."
    campaign_status = "Visible"

    def test_check_instory_campaign(self):
        """Test checks, all the steps should be followed while creating an InStory campaign on panel."""
        print("1. Login the panel, navigated to the Campaign List Page.")
        login_page = LoginPage(self.driver)
        login_page.login_button_loaded()
        login_page.entering_email_password(self.EMAIL, self.PASSWORD)
        panel_page = login_page.clicking_login_button()
        print("1. Logged in & navigated to the Campaign List, successfully.")

        print("2. Creating an InStory campaign.")
        campaign_name = panel_page.generate_campaign_name()
        panel_page.waited_elements()
        instory_page = panel_page.select_experience_on_side_menu()
        instory_page.create_campaign(campaign_name)
        print("2. InStory campaign was created successfully!")

        print("3. Filling all the steps until the Launch step")
        rules_tab = instory_page.navigating_to_rule_section()
        rules_tab.select_condition(self.condition).select_operator(self.operator)
        design_pages = rules_tab.click_save_and_continue()
        action_builder_page = design_pages.adding_new_variant()
        action_builder_page.selecting_instory_template()
        action_builder_page.clicking_ok_button()
        action_builder_page.clicking_insert_after_element()
        action_builder_page.clicking_save_button()
        goals_tab = design_pages.click_save_and_continue()
        goals_tab.select_goal()
        launch_tab = goals_tab.click_save_and_continue()
        print("3. Process until the Launch step was filled, successfully!")

        print("4. Defining all the launch steps")
        launch_tab.select_personalization_language(self.language)
        launch_tab.select_activation_time()
        launch_tab.adjusting_display_settings()
        launch_tab.adjusting_priority(self.priority)
        launch_tab.adjusting_activation_status()
        launch_tab.adding_note(self.note)
        launch_tab.launching_campaign()
        instory_page.searching_campaign(campaign_name)
        instory_page.generating_campaign()
        print("4. All the launch steps were defined, successfully!")

        print("5. Navigate to the campaigns list, check if campaign's status is Test also the same status presents in "
              "Test link menu")
        self.assertEqual("Test", instory_page.getting_campaign_status(), "Campaign status doesn't match.")
        self.assertTrue(instory_page.test_link_is_present())
        print("5. Navigated to the campaigns, campaign's status is Test, also the same status presents in Test link "
              "menu")

        print("6. Opens campaign detail window and checks all the informations that were filled during panel process.")
        details_page = instory_page.go_to_campaign_details()
        camp_id = details_page.get_campaign_id()
        self.assertEqual(campaign_name, details_page.get_campaign_name(), "Campaign name doesn't match.")
        self.assertEqual(self.priority, details_page.get_campaign_priority(), "Campaign priority doesn't match.")
        self.assertEqual(self.condition + " " + self.operator + " " + self.page_condition,
                         details_page.get_campaign_rules(), "Campaign rules doesn't match.")
        self.assertEqual(self.note, details_page.get_campaign_note(), "Campaign note doesn't match.")
        details_page.close_detail_side_menu()
        print("6. Campaign's details were checked successfully!")

        print("7. Navigates to the website by using test link.")
        instory_page.click_test_link()
        campaign_page = instory_page.go_to_test_link()
        self.assertEqual(self.campaign_status, campaign_page.get_campaign_visibility(), "Campaign visibility doesn't "
                                                                                        "match.")
        print("7. Navigated to the website by using test link, successfully!")

        print("8. Checks, whether the campaign is visible on the test link but also in storage, too.")
        self.assertTrue(campaign_page.is_present_campaign_class(camp_id), "Campaign class doesn't match.")
        local_storage = campaign_page.test_link_campaign_control(camp_id)
        self.assertIn('"step1-displayed":true', local_storage, 'No display template log in local storage!')
        print("8. Campaign visibility, in storage and class presence were checked, successfully!")

    def tearDown(self):
        self.driver.close()
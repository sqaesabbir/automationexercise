from .base_page import BasePage
from typing import Dict

class SignupPage(BasePage):
    # Locators
    ACCOUNT_INFO_HEADER = "h2.title"
    TITLE_MR = "input#id_gender1"
    TITLE_MRS = "input#id_gender2"
    PASSWORD = "input[type='password']"
    DAYS = "select#days"
    MONTHS = "select#months"
    YEARS = "select#years"
    NEWSLETTER = "input#newsletter"
    SPECIAL_OFFERS = "input#optin"
    FIRST_NAME = "input#first_name"
    LAST_NAME = "input#last_name"
    COMPANY = "input#company"
    ADDRESS1 = "input#address1"
    ADDRESS2 = "input#address2"
    COUNTRY = "select#country"
    STATE = "input#state"
    CITY = "input#city"
    ZIPCODE = "input#zipcode"
    MOBILE_NUMBER = "input#mobile_number"
    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
    ACCOUNT_CREATED_MESSAGE = "h2.title"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    
    def fill_account_details(self, user_data: Dict[str, str]):
        """Fill all account details"""
        # Wait for form to be fully loaded
        self.wait_for_element(self.ACCOUNT_INFO_HEADER)
        
        # Personal Information
        self.click(self.TITLE_MR if user_data.get('title') == 'Mr' else self.TITLE_MRS)
        self.fill(self.PASSWORD, user_data['password'])
        
        # Date of Birth
        if 'dob_day' in user_data:
            self.select_dropdown(self.DAYS, user_data['dob_day'])
        if 'dob_month' in user_data:
            self.select_dropdown(self.MONTHS, user_data['dob_month'])
        if 'dob_year' in user_data:
            self.select_dropdown(self.YEARS, user_data['dob_year'])
        
        # Newsletter and Special Offers
        if user_data.get('newsletter', True):
            self.click(self.NEWSLETTER)
        if user_data.get('special_offers', True):
            self.click(self.SPECIAL_OFFERS)
        
        # Address Information
        self.fill(self.FIRST_NAME, user_data['first_name'])
        self.fill(self.LAST_NAME, user_data['last_name'])
        if 'company' in user_data:
            self.fill(self.COMPANY, user_data['company'])
        self.fill(self.ADDRESS1, user_data['address'])
        if 'address2' in user_data:
            self.fill(self.ADDRESS2, user_data['address2'])
        self.select_dropdown(self.COUNTRY, user_data['country'])
        self.fill(self.STATE, user_data['state'])
        self.fill(self.CITY, user_data['city'])
        self.fill(self.ZIPCODE, user_data['zipcode'])
        self.fill(self.MOBILE_NUMBER, user_data['mobile_number'])
    
    def click_create_account(self):
        """Click create account button"""
        self.click(self.CREATE_ACCOUNT_BUTTON)
        self.wait_for_navigation()
    
    def verify_account_created(self) -> bool:
        """Verify account created message is visible"""
        try:
            self.wait_for_element(self.ACCOUNT_CREATED_MESSAGE)
            return "ACCOUNT CREATED!" in self.get_text(self.ACCOUNT_CREATED_MESSAGE)
        except:
            return False
    
    def click_continue(self):
        """Click continue button"""
        self.click(self.CONTINUE_BUTTON)
        self.wait_for_navigation()
    
    def verify_account_info_visible(self) -> bool:
        """Verify account information form is visible"""
        try:
            self.wait_for_element(self.ACCOUNT_INFO_HEADER)
            return "ENTER ACCOUNT INFORMATION" in self.get_text(self.ACCOUNT_INFO_HEADER)
        except:
            return False
    
    def select_dropdown(self, locator: str, value: str):
        """Select value from dropdown"""
        try:
            self.wait_for_element(locator)
            self.page.select_option(locator, value)
        except Exception as e:
            self.logger.error(f"Failed to select option in dropdown: {locator}")
            raise e 
from .base_page import BasePage

class HomePage(BasePage):
    # Locators
    PRODUCTS_LINK = "a[href='/products']"
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    CART_LINK = "a[href='/view_cart']"
    TEST_CASES_LINK = "a[href='/test_cases']"
    CONTACT_US_LINK = "a[href='/contact_us']"
    CATEGORY_WOMEN = "a[href='#Women']"
    CATEGORY_MEN = "a[href='#Men']"
    CATEGORY_KIDS = "a[href='#Kids']"
    SUBSCRIPTION_EMAIL = "input#susbscribe_email"
    SUBSCRIPTION_BUTTON = "button#subscribe"
    SUBSCRIPTION_SUCCESS = "div#success-subscribe"
    CONTACT_NAME = "input[data-qa='name']"
    CONTACT_EMAIL = "input[data-qa='email']"
    CONTACT_SUBJECT = "input[data-qa='subject']"
    CONTACT_MESSAGE = "textarea[data-qa='message']"
    CONTACT_SUBMIT = "input[data-qa='submit-button']"
    CONTACT_SUCCESS = "div.alert-success"
    SCROLL_UP_BUTTON = "i.fa-angle-up"
    LOGGED_IN_USER = "a:has-text('Logged in as')"
    DELETE_ACCOUNT = "a[href='/delete_account']"
    ACCOUNT_DELETED = "h2.title"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    LOGOUT_BUTTON = "a[href='/logout']"

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.automationexercise.com"

    def load(self):
        """Navigate to home page"""
        self.navigate(self.url)

    def click_products(self):
        """Click on Products link"""
        self.click(self.PRODUCTS_LINK)

    def click_signup_login(self):
        """Click on Signup / Login link"""
        self.click(self.SIGNUP_LOGIN_LINK)

    def click_cart(self):
        """Click on Cart link"""
        self.click(self.CART_LINK)

    def click_test_cases(self):
        """Click on Test Cases link"""
        self.click(self.TEST_CASES_LINK)

    def click_contact_us(self):
        """Click on Contact Us link"""
        self.click(self.CONTACT_US_LINK)

    def subscribe_newsletter(self, email: str):
        """Subscribe to newsletter"""
        self.fill(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIPTION_BUTTON)

    def is_subscription_successful(self) -> bool:
        """Check if subscription was successful"""
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)

    def select_category(self, category: str):
        """Select a category (Women, Men, or Kids)"""
        category_map = {
            "Women": self.CATEGORY_WOMEN,
            "Men": self.CATEGORY_MEN,
            "Kids": self.CATEGORY_KIDS
        }
        if category in category_map:
            self.click(category_map[category])
        else:
            raise ValueError(f"Invalid category: {category}")

    def verify_page_loaded(self) -> bool:
        """Verify home page is loaded"""
        return self.is_visible(self.PRODUCTS_LINK) and self.is_visible(self.SIGNUP_LOGIN_LINK)

    def fill_contact_form(self, contact_info: dict):
        """Fill and submit contact form"""
        self.fill(self.CONTACT_NAME, contact_info["name"])
        self.fill(self.CONTACT_EMAIL, contact_info["email"])
        self.fill(self.CONTACT_SUBJECT, contact_info["subject"])
        self.fill(self.CONTACT_MESSAGE, contact_info["message"])
        self.click(self.CONTACT_SUBMIT)

    def verify_contact_success(self) -> bool:
        """Verify contact form submission success"""
        return "Success! Your details have been submitted successfully." in self.get_text(self.CONTACT_SUCCESS)

    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        """Scroll to top of page"""
        self.page.evaluate("window.scrollTo(0, 0)")

    def click_scroll_up_button(self):
        """Click scroll up button"""
        self.click(self.SCROLL_UP_BUTTON)

    def verify_logged_in_as(self, username: str) -> bool:
        """Verify logged in as specific user"""
        return f"Logged in as {username}" in self.get_text(self.LOGGED_IN_USER)

    def click_delete_account(self):
        """Click delete account button"""
        self.click(self.DELETE_ACCOUNT)

    def verify_account_deleted(self) -> bool:
        """Verify account deleted message"""
        return "ACCOUNT DELETED!" in self.get_text(self.ACCOUNT_DELETED)

    def click_continue(self):
        """Click continue button"""
        self.click(self.CONTINUE_BUTTON)

    def click_logout(self):
        """Click logout button"""
        self.click(self.LOGOUT_BUTTON) 
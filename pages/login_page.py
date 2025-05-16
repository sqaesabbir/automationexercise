from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    LOGIN_FORM = "div.login-form"
    SIGNUP_FORM = "div.signup-form"
    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    ERROR_MESSAGE = "p[style='color: red;']"
    LOGIN_HEADER = "div.login-form h2"
    SIGNUP_HEADER = "div.signup-form h2"
    
    def enter_login_credentials(self, email: str, password: str):
        """Enter login credentials"""
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
        self.wait_for_navigation()
    
    def enter_signup_details(self, name: str, email: str):
        """Enter signup details"""
        self.fill(self.SIGNUP_NAME, name)
        self.fill(self.SIGNUP_EMAIL, email)
    
    def click_signup(self):
        """Click signup button"""
        self.click(self.SIGNUP_BUTTON)
        self.wait_for_navigation()
    
    def verify_login_form_visible(self) -> bool:
        """Verify login form is visible"""
        return "Login to your account" in self.get_text(self.LOGIN_HEADER)
    
    def verify_signup_form_visible(self) -> bool:
        """Verify signup form is visible"""
        return "New User Signup!" in self.get_text(self.SIGNUP_HEADER)
    
    def get_error_message(self) -> str:
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return ""  # Return empty string if error message is not found
    
    def verify_login_header(self) -> bool:
        """Verify login header is visible"""
        return "Login to your account" in self.get_text(self.LOGIN_HEADER)
    
    def verify_signup_header(self) -> bool:
        """Verify signup header is visible"""
        return "New User Signup!" in self.get_text(self.SIGNUP_HEADER) 
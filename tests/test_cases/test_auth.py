import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from config.config import Config
import random
import string

def generate_random_email():
    """Generate random email for testing"""
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}@example.com"

@pytest.fixture
def auth_pages(page):
    """Fixture for authentication related pages"""
    return {
        "home": HomePage(page),
        "login": LoginPage(page),
        "signup": SignupPage(page)
    }

@pytest.fixture(scope="session")
def registered_user_credentials():
    """Fixture to store registered user credentials"""
    return {
        "email": "",
        "password": "testpass123",
        "name": "Test User",
        "title": "Mr",
        "dob_day": "1",
        "dob_month": "1",
        "dob_year": "1990",
        "first_name": "Test",
        "last_name": "User",
        "company": "Test Company",
        "address": "123 Test St",
        "address2": "Apt 4",
        "country": "United States",
        "state": "Test State",
        "city": "Test City",
        "zipcode": "12345",
        "mobile_number": "1234567890"
    }

def test_register_user(auth_pages, registered_user_credentials):
    """Test Case 1: Register User"""
    # 1-3. Launch browser and verify home page
    auth_pages["home"].load()
    auth_pages["home"].maximize_window()
    assert auth_pages["home"].verify_page_loaded(), "Home page is not visible"
    
    # 4-5. Click signup and verify form
    auth_pages["home"].click_signup_login()
    assert auth_pages["login"].verify_signup_form_visible(), "'New User Signup!' is not visible"
    
    # 6-7. Enter signup details and click signup
    test_email = generate_random_email()
    registered_user_credentials["email"] = test_email  # Save for later use
    auth_pages["login"].enter_signup_details(registered_user_credentials["name"], test_email)
    auth_pages["login"].click_signup()
    
    # 8-9. Verify and fill account information
    assert auth_pages["signup"].verify_account_info_visible(), "'ENTER ACCOUNT INFORMATION' is not visible"
    auth_pages["signup"].fill_account_details(registered_user_credentials)
    
    # 13-14. Create account and verify
    auth_pages["signup"].click_create_account()
    assert auth_pages["signup"].verify_account_created(), "'ACCOUNT CREATED!' is not visible"
    
    # 15-16. Continue and verify logged in
    auth_pages["signup"].click_continue()
    assert auth_pages["home"].verify_logged_in_as(registered_user_credentials["name"]), "'Logged in as username' is not visible"
    
    # 17-18. Delete account and verify
    auth_pages["home"].click_delete_account()
    assert auth_pages["home"].verify_account_deleted(), "'ACCOUNT DELETED!' is not visible"
    auth_pages["home"].click_continue()

def test_login_with_correct_credentials(auth_pages, registered_user_credentials):
    """Test Case 2: Login User with correct email and password"""
    # 1-3. Launch browser and verify home page
    auth_pages["home"].load()
    assert auth_pages["home"].verify_page_loaded(), "Home page is not visible"
    
    # 4-5. Click login and verify form
    auth_pages["home"].click_signup_login()
    assert auth_pages["login"].verify_login_form_visible(), "'Login to your account' is not visible"
    
    # Register a new user first to get valid credentials
    test_email = generate_random_email()
    registered_user_credentials["email"] = test_email
    auth_pages["login"].enter_signup_details(registered_user_credentials["name"], test_email)
    auth_pages["login"].click_signup()
    auth_pages["signup"].fill_account_details(registered_user_credentials)
    auth_pages["signup"].click_create_account()
    auth_pages["signup"].click_continue()
    auth_pages["home"].click_logout()
    
    # 6-7. Enter correct credentials and login
    auth_pages["home"].click_signup_login()
    auth_pages["login"].enter_login_credentials(
        registered_user_credentials["email"],
        registered_user_credentials["password"]
    )
    auth_pages["login"].click_login()
    
    # 8. Verify logged in
    assert auth_pages["home"].verify_logged_in_as(registered_user_credentials["name"]), "'Logged in as username' is not visible"
    
    # 9-10. Delete account and verify
    auth_pages["home"].click_delete_account()
    assert auth_pages["home"].verify_account_deleted(), "'ACCOUNT DELETED!' is not visible"

def test_login_with_incorrect_credentials(auth_pages):
    """Test Case 3: Login User with incorrect email and password"""
    # 1-3. Launch browser and verify home page
    auth_pages["home"].load()
    assert auth_pages["home"].verify_page_loaded(), "Home page is not visible"
    
    # 4-5. Click login and verify form
    auth_pages["home"].click_signup_login()
    assert auth_pages["login"].verify_login_form_visible(), "'Login to your account' is not visible"
    
    # 6-7. Enter incorrect credentials and login
    auth_pages["login"].enter_login_credentials(
        "wrong@email.com",
        "wrongpassword"
    )
    auth_pages["login"].click_login()
    
    # 8. Verify error message
    assert "Your email or password is incorrect!" in auth_pages["login"].get_error_message(), "Error message is not visible"

def test_logout_user(auth_pages, registered_user_credentials):
    """Test Case 4: Logout User"""
    # 1-3. Launch browser and verify home page
    auth_pages["home"].load()
    assert auth_pages["home"].verify_page_loaded(), "Home page is not visible"
    
    # Register a new user first to get valid credentials
    test_email = generate_random_email()
    registered_user_credentials["email"] = test_email
    auth_pages["login"].enter_signup_details(registered_user_credentials["name"], test_email)
    auth_pages["login"].click_signup()
    auth_pages["signup"].fill_account_details(registered_user_credentials)
    auth_pages["signup"].click_create_account()
    auth_pages["signup"].click_continue()
    
    # 4-5. Click login and verify form
    auth_pages["home"].click_signup_login()
    assert auth_pages["login"].verify_login_form_visible(), "'Login to your account' is not visible"
    
    # 6-7. Enter correct credentials and login
    auth_pages["login"].enter_login_credentials(
        registered_user_credentials["email"],
        registered_user_credentials["password"]
    )
    auth_pages["login"].click_login()
    
    # 8. Verify logged in
    assert auth_pages["home"].verify_logged_in_as(registered_user_credentials["name"]), "'Logged in as username' is not visible"
    
    # 9-10. Logout and verify
    auth_pages["home"].click_logout()
    assert auth_pages["login"].verify_login_form_visible(), "Not navigated to login page"

def test_register_with_existing_email(auth_pages):
    """Test Case 5: Register User with existing email"""
    # 1-3. Launch browser and verify home page
    auth_pages["home"].load()
    assert auth_pages["home"].verify_page_loaded(), "Home page is not visible"
    
    # 4-5. Click signup and verify form
    auth_pages["home"].click_signup_login()
    assert auth_pages["login"].verify_signup_form_visible(), "'New User Signup!' is not visible"
    
    # 6-7. Enter existing email and signup
    auth_pages["login"].enter_signup_details(
        "Test User",
        Config.TEST_USER["email"]  # Using existing email
    )
    auth_pages["login"].click_signup()
    
    # 8. Verify error message
    assert "Email Address already exist!" in auth_pages["login"].get_error_message(), "Error message is not visible" 
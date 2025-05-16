import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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
def checkout_pages(page):
    """Fixture for checkout related pages"""
    return {
        "home": HomePage(page),
        "products": ProductsPage(page),
        "cart": CartPage(page),
        "checkout": CheckoutPage(page),
        "login": LoginPage(page),
        "signup": SignupPage(page)
    }

def add_product_to_cart(pages):
    """Helper function to add a product to cart"""
    pages["home"].click_products()
    pages["products"].add_to_cart(0)
    pages["products"].click_view_cart()

def register_new_user(pages, email=None):
    """Helper function to register a new user"""
    if not email:
        email = generate_random_email()
    
    pages["home"].click_signup_login()
    pages["login"].enter_signup_details("Test User", email)
    pages["login"].click_signup()
    
    user_data = {
        **Config.TEST_USER,
        "email": email,
        "dob_day": "1",
        "dob_month": "1",
        "dob_year": "1990"
    }
    pages["signup"].fill_account_details(user_data)
    pages["signup"].click_create_account()
    pages["signup"].click_continue()
    
    return user_data

def test_place_order_register_while_checkout(checkout_pages):
    """Test Case 14: Place Order: Register while Checkout"""
    # Load home page and add product to cart
    checkout_pages["home"].load()
    add_product_to_cart(checkout_pages)
    
    # Proceed to checkout and register
    checkout_pages["cart"].click_proceed_to_checkout()
    checkout_pages["cart"].click_register_login()
    
    # Register new user
    user_data = register_new_user(checkout_pages)
    
    # Proceed with checkout
    checkout_pages["cart"].click_proceed_to_checkout()
    assert checkout_pages["checkout"].verify_order_review()
    
    # Add comment and place order
    checkout_pages["checkout"].add_comment("Test order")
    checkout_pages["checkout"].click_place_order()
    
    # Fill payment details
    payment_info = {
        "name_on_card": "Test User",
        "card_number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025"
    }
    checkout_pages["checkout"].fill_payment_details(payment_info)
    checkout_pages["checkout"].click_pay_button()
    
    # Verify success
    assert checkout_pages["checkout"].verify_success_message()

def test_place_order_register_before_checkout(checkout_pages):
    """Test Case 15: Place Order: Register before Checkout"""
    # Load home page and register
    checkout_pages["home"].load()
    user_data = register_new_user(checkout_pages)
    
    # Add product to cart
    add_product_to_cart(checkout_pages)
    
    # Proceed with checkout
    checkout_pages["cart"].click_proceed_to_checkout()
    assert checkout_pages["checkout"].verify_order_review()
    
    # Complete order
    checkout_pages["checkout"].add_comment("Test order")
    checkout_pages["checkout"].click_place_order()
    
    payment_info = {
        "name_on_card": "Test User",
        "card_number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025"
    }
    checkout_pages["checkout"].fill_payment_details(payment_info)
    checkout_pages["checkout"].click_pay_button()
    
    assert checkout_pages["checkout"].verify_success_message()

def test_place_order_login_before_checkout(checkout_pages):
    """Test Case 16: Place Order: Login before Checkout"""
    # Load home page and login
    checkout_pages["home"].load()
    checkout_pages["home"].click_signup_login()
    checkout_pages["login"].enter_login_credentials(
        Config.TEST_USER["email"],
        Config.TEST_USER["password"]
    )
    checkout_pages["login"].click_login()
    
    # Add product and checkout
    add_product_to_cart(checkout_pages)
    checkout_pages["cart"].click_proceed_to_checkout()
    assert checkout_pages["checkout"].verify_order_review()
    
    # Complete order
    checkout_pages["checkout"].add_comment("Test order")
    checkout_pages["checkout"].click_place_order()
    
    payment_info = {
        "name_on_card": "Test User",
        "card_number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025"
    }
    checkout_pages["checkout"].fill_payment_details(payment_info)
    checkout_pages["checkout"].click_pay_button()
    
    assert checkout_pages["checkout"].verify_success_message()

def test_verify_address_details(checkout_pages):
    """Test Case 23: Verify address details in checkout page"""
    # Register new user
    checkout_pages["home"].load()
    user_data = register_new_user(checkout_pages)
    
    # Add product and proceed to checkout
    add_product_to_cart(checkout_pages)
    checkout_pages["cart"].click_proceed_to_checkout()
    
    # Verify address details
    address_details = checkout_pages["checkout"].verify_address_details()
    assert user_data["address"] in address_details["delivery"]
    assert user_data["address"] in address_details["billing"]

def test_download_invoice(checkout_pages):
    """Test Case 24: Download Invoice after purchase order"""
    # Register and place order
    checkout_pages["home"].load()
    user_data = register_new_user(checkout_pages)
    
    add_product_to_cart(checkout_pages)
    checkout_pages["cart"].click_proceed_to_checkout()
    
    checkout_pages["checkout"].add_comment("Test order")
    checkout_pages["checkout"].click_place_order()
    
    payment_info = {
        "name_on_card": "Test User",
        "card_number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025"
    }
    checkout_pages["checkout"].fill_payment_details(payment_info)
    checkout_pages["checkout"].click_pay_button()
    
    # Download and verify invoice
    download = checkout_pages["cart"].download_invoice()
    assert download is not None 
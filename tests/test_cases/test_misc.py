import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from config.config import Config

@pytest.fixture
def misc_pages(page):
    """Fixture for miscellaneous pages"""
    return {
        "home": HomePage(page),
        "cart": CartPage(page)
    }

def test_contact_us_form(misc_pages):
    """Test Case 6: Contact Us Form"""
    misc_pages["home"].load()
    assert misc_pages["home"].verify_page_loaded()
    
    misc_pages["home"].click_contact_us()
    
    # Fill contact form
    contact_info = {
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Test Subject",
        "message": "This is a test message"
    }
    misc_pages["home"].fill_contact_form(contact_info)
    
    # Upload file
    misc_pages["home"].upload_file("test.txt")
    misc_pages["home"].submit_contact_form()
    
    # Handle alert
    misc_pages["home"].page.on("dialog", lambda dialog: dialog.accept())
    
    assert misc_pages["home"].verify_contact_success()

def test_verify_test_cases(misc_pages):
    """Test Case 7: Verify Test Cases Page"""
    misc_pages["home"].load()
    assert misc_pages["home"].verify_page_loaded()
    
    misc_pages["home"].click_test_cases()
    assert "TEST CASES" in misc_pages["home"].page.title()

def test_subscription_in_home(misc_pages):
    """Test Case 10: Verify Subscription in home page"""
    misc_pages["home"].load()
    assert misc_pages["home"].verify_page_loaded()
    
    # Scroll to footer
    misc_pages["home"].page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    misc_pages["home"].subscribe_newsletter("test@example.com")
    assert misc_pages["home"].is_subscription_successful()

def test_subscription_in_cart(misc_pages):
    """Test Case 11: Verify Subscription in Cart page"""
    misc_pages["home"].load()
    misc_pages["home"].click_cart()
    
    # Scroll to footer
    misc_pages["home"].page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    misc_pages["cart"].subscribe_newsletter("test@example.com")
    assert misc_pages["cart"].verify_subscription_success()

def test_scroll_up_using_arrow(misc_pages):
    """Test Case 25: Verify Scroll Up using 'Arrow' button"""
    misc_pages["home"].load()
    assert misc_pages["home"].verify_page_loaded()
    
    # Scroll down
    misc_pages["home"].page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    assert "SUBSCRIPTION" in misc_pages["home"].get_text("div.single-widget h2")
    
    # Click scroll up arrow
    misc_pages["home"].click("i.fa-angle-up")
    
    # Verify scroll up
    assert misc_pages["home"].is_visible("div.features_items")

def test_scroll_up_without_arrow(misc_pages):
    """Test Case 26: Verify Scroll Up without 'Arrow' button"""
    misc_pages["home"].load()
    assert misc_pages["home"].verify_page_loaded()
    
    # Scroll down
    misc_pages["home"].page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    assert "SUBSCRIPTION" in misc_pages["home"].get_text("div.single-widget h2")
    
    # Scroll up
    misc_pages["home"].page.evaluate("window.scrollTo(0, 0)")
    
    # Verify scroll up
    assert misc_pages["home"].is_visible("div.features_items") 
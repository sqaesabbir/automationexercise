import pytest
from pages.home_page import HomePage
from config.config import Config

def test_home_page_loads(home_page: HomePage):
    """Test that home page loads successfully"""
    home_page.load()
    assert home_page.verify_page_loaded(), "Home page did not load properly"

def test_navigation_links(home_page: HomePage):
    """Test navigation links are working"""
    home_page.load()
    
    # Test Products link
    home_page.click_products()
    assert home_page.page.url == f"{Config.BASE_URL}/products"
    
    # Test Cart link
    home_page.click_cart()
    assert home_page.page.url == f"{Config.BASE_URL}/view_cart"
    
    # Test Login link
    home_page.click_signup_login()
    assert home_page.page.url == f"{Config.BASE_URL}/login"

def test_category_navigation(home_page: HomePage):
    """Test category navigation"""
    home_page.load()
    
    categories = ["Women", "Men", "Kids"]
    for category in categories:
        home_page.select_category(category)
        # Add assertions based on what should happen when category is selected
        # For example, verify category items are displayed

@pytest.mark.parametrize("email", [
    "test@example.com",
    "another@test.com"
])
def test_newsletter_subscription(home_page: HomePage, email: str):
    """Test newsletter subscription with different email addresses"""
    home_page.load()
    home_page.subscribe_newsletter(email)
    assert home_page.is_subscription_successful(), "Newsletter subscription failed" 
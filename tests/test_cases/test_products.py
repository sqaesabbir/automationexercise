import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from config.config import Config

@pytest.fixture
def shop_pages(page):
    """Fixture for shopping related pages"""
    return {
        "home": HomePage(page),
        "products": ProductsPage(page),
        "cart": CartPage(page)
    }

def test_verify_all_products(shop_pages):
    """Test Case 8: Verify All Products and product detail page"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    shop_pages["home"].click_products()
    assert shop_pages["products"].verify_products_page()
    assert shop_pages["products"].get_product_count() > 0
    
    shop_pages["products"].click_view_product()
    details = shop_pages["products"].get_product_details()
    assert all(key in details for key in ["name", "category", "price", "availability", "condition", "brand"])

def test_search_product(shop_pages):
    """Test Case 9: Search Product"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    shop_pages["home"].click_products()
    assert shop_pages["products"].verify_products_page()
    
    shop_pages["products"].search_product("Blue Top")
    assert shop_pages["products"].verify_search_results()
    assert shop_pages["products"].get_product_count() > 0

def test_add_products_to_cart(shop_pages):
    """Test Case 12: Add Products in Cart"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    shop_pages["home"].click_products()
    
    # Add first product
    shop_pages["products"].add_to_cart(0)
    shop_pages["products"].click_continue_shopping()
    
    # Add second product
    shop_pages["products"].add_to_cart(1)
    shop_pages["products"].click_view_cart()
    
    cart_items = shop_pages["cart"].get_cart_items()
    assert len(cart_items) == 2
    for item in cart_items:
        assert all(key in item for key in ["name", "price", "quantity", "total"])

def test_verify_product_quantity(shop_pages):
    """Test Case 13: Verify Product quantity in Cart"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    # View first product
    shop_pages["products"].click_view_product(0)
    
    # Set quantity to 4
    shop_pages["products"].set_quantity(4)
    shop_pages["products"].click("button.add-to-cart")
    shop_pages["products"].click_view_cart()
    
    cart_items = shop_pages["cart"].get_cart_items()
    assert len(cart_items) == 1
    assert cart_items[0]["quantity"] == "4"

def test_remove_products_from_cart(shop_pages):
    """Test Case 17: Remove Products From Cart"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    # Add a product to cart
    shop_pages["home"].click_products()
    shop_pages["products"].add_to_cart(0)
    shop_pages["products"].click_view_cart()
    
    # Get product name before removal
    cart_items = shop_pages["cart"].get_cart_items()
    product_name = cart_items[0]["name"]
    
    # Remove product
    shop_pages["cart"].remove_product(0)
    
    # Verify product is removed
    assert shop_pages["cart"].verify_product_removed(product_name)

def test_view_category_products(shop_pages):
    """Test Case 18: View Category Products"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    # Click on Women category
    shop_pages["home"].select_category("Women")
    
    # Verify category products are displayed
    assert shop_pages["products"].get_product_count() > 0
    
    # Click on Men category
    shop_pages["home"].select_category("Men")
    
    # Verify category products are displayed
    assert shop_pages["products"].get_product_count() > 0

def test_add_review_on_product(shop_pages):
    """Test Case 21: Add review on product"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    shop_pages["home"].click_products()
    shop_pages["products"].click_view_product(0)
    
    shop_pages["products"].write_review(
        "Test User",
        "test@example.com",
        "This is a test review"
    )
    
    assert shop_pages["products"].verify_review_success()

def test_add_to_cart_recommended_items(shop_pages):
    """Test Case 22: Add to cart from Recommended items"""
    shop_pages["home"].load()
    assert shop_pages["home"].verify_page_loaded()
    
    # Scroll to bottom to see recommended items
    shop_pages["home"].page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    # Add recommended product to cart
    shop_pages["products"].add_to_cart(-1)  # Last product in recommended items
    shop_pages["products"].click_view_cart()
    
    # Verify product is in cart
    cart_items = shop_pages["cart"].get_cart_items()
    assert len(cart_items) > 0 
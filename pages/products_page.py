from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    ALL_PRODUCTS_HEADER = "h2.title.text-center"
    SEARCH_INPUT = "input#search_product"
    SEARCH_BUTTON = "button#submit_search"
    PRODUCT_LIST = "div.features_items"
    PRODUCT_ITEMS = "div.product-image-wrapper"
    VIEW_PRODUCT_BUTTONS = "a.view-product"
    ADD_TO_CART_BUTTONS = "a.add-to-cart"
    CONTINUE_SHOPPING_BUTTON = "button.close-modal"
    VIEW_CART_BUTTON = "p.text-center a"
    PRODUCT_NAME = "div.productinfo h2"
    PRODUCT_PRICE = "div.productinfo h2"
    PRODUCT_CATEGORY = "div.product-information p"
    PRODUCT_AVAILABILITY = "div.product-information p"
    PRODUCT_CONDITION = "div.product-information p"
    PRODUCT_BRAND = "div.product-information p"
    QUANTITY_INPUT = "input#quantity"
    SEARCHED_PRODUCTS_HEADER = "h2.title.text-center"
    WRITE_REVIEW_HEADER = "a[href='#reviews']"
    REVIEW_NAME = "input#name"
    REVIEW_EMAIL = "input#email"
    REVIEW_TEXT = "textarea#review"
    SUBMIT_REVIEW_BUTTON = "button#button-review"
    REVIEW_SUCCESS_MESSAGE = "div.alert-success"
    
    def verify_products_page(self) -> bool:
        """Verify products page is loaded"""
        return "ALL PRODUCTS" in self.get_text(self.ALL_PRODUCTS_HEADER)
    
    def search_product(self, product_name: str):
        """Search for a product"""
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def verify_search_results(self) -> bool:
        """Verify search results are displayed"""
        return "SEARCHED PRODUCTS" in self.get_text(self.SEARCHED_PRODUCTS_HEADER)
    
    def get_product_count(self) -> int:
        """Get number of products displayed"""
        return self.get_element_count(self.PRODUCT_ITEMS)
    
    def click_view_product(self, index: int = 0):
        """Click view product button"""
        self.page.query_selector_all(self.VIEW_PRODUCT_BUTTONS)[index].click()
    
    def add_to_cart(self, index: int = 0):
        """Add product to cart"""
        products = self.page.query_selector_all(self.PRODUCT_ITEMS)
        if index < len(products):
            products[index].hover()
            self.page.query_selector_all(self.ADD_TO_CART_BUTTONS)[index].click()
    
    def click_continue_shopping(self):
        """Click continue shopping button"""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
    
    def click_view_cart(self):
        """Click view cart button"""
        self.click(self.VIEW_CART_BUTTON)
    
    def get_product_details(self) -> dict:
        """Get product details from product page"""
        return {
            "name": self.get_text(self.PRODUCT_NAME),
            "price": self.get_text(self.PRODUCT_PRICE),
            "category": self.get_text(self.PRODUCT_CATEGORY),
            "availability": self.get_text(self.PRODUCT_AVAILABILITY),
            "condition": self.get_text(self.PRODUCT_CONDITION),
            "brand": self.get_text(self.PRODUCT_BRAND)
        }
    
    def set_quantity(self, quantity: int):
        """Set product quantity"""
        self.fill(self.QUANTITY_INPUT, str(quantity))
    
    def write_review(self, name: str, email: str, review: str):
        """Write a product review"""
        self.fill(self.REVIEW_NAME, name)
        self.fill(self.REVIEW_EMAIL, email)
        self.fill(self.REVIEW_TEXT, review)
        self.click(self.SUBMIT_REVIEW_BUTTON)
    
    def verify_review_success(self) -> bool:
        """Verify review success message"""
        return "Thank you for your review" in self.get_text(self.REVIEW_SUCCESS_MESSAGE) 
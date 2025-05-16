from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = "tr.cart_item"
    PRODUCT_NAMES = "h4 a"
    PRODUCT_PRICES = "td.cart_price p"
    PRODUCT_QUANTITIES = "td.cart_quantity button"
    PRODUCT_TOTALS = "td.cart_total p"
    REMOVE_BUTTONS = "td.cart_delete a"
    PROCEED_CHECKOUT_BUTTON = "a.check_out"
    REGISTER_LOGIN_BUTTON = "a[href='/login']"
    CART_INFO = "div#cart_info"
    SUBSCRIPTION_EMAIL = "input#susbscribe_email"
    SUBSCRIPTION_BUTTON = "button#subscribe"
    SUBSCRIPTION_SUCCESS = "div#success-subscribe"
    DOWNLOAD_INVOICE_BUTTON = "a.download-invoice"
    
    def verify_cart_page(self) -> bool:
        """Verify cart page is loaded"""
        return self.is_visible(self.CART_INFO)
    
    def get_cart_items(self) -> list:
        """Get all cart items details"""
        items = []
        names = self.page.query_selector_all(self.PRODUCT_NAMES)
        prices = self.page.query_selector_all(self.PRODUCT_PRICES)
        quantities = self.page.query_selector_all(self.PRODUCT_QUANTITIES)
        totals = self.page.query_selector_all(self.PRODUCT_TOTALS)
        
        for i in range(len(names)):
            items.append({
                "name": names[i].text_content(),
                "price": prices[i].text_content(),
                "quantity": quantities[i].text_content(),
                "total": totals[i].text_content()
            })
        return items
    
    def remove_product(self, index: int = 0):
        """Remove product from cart"""
        self.page.query_selector_all(self.REMOVE_BUTTONS)[index].click()
    
    def click_proceed_to_checkout(self):
        """Click proceed to checkout button"""
        self.click(self.PROCEED_CHECKOUT_BUTTON)
    
    def click_register_login(self):
        """Click register/login button"""
        self.click(self.REGISTER_LOGIN_BUTTON)
    
    def subscribe_newsletter(self, email: str):
        """Subscribe to newsletter"""
        self.fill(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIPTION_BUTTON)
    
    def verify_subscription_success(self) -> bool:
        """Verify subscription success message"""
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)
    
    def download_invoice(self):
        """Click download invoice button"""
        with self.page.expect_download() as download_info:
            self.click(self.DOWNLOAD_INVOICE_BUTTON)
        download = download_info.value
        return download
    
    def verify_product_removed(self, product_name: str) -> bool:
        """Verify product is removed from cart"""
        names = self.page.query_selector_all(self.PRODUCT_NAMES)
        return not any(name.text_content() == product_name for name in names) 
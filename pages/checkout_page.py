from .base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    DELIVERY_ADDRESS = "ul#address_delivery"
    BILLING_ADDRESS = "ul#address_billing"
    ORDER_REVIEW = "div.order-review"
    COMMENT_TEXTAREA = "textarea.form-control"
    PLACE_ORDER_BUTTON = "a.check_out"
    PAYMENT_FORM = "form.payment-form"
    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"
    PAY_BUTTON = "button[data-qa='pay-button']"
    SUCCESS_MESSAGE = "div.alert-success"
    
    def verify_address_details(self) -> dict:
        """Get and verify address details"""
        delivery = self.get_text(self.DELIVERY_ADDRESS)
        billing = self.get_text(self.BILLING_ADDRESS)
        return {
            "delivery": delivery,
            "billing": billing
        }
    
    def verify_order_review(self) -> bool:
        """Verify order review section is visible"""
        return self.is_visible(self.ORDER_REVIEW)
    
    def add_comment(self, comment: str):
        """Add comment to order"""
        self.fill(self.COMMENT_TEXTAREA, comment)
    
    def click_place_order(self):
        """Click place order button"""
        self.click(self.PLACE_ORDER_BUTTON)
    
    def fill_payment_details(self, payment_info: dict):
        """Fill payment form details"""
        self.fill(self.NAME_ON_CARD, payment_info['name_on_card'])
        self.fill(self.CARD_NUMBER, payment_info['card_number'])
        self.fill(self.CVC, payment_info['cvc'])
        self.fill(self.EXPIRY_MONTH, payment_info['expiry_month'])
        self.fill(self.EXPIRY_YEAR, payment_info['expiry_year'])
    
    def click_pay_button(self):
        """Click pay and confirm order button"""
        self.click(self.PAY_BUTTON)
    
    def verify_success_message(self) -> bool:
        """Verify order success message"""
        return "Your order has been placed successfully" in self.get_text(self.SUCCESS_MESSAGE)
    
    def verify_payment_form(self) -> bool:
        """Verify payment form is visible"""
        return self.is_visible(self.PAYMENT_FORM) 
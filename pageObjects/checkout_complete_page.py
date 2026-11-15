from playwright.sync_api import expect
class CheckoutCompletePage:

    def __init__(self,page):
        self.page=page

    def verify_order_confirmation(self):
        expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")
from playwright.sync_api import expect
class CheckoutCompletePage:

    def __init__(self,checkout_overview_page):
        self.checkout_overview_page=checkout_overview_page
        self.page=checkout_overview_page.page

    def verify_order_confirmation(self):
        expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")

    def verify_confirmation_page_heading(self):
        expect(self.page.locator('.title')).to_have_text('Checkout: Complete!')

    def verify_order_dispatch_message(self):
        expect(self.page.locator('.complete-text')).to_have_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!')

    def verify_confirmation_image(self):
        expect(self.page.locator('.pony_express')).to_be_visible()

    def click_back_home(self):
        self.page.get_by_role("button",name="Back Home").click()
        expect(self.page).to_have_url('https://www.saucedemo.com/inventory.html')

    def verify_cart_after_order_completion(self):
        expect(self.page.locator('.shopping_cart_badge')).not_to_be_visible()
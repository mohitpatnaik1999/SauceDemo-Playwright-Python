from playwright.sync_api import expect
from pageObjects.checkout_page import CheckOutPage

class CartPage:

    def __init__(self,page):
        self.page=page

    def proceed_to_checkout(self):
        expect(self.page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack")).to_have_text("Sauce Labs Backpack")
        expect(self.page.locator(".inventory_item_name").filter(has_text="Sauce Labs Bike Light")).to_have_text("Sauce Labs Bike Light")
        self.page.get_by_role("button",name="Checkout").click()
        checkout_page=CheckOutPage(self.page)
        return checkout_page
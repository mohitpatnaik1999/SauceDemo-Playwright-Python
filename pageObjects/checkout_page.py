from pageObjects.checkout_overview_page import CheckoutOverviewPage
from playwright.sync_api import expect
class CheckOutPage:

    def __init__(self,cart_page):
        self.cart_page=cart_page
        self.page=cart_page.page

    def complete_checkout_information(self):
        self.page.get_by_placeholder("First Name").fill("Mohit")
        self.page.get_by_placeholder("Last Name").fill("Patnaik")
        self.page.get_by_placeholder("Zip/Postal Code").fill("760010")
        self.page.locator("#continue").click()
        checkout_overview_page=CheckoutOverviewPage(self.page)
        return checkout_overview_page

    def verify_validation_when_mandatory_fields_are_blank(self):
        self.page.locator('#continue').click()
        expect(self.page.locator('h3')).to_have_text('Error: First Name is required')

    def complete_checkout_info(self,first_name,last_name,postal_code):
        self.page.get_by_placeholder('First Name').fill(first_name)
        self.page.get_by_placeholder('Last Name').fill(last_name)
        self.page.get_by_placeholder('Zip/Postal Code').fill(postal_code)
        self.page.locator("#continue").click()
from pageObjects.checkout_overview_page import CheckoutOverviewPage
class CheckOutPage:

    def __init__(self,page):
        self.page=page

    def complete_checkout_information(self):
        self.page.get_by_placeholder("First Name").fill("Mohit")
        self.page.get_by_placeholder("Last Name").fill("Patnaik")
        self.page.get_by_placeholder("Zip/Postal Code").fill("760010")
        self.page.locator("#continue").click()
        checkout_overview_page=CheckoutOverviewPage(self.page)
        return checkout_overview_page
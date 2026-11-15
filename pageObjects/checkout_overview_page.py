from pageObjects.checkout_complete_page import CheckoutCompletePage
class CheckoutOverviewPage:

    def __init__(self,page):
        self.page=page

    def finish_checkout(self):
        self.page.get_by_role("button",name="Finish").click()
        order_confirmation_page=CheckoutCompletePage(self.page)
        return order_confirmation_page
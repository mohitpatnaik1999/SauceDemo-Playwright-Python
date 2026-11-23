from pageObjects.checkout_complete_page import CheckoutCompletePage
from playwright.sync_api import expect
class CheckoutOverviewPage:

    def __init__(self,checkout_page):
        self.checkout_page=checkout_page
        self.page=checkout_page.page

    def verify_selected_products_appear_in_the_order(self,expected_products):
        actual_products = self.page.locator('.inventory_item_name').all_text_contents()
        assert sorted(actual_products) == sorted(expected_products)

    def verify_product_prices(self,expected_prices):
        prices=self.page.locator('.inventory_item_price').all_text_contents()
        actual_price=[float(price.replace('$',"")) for price in prices]
        assert sorted(actual_price) == sorted(expected_prices)

    def verify_item_total(self):
        actual_total=0
        prices=self.page.locator('.inventory_item_price').all_text_contents()
        actual_prices=[float(price.replace('$',"")) for price in prices]
        actual_total=sum(actual_prices)
        expected_total = float(self.page.locator('.summary_subtotal_label').text_content().strip().replace('Item total: $',""))
        assert actual_total == expected_total

    def verify_tax_calculation(self):
        item_total=self.page.locator('.summary_subtotal_label').text_content().strip()
        actual_total=float(item_total.replace('Item total: $',""))
        actual_tax=round(actual_total*0.08,2)
        expected_tax=float(self.page.locator('.summary_tax_label').text_content().strip().replace('Tax: $',""))
        assert actual_tax == expected_tax

    def verify_final_total(self):
        total=self.page.locator('.summary_subtotal_label').text_content().strip()
        item_total=float(total.replace('Item total: $',""))
        tax=self.page.locator('.summary_tax_label').text_content().strip()
        total_tax=float(tax.replace('Tax: $',""))
        final_price=float(item_total+total_tax)
        expected_final_price=float(self.page.locator('.summary_total_label').text_content().strip().replace('Total: $',""))
        assert final_price == expected_final_price

    def click_finish_and_navigate_to_order_confirmation(self):
        self.page.get_by_role("button",name="Finish").click()
        expect(self.page.locator('h2')).to_have_text('Thank you for your order!')

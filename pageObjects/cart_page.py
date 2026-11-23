from playwright.sync_api import expect
from pageObjects.checkout_page import CheckOutPage

class CartPage:

    def __init__(self,inventory_page):
        self.inventory_page=inventory_page
        self.page=inventory_page.page
        self.cart_item=self.page.locator('.cart_item')

    def navigate_to_cart(self):
        self.page.locator('.shopping_cart_link').click()

    def verify_added_products(self,expected_products):
        actual_product=self.page.locator('.inventory_item_name').all_text_contents()
        assert actual_product == expected_products

    def verify_product_details(self):
        cart_item=self.page.locator('.cart_item')
        text=cart_item.filter(has_text='Sauce Labs Backpack').locator('.inventory_item_name').text_content()
        item_price=cart_item.filter(has_text='$29.99').locator('.inventory_item_price').text_content()
        cart_item.filter(has_text='Sauce Labs Backpack').locator('.inventory_item_name').click()
        expect(self.page.locator('.inventory_details_img')).to_be_visible()
        expect(self.page.locator('.inventory_details_name')).to_have_text(text)
        expect(self.page.locator('.inventory_details_desc')).not_to_be_empty()
        expect(self.page.locator('.inventory_details_price')).to_have_text(item_price)

    def remove_a_product_from_cart(self):
        count=0
        for item in self.cart_item.all():
            if item.get_by_role("button",name="Remove").count() > 0:
                item.get_by_role("button",name="Remove").click()
                count=count+1
        expect(self.page.locator('.shopping_cart_badge')).to_have_text(str(count))

    def navigate_back_to_inventory_page(self):
        self.page.get_by_role("button",name="Continue Shopping").click()
        expect(self.page.locator(".inventory_container")).to_be_visible()

    def navigate_to_checkout_page(self):
        self.page.get_by_role("button",name="Checkout").click()
        expect(self.page.locator('.checkout_info_wrapper')).to_be_visible()
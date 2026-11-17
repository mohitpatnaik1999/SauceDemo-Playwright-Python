from pageObjects.cart_page import CartPage

from playwright.sync_api import expect
class InventoryPage:

    def __init__(self,page):
        self.page=page
        self.inventory_page=page.locator('.inventory_item')

    def add_products_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()
        self.page.locator(".shopping_cart_link").click()
        cart_page=CartPage(self.page)
        return cart_page

    def verify_product_details(self):
        for item in self.inventory_page.all():
            expect(item.locator('.inventory_item_img img')).to_be_visible()
            expect(item.locator(".inventory_item_description")).not_to_be_empty()
            expect(item.locator(".inventory_item_name")).to_be_visible()
            expect(item.locator(".inventory_item_price")).not_to_be_empty()
            expect(item.locator(".btn_inventory")).to_be_visible()
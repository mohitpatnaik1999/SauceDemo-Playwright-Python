from pageObjects.cart_page import CartPage
class InventoryPage:

    def __init__(self,page):
        self.page=page

    def add_products_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()
        self.page.locator(".shopping_cart_link").click()
        cart_page=CartPage(self.page)
        return cart_page
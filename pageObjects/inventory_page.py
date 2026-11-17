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

    def sort_products_name_in_ascending_order(self):
        self.page.locator('.product_sort_container').select_option('az')
        products_name=self.page.locator('.inventory_item_name').all_text_contents()
        expected_names=sorted(products_name)
        assert expected_names == products_name

    def sort_product_names_in_descending_order(self):
        self.page.locator('.product_sort_container').select_option('za')
        product_names=self.page.locator('.inventory_item_name').all_text_contents()
        expected_name=sorted(product_names, reverse=True)
        assert product_names == expected_name

    def sort_product_by_price_in_ascending(self):
        self.page.locator('.product_sort_container').select_option('lohi')
        prices=self.page.locator('.inventory_item_price').all_text_contents()
        actual_price=[float(price.replace("$","")) for price in prices]
        expected_price=sorted(actual_price)
        assert expected_price == actual_price

    def sort_product_by_price_in_descending(self):
        self.page.locator('.product_sort_container').select_option('hilo')
        prices=self.page.locator('.inventory_item_price').all_text_contents()
        actual_price=[float(price.replace("$","")) for price in prices]
        expected_price=sorted(actual_price, reverse=True)
        assert expected_price == actual_price

    def verify_product_details_navigation(self):

        #Navigation check by clicking on product name
        self.page.locator("a[id='item_4_title_link']").click()
        expect(self.page.locator('.inventory_details_name')).to_be_visible()
        expect(self.page.locator('.inventory_details_desc')).not_to_be_empty()
        expect(self.page.locator('.inventory_details_price')).to_be_visible()
        expect(self.page.locator('.btn_inventory')).to_be_visible()
        expect(self.page.locator('.inventory_details_img_container img')).to_be_visible()

        self.page.get_by_role("button",name="Back to products").click()

        #Navigation check by clicking on product name
        self.page.locator("img[alt='Sauce Labs Backpack']").click()
        expect(self.page.locator('.inventory_details_name')).to_be_visible()
        expect(self.page.locator('.inventory_details_desc')).not_to_be_empty()
        expect(self.page.locator('.inventory_details_price')).to_be_visible()
        expect(self.page.locator('.btn_inventory')).to_be_visible()
        expect(self.page.locator('.inventory_details_img_container img')).to_be_visible()
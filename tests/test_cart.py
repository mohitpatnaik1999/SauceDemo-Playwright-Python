from pageObjects.cart_page import CartPage

def test_verify_navigate_to_cart_and_verify_url(cart_page_fixture):
    assert cart_page_fixture.page.url == 'https://www.saucedemo.com/cart.html'

def test_verify_added_products(cart_page_fixture):
    expected_products=['Sauce Labs Backpack','Sauce Labs Bike Light']
    cart_page_fixture.verify_added_products(expected_products)

def test_verify_product_details(cart_page_fixture):
    cart_page_fixture.verify_product_details()

def test_verify_remove_a_product_from_cart(cart_page_fixture):
    cart_page_fixture.remove_a_product_from_cart()

def test_verify_navigate_back_to_inventory_page(cart_page_fixture):
    cart_page_fixture.navigate_back_to_inventory_page()

def test_verify_navigate_to_checkout_page(cart_page_fixture):
    cart_page_fixture.navigate_to_checkout_page()
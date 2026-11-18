from playwright.sync_api import expect

from pageObjects.inventory_page import InventoryPage
def test_verify_inventory_page(login_fixture):
    page=login_fixture
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    # assert page.url == 'https://www.saucedemo.com/inventory.html'
    expect(page.locator('.app_logo')).to_have_text('Swag Labs')
    expect(page.locator('.inventory_list')).to_be_visible()

def test_verify_product_count(login_fixture):
    page=login_fixture
    expect(page.locator('.inventory_item')).to_have_count(6)

def test_verify_product_details(inventory_page_fixture):
    inventory_page_fixture.verify_product_details()

def test_verify_product_sort_by_name_ascending(inventory_page_fixture):
    inventory_page_fixture.sort_products_name_in_ascending_order()

def test_verify_product_sort_by_name_descending(inventory_page_fixture):
    inventory_page_fixture.sort_product_names_in_descending_order()

def test_verify_product_sort_by_price_ascending(inventory_page_fixture):
    inventory_page_fixture.sort_product_by_price_in_ascending()

def test_verify_product_sort_by_price_descending(inventory_page_fixture):
    inventory_page_fixture.sort_product_by_price_in_descending()

def test_verify_product_detail_navigation(inventory_page_fixture):
    inventory_page_fixture.verify_product_details_navigation()

def test_verify_add_multiple_products_to_cart(inventory_page_fixture):
    inventory_page_fixture.add_multiple_products_to_cart()

def test_verify_remove_product_from_inventory(inventory_page_fixture):
    inventory_page_fixture.remove_product_from_inventory()

def test_verify_verify_cart_badge_after_removal(inventory_page_fixture):
    inventory_page_fixture.remove_product_from_inventory()
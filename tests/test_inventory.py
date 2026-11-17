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

def test_verify_product_details(login_fixture):
    page=login_fixture
    inventory_page=InventoryPage(page)
    inventory_page.verify_product_details()

def test_verify_product_name_sorting_in_ascending(login_fixture):
    page=login_fixture
    inventory_page = InventoryPage(page)
    inventory_page.sort_products_name_in_ascending_order()

def test_verify_product_name_sorting_in_descending(login_fixture):
    page=login_fixture
    inventory_page=InventoryPage(page)
    inventory_page.sort_product_names_in_descending_order()
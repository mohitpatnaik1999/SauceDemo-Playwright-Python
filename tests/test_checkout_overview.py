from playwright.sync_api import expect

def test_verify_checkout_overview_page_url(checkout_overview_page_fixture):
    # assert checkout_overview_page_fixture.page.url == 'https://www.saucedemo.com/checkout-step-two.html'
    expect(checkout_overview_page_fixture.page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')

def test_verify_selected_products_appear_in_the_order(checkout_overview_page_fixture):
    expected_products=['Sauce Labs Bike Light','Sauce Labs Backpack']
    checkout_overview_page_fixture.verify_selected_products_appear_in_the_order(expected_products)

def test_verify_product_prices(checkout_overview_page_fixture):
    expected_prices=[9.99,29.99]
    checkout_overview_page_fixture.verify_product_prices(expected_prices)

def test_verify_item_total(checkout_overview_page_fixture):
    checkout_overview_page_fixture.verify_item_total()

def test_verify_tax_calculation(checkout_overview_page_fixture):
    checkout_overview_page_fixture.verify_tax_calculation()

def test_verify_final_total(checkout_overview_page_fixture):
    checkout_overview_page_fixture.verify_final_total()

def test_verify_click_finish_and_navigate_to_order_confirmation(checkout_overview_page_fixture):
    checkout_overview_page_fixture.click_finish_and_navigate_to_order_confirmation()
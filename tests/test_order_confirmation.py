from playwright.sync_api import expect
def test_verify_order_confirmation_page_url(checkout_confirmation_page_fixture):
    # assert checkout_confirmation_page_fixture.page.url == "https://www.saucedemo.com/checkout-complete.html"
    expect(checkout_confirmation_page_fixture.page).to_have_url('https://www.saucedemo.com/checkout-complete.html')

def test_verify_confirmation_page_heading(checkout_confirmation_page_fixture):
    checkout_confirmation_page_fixture.verify_confirmation_page_heading()

def test_verify_order_dispatch_message(checkout_confirmation_page_fixture):
    checkout_confirmation_page_fixture.verify_order_dispatch_message()

def test_verify_confirmation_image(checkout_confirmation_page_fixture):
    checkout_confirmation_page_fixture.verify_confirmation_image()

def test_verify_click_back_home(checkout_confirmation_page_fixture):
    checkout_confirmation_page_fixture.click_back_home()

def test_verify_cart_after_order_completion(checkout_confirmation_page_fixture):
    checkout_confirmation_page_fixture.verify_cart_after_order_completion()
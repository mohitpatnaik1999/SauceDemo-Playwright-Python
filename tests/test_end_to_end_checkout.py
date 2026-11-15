from playwright.sync_api import Playwright, expect
from pageObjects.login_page import LoginPage

def test_login(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #login screen
    login_page=LoginPage(page)
    inventory_page=login_page.login_with_credentials("standard_user","secret_sauce")

    #dashboard page
    cart_page=inventory_page.add_products_to_cart()

    #Add to Cart page
    checkout_page=cart_page.proceed_to_checkout()

    #checkout page
    checkout_overview_page=checkout_page.complete_checkout_information()

    #Pre Order Confirmation Page 
    checkout_complete_page=checkout_overview_page.finish_checkout()

    #Order confirmation Page
    checkout_complete_page.verify_order_confirmation()

    #page.get_by_role("button",name="Back Home").click()

import pytest, json
from pageObjects.checkout_complete_page import CheckoutCompletePage
from pageObjects.checkout_overview_page import CheckoutOverviewPage
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage
from pageObjects.checkout_page import CheckOutPage

with open('test_data/credentials.json') as f:
    test_data=json.load(f)

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection for cross browser testing"
    )

@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == 'chrome':
        browser=playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
    browser.close()

def user_credentials(request):
    return request.param

@pytest.fixture(params=test_data["user_credentials"])
def login_fixture(request, browser_instance):
    credentials = user_credentials(request)
    username=credentials['username']
    password=credentials['password']
    login_page=LoginPage(browser_instance)
    login_page.login_with_credentials(username,password)
    return browser_instance

@pytest.fixture
def inventory_page_fixture(login_fixture):
    inventory_page=InventoryPage(login_fixture)
    return inventory_page

@pytest.fixture
def cart_page_fixture(inventory_page_fixture):
    cart_page=CartPage(inventory_page_fixture)
    cart_page.inventory_page.add_multiple_products_to_cart()
    cart_page.navigate_to_cart()
    return cart_page

@pytest.fixture
def checkout_page_fixture(cart_page_fixture):
    checkout_page=CheckOutPage(cart_page_fixture)
    checkout_page.cart_page.navigate_to_checkout_page()
    return checkout_page

def checkout_credentials(request):
    return request.param

@pytest.fixture(params=test_data["checkout_creds"])
def checkout_overview_page_fixture(checkout_page_fixture,request):
    credentials=checkout_credentials(request)
    first_name=credentials['first_name']
    last_name=credentials['last_name']
    postal_code=credentials['postal_code']
    checkout_overview=CheckoutOverviewPage(checkout_page_fixture)
    checkout_overview.checkout_page.complete_checkout_info(first_name,last_name,postal_code)
    return checkout_overview

@pytest.fixture
def checkout_confirmation_page_fixture(checkout_overview_page_fixture):
    checkout_complete=CheckoutCompletePage(checkout_overview_page_fixture)
    checkout_complete.checkout_overview_page.click_finish_and_navigate_to_order_confirmation()
    return checkout_complete
import pytest, json
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage

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
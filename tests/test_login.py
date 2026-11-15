from playwright.sync_api import expect
from pageObjects.login_page import LoginPage
import pytest, json

with open('test_data/credentials.json') as f:
    test_data=json.load(f)
    user_credentials_list=test_data['user_credentials']


@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_login_with_valid_credentials(browser_instance, user_credentials):

    username = user_credentials['username']
    password = user_credentials['password']

    page=browser_instance
    login_page=LoginPage(page)
    login_page.login_with_credentials(username,password)

# def test_login_with_invalid_credentials(browser_instance):
#     login_page=LoginPage(browser_instance)
#     login_page.login_with_credentials("mohit","patnaik")
#     expect(browser_instance.get_by_role("alert")).to_have_text("Epic sadface: Username and password do not match any user in this service")
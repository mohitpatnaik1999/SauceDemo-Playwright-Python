from playwright.sync_api import expect
from pageObjects.login_page import LoginPage
import pytest, json

with open('test_data/credentials.json') as f:
    test_data=json.load(f)
    user_credentials_list=test_data['user_credentials']
    invalid_user_credentials_list=test_data['invalid_user_credentials']
    blank_credentials_list=test_data['blank_credentials']


@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_login_with_valid_credentials(browser_instance, user_credentials):

    username = user_credentials['username']
    password = user_credentials['password']

    page=browser_instance
    login_page=LoginPage(page)
    login_page.login_with_credentials(username,password)


@pytest.mark.parametrize('invalid_user_credentials',invalid_user_credentials_list)
def test_login_with_invalid_credentials(browser_instance, invalid_user_credentials):
    username=invalid_user_credentials['username']
    password=invalid_user_credentials['password']
    login_page=LoginPage(browser_instance)
    login_page.login_with_credentials(username,password)
    expect(browser_instance.get_by_role("alert")).to_have_text("Epic sadface: Username and password do not match any user in this service")

@pytest.mark.parametrize('blank_credentials',blank_credentials_list)
def test_login_with_blank_credentials(browser_instance,blank_credentials):
    username=blank_credentials['username']
    password=blank_credentials['password']
    login_page=LoginPage(browser_instance)
    login_page.login_with_credentials(username,password)
    expect(browser_instance.get_by_role("alert")).to_have_text("Epic sadface: Username and password do not match any user in this service")
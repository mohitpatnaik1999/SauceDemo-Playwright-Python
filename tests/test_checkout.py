from playwright.sync_api import expect
import pytest, json

with open('test_data/credentials.json') as f:
    test_data=json.load(f)
    checkout_credentials=test_data['checkout_creds']

def test_verify_checkout_page_url(checkout_page_fixture):
    # assert checkout_page_fixture.page.url == 'https://www.saucedemo.com/checkout-step-one.html'
    expect(checkout_page_fixture.page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')

def test_verify_validation_when_mandatory_fields_are_blank(checkout_page_fixture):
    checkout_page_fixture.verify_validation_when_mandatory_fields_are_blank()

@pytest.mark.parametrize('checkout_credentials',checkout_credentials)
def test_verify_complete_checkout_info(checkout_page_fixture, checkout_credentials):
    checkout_page_fixture.complete_checkout_info(checkout_credentials)
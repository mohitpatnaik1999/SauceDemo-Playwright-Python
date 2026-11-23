from pageObjects.inventory_page import InventoryPage
class LoginPage:

    def __init__(self,page):
        self.page=page

    def login_with_credentials(self, username, password):
        self.page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator("#login-button").click()
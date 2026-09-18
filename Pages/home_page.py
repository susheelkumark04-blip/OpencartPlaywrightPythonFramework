from logging import exception

from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.get_my_account = page.locator("//span[@class='caret']")
        self.lnk_register =page.locator("//a[normalize-space()='Register']")
        self.lnk_login = page.locator("//a[normalize-space()='Login']")
        self.txt_search_box = page.locator("//input[@class='form-control input-lg']")
        self.btn_search = page.locator("//button[@class='btn btn-default btn-lg']")

    def get_home_page_title(self):
        title = self.page.title()
        return title

    def click_my_account(self):
        try:
            self.get_my_account.click()
        except exception as e:
            print(f"Error: {e}")
            raise

    def click_register(self):
        try:
            self.lnk_register.click()
        except exception as e:
            print(f"Error: {e}")
            raise

    def click_login(self):
        try:
            self.lnk_login.click()
        except exception as e:
            print(f"Error: {e}")
            raise

    def enter_product_name(self, product_name):
        try:
            self.txt_search_box.fill(product_name)
        except exception as e:
            print(f"Error: {e}")
            raise

    def click_search(self):
        try:
            self.btn_search.click()
        except exception as e:
            print(f"Error: {e}")
            raise


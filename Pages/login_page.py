from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.txt_email_id = page.locator("//input[@id='input-email']")
        self.txt_password = page.locator("//input[@id='input-password']")
        self.login_button = page.locator("//input[@class='btn btn-primary']")
        self.txt_error_msg = page.locator("//div[@class='alert alert-danger alert-dismissible']")

    def enter_email_id(self, email):
        try:
             self.txt_email_id.fill(email)
        except Exception as e:
            print(f" Exception while entering email: {e}")
            raise

    def enter_password(self, password):
        try:
            self.txt_password.fill(password)
        except Exception as e:
            print(f" Exception while entering password: {e}")
            raise

    def click_login_button(self):
        try:
            self.login_button.click()
        except Exception as e:
            print(f" Exception while clicking login button: {e}")
            raise

    def login(self, email, password):
        self.enter_email_id(email)
        self.enter_password(password)
        self.click_login_button()

    def login_error_msg(self):
        try:
            return self.txt_error_msg
        except Exception as e:
            print(f" Exception while fetching login error message: {e}")
            return None
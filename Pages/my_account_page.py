from playwright.sync_api import Page

class MyAccountPage:

    def __init__(self , page):
        self.page = page

        self.msg_header = page.locator("//h2[normalize-space()='My Account']")
        self.lnk_logout = page.locator("//a[normalize-space()='Logout']")

    def get_msg_header(self):
        try:
            return self.msg_header
        except Exception as e:
            print(f"Error: {e}")
            return None

    def click_logout(self):
        try:
            self.lnk_logout.click()
            return self.lnk_logout
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def get_page_title(self):
        try:
            return self.page.title
        except Exception as e:
            print(f"Error: {e}")
            return None



import pytest

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.my_account_page import MyAccountPage
from Pages.logout_page import LogoutPage
from playwright.sync_api import expect
from config import Config

def test_user_logout(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email_id(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_login_button()

    expect(my_account_page.get_msg_header()).to_be_visible(timeout=3000)

    logout_page = my_account_page.click_logout()

    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)

    logout_page.click_continue()
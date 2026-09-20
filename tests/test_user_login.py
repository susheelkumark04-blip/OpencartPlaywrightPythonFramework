import pytest

import Pages
import config
from Pages import my_account_page
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from config import Config

@pytest.mark.regression
def test_invalid_user_login(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email_id(Config.invalid_email)
    login_page.enter_password(Config.invalid_password)
    login_page.click_login_button()

    expect(login_page.login_error_msg()).to_be_visible(timeout=3000)

def test_valid_user_login(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.enter_email_id(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_login_button()

    expect(my_account_page.get_msg_header()).to_be_visible(timeout=3000)

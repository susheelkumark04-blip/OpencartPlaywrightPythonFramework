import pytest
from Pages.home_page import HomePage
from Pages.registration_page import RegistrationPage
from playwright.sync_api import expect

from Utils.random_data_util import RandomDataUtil


def test_user_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()

    first_name= random_data.get_first_name()
    last_name= random_data.get_last_name()
    email= random_data.get_email()
    phone_number= random_data.get_phone_number()
    password= random_data.get_password()

    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_phone(phone_number)
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)

    registration_page.check_policy()
    registration_page.continue_button.click()

    conformation_msg= registration_page.get_msg_confirmation()
    expect(conformation_msg).to_have_text("Your Account Has Been Created!")





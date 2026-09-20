import pytest
from playwright.sync_api import expect

import config
from Pages.home_page import HomePage
from Pages.search_result_page import SearchResultPage
from config import Config

@pytest.mark.sanity
def test_search_result_page(page):
    product_name = Config.product_name
    home_page = HomePage(page)
    search_result_page = SearchResultPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()

    expect(search_result_page.get_search_result_page_header()).to_be_visible(timeout=5000)
    expect(search_result_page.get_product_result(product_name)).to_be_visible()



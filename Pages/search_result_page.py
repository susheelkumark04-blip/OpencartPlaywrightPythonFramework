from playwright.sync_api import Page

from Pages.product_page import ProductPage


class SearchResultPage:

    def __init__(self , page : Page):
        self.page = page

        self.search_page_header = page.locator("//*[@id='content']/h1", has_text='Search -')
        self.product_list = page.locator("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)")

    def get_search_result_page_header(self):
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_product_result(self, product_name):
        try:
            count= self.product_list.count()
            for i in range(count):
                product = self.product_list.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page)
            print(f"Product not found: {product_name}")
        except Exception as e:
            print(f"Error: {e}")
            return None








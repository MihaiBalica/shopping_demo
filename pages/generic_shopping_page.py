"""
Generic shopping Page that applies to both women and men and other forms of life
"""
from symtable import Class
from time import sleep
from urllib.response import addbase

from pages.base_page import BasePage
from utils.locators import BasePageLocators, WhatsNewLocators, ShopLocators
from playwright.sync_api import TimeoutError

class GenericShopPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # self.product_name = page.locator(ShopLocators.PRODUCT_NAME)
        self.add_to_cart_button_locator = page.locator(ShopLocators.ADD_TO_CART)
        self.sort_by_locator = page.locator(ShopLocators.PAGE_TITLE)

    def wait_for_page_to_load(self):
        self.wait_for_element(self.sort_by_locator)
        # this is only for the audience, to see that it is actually happening
        sleep(2)

    def add_items_to_cart(self, product_name: str):
        product_locator = self.page.locator(str(ShopLocators.PRODUCT_NAME).format(product_name))

        product_locator.click()
        sleep(2)
        # workaround
        add_to_cart_button = self.page.locator(str(ShopLocators.ADD_TO_CART).format(product_name))
        add_to_cart_button.click()

        # and now the Shopping cart page should open. To be continued
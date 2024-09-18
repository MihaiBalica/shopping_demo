"""
Luma Home Page
"""
from symtable import Class

from pages.base_page import BasePage
from utils.locators import HomePageLocators
from playwright.sync_api import TimeoutError

class LumaHomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.search_store_locator = page.locator(HomePageLocators.SEARCH_ENTIRE_STORE)
        self.whatsnew_locator = page.locator(HomePageLocators.WHATS_NEW)
        self.sale_locator = page.locator(HomePageLocators.SALE)
        self.training_locator = page.locator(HomePageLocators.TRAINING)


    def go_to_site(self) -> None:
        """
        this will navigate to the site
        :return:
        """
        self.logger.info("Navigating to url: {}".format(self.url))
        super().go_to_site()


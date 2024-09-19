"""
Luma Home Page
"""
from symtable import Class

from pages.base_page import BasePage
from utils.locators import BasePageLocators
from playwright.sync_api import TimeoutError

class LumaHomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    def go_to_site(self) -> None:
        """
        this will navigate to the site
        :return:
        """
        self.logger.info("Navigating to url: {}".format(self.url))
        super().go_to_site()


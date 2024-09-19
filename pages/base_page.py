"""
This module provides the base class for all pages.
"""
from utils.config import Config
from utils.logger import setup_logger
from utils.locators import BasePageLocators


class BasePage:
    """
    this is the base class for all pages.
    """

    def __init__(self, page):
        self.page = page
        self.url = Config.URL
        self.logger = setup_logger(self.__class__.__name__, 'shopping_page.log')

        self.search_store_locator = page.locator(BasePageLocators.SEARCH_ENTIRE_STORE)
        self.whatsnew_locator = page.locator(BasePageLocators.WHATS_NEW)
        self.sale_locator = page.locator(BasePageLocators.SALE)
        self.training_locator = page.locator(BasePageLocators.TRAINING)

    def wait_for_element(self, locator, state="visible", timeout=10000):
        """
        Wait for a specific locator to be in a given state
        """
        locator.wait_for(state=state, timeout=timeout)


    def go_to_site(self) -> None:
        """
        navigate to the site
        """
        self.logger.info(f"Navigating to {self.url}")
        self.page.goto(self.url)

    def go_to_whatsnew(self):
        """
        navigate to the whatsnew page
        :return:
        """
        self.logger.info(f"Navigating to {self.whatsnew_locator}")
        self.whatsnew_locator.click()

    def select_left_side_menu(self, genre: str, category: str):
        menu_locator = self.page.locator(str(BasePageLocators.LEFT_SIDE_MENU_ENTRY).format(genre.lower(), category))
        menu_locator.click()

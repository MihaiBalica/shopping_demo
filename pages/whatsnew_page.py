"""
Whats's New Page
"""
from symtable import Class

from pages.base_page import BasePage
from utils.locators import BasePageLocators, WhatsNewLocators
from playwright.sync_api import TimeoutError

class WhatsNewPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.my_wish_list = page.locator(WhatsNewLocators.MY_WISH_LIST)
        self.new_luma_yoga = page.locator(WhatsNewLocators.NEW_LUMA_YOGA)
        self.whatever_day_brings = page.locator(WhatsNewLocators.WHATEVER_DAY_BRINGS)
        self.sense_of_renewal = page.locator(WhatsNewLocators.SENSE_OF_RENEWAL)



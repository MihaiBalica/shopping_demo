"""
A walkthrough test, to check pages are loading
"""
from time import sleep

import pytest

from pages.generic_shopping_page import GenericShopPage
from pages.whatsnew_page import WhatsNewPage
from pages.luma_home_page import LumaHomePage
from utils.logger import setup_logger

logger = setup_logger(__name__, 'smoke_test.log')


class TestWalkThrough:
    """
    Test Case for a walkthrough test
    """

    @pytest.mark.smoke
    def test_walk_through(self, page):
        logger.info('Starting test: test_walk_through')

        home_page = LumaHomePage(page)
        luna_home_page = LumaHomePage(page)
        whatsnew_page = WhatsNewPage(page)
        generic_shopping_page = GenericShopPage(page)

        home_page.go_to_site()
        home_page.go_to_whatsnew()

        whatsnew_page.wait_for_page_to_load()
        whatsnew_page.select_left_side_menu("Men","Pants")

        generic_shopping_page.wait_for_page_to_load()
        generic_shopping_page.add_items_to_cart("Cronus Yoga Pant")

        # this sleep is here till a page object for the cart is implemented so to be able to wait for it to load
        sleep(10)
        logger.info('Test completed')
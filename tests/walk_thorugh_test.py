"""
A walkthrough test, to check pages are loading
"""

import pytest
from pages.whatsnew_page import WhatsNewPage
from pages.luma_home_page import LumaHomePage
from utils.logger import setup_logger

logger = setup_logger(__name__, 'smoke_test.log')


class TestWalkThrough:
    """
    Test Case for a walkthrough test
    """

    # @pytest.mark.smoke
    def test_walk_through(self, page):
        logger.info('Starting test: test_walk_through')

        home_page = LumaHomePage(page)
        luna_home_page = LumaHomePage(page)
        whatsnew_page = WhatsNewPage(page)

        home_page.go_to_site()
        home_page.go_to_whatsnew()

        logger.info('Test completed')
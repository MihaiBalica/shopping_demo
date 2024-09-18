class HomePageLocators:
    """
    Locators for home page
    """

    SEARCH_ENTIRE_STORE = '//div/input[@id="search"]'
    WHATS_NEW = '//a[span[text()="What\'s New"]]'
    SALE = '//a[span[text()="Sale"]]'
    TRAINING = '//a[span[text()="Training"]]'


class WhatsNewLocators:
    """
    Locators for WhatsNew page
    """
    MY_WISH_LIST = '//div[@class="block-title"]/strong[text()="My Wish List"]'
    NEW_LUMA_YOGA = '//a[@class="block-promo new-main"]//span[text()="New Luma Yoga Collection"]'
    WHATEVER_DAY_BRINGS = '//a[@class="block-promo new-performance"]//strong[text()="Whatever day brings"]'
    SENSE_OF_RENEWAL = '//a[@class="block-promo new-eco"]//strong[text()="A sense of renewal"]'

class SalesLocators:
    """
    Locators for Sales page
    """
    WOMENS_DEALS = '//a[@class="block-promo sale-main"]//strong[text()="Pristine prices on pants, tanks and bras."]'
    MENS_BARGAINS = '//a[@class="block-promo sale-mens"]//strong[text()="Men’s Bargains"]'
    LUMA_GEAR_STEALS = '//a[@class="block-promo sale-women"]//strong[text()="Luma Gear Steals"]'
    TWENTY_PERCENT_OFF = '//a[@class="block-promo sale-20-off"]//strong[text()="20% OFF"]'
    FREE_SHIPPING = '//a[@class="block-promo sale-free-shipping"]//strong[contains(text(),"Spend $50 or more")]'
    WOMENS_TEE_SALE = '//a[@class="block-promo sale-womens-t-shirts"]//strong[text()="You can\'t have too many tees"]'

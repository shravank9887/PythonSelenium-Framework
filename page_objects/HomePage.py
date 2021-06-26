from selenium.webdriver.common.by import By

from page_objects.ShopPage import ShopPage


class HomePage:

    # Variables for all object in
    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    # Clicks on the shop link top level menu
    # Returns the shop page object, where next interaction happens
    def get_shop_page(self):
        self.driver.find_element(*HomePage.shop_link).click()
        shop_page = ShopPage(self.driver)
        return shop_page

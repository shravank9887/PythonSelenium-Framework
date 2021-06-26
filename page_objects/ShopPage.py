# This class presents the shop page in the app
# Link to the shop page - https://rahulshettyacademy.com/angularpractice/shop
# All the objects in this page are captured here.
#
from selenium.webdriver.common.by import By


class ShopPage:

    # cards = self.driver.find_elements_by_css_selector(".card-title a")
    card_titles = (By.CSS_SELECTOR, ".card-title a")

    # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
    # Add button in the card footer
    card_footer_add_btn = (By.CSS_SELECTOR, ".card-footer button")

    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    # Checkout button in the shop page
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def find_card_titles(self):
        return self.driver.find_elements(*ShopPage.card_titles)

    def find_card_footer_add_btn(self):
        return self.driver.find_elements(*ShopPage.card_footer_add_btn)

    def find_checkout_btn(self):
        return self.driver.find_element(*ShopPage.checkout_btn)


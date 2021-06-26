from selenium.webdriver.common.by import By


class CheckoutPage:

    # cards = self.driver.find_elements_by_css_selector(".card-title a")
    card_titles = (By.CSS_SELECTOR,".card-title a")

    # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
    # Add button in the card footer
    card_footer_add_btn = (By.CSS_SELECTOR,".card-footer button")

    def __init__(self, driver):
        self.driver = driver

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_titles)

    def get_card_footer_add_btn(self):
        return self.driver.find_elements(*CheckoutPage.card_footer_add_btn)


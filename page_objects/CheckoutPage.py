from selenium.webdriver.common.by import By

from page_objects.ConfirmPage import ConfirmationPage


class CheckoutPage:

    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_page(self):
        self.driver.find_element(*CheckoutPage.checkout_btn).click()
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page



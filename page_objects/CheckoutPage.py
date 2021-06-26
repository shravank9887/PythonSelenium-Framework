from selenium.webdriver.common.by import By


class CheckoutPage:

    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def find_checkout_btn(self):
        return self.driver.find_elements(*CheckoutPage.checkout_btn)




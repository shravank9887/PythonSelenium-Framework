from selenium.webdriver.common.by import By


class ConfirmationPage:

    # self.driver.find_element_by_id("country").send_keys("ind")
    # location text box for entering delivery location on Confirmation page
    location_txt_bx = (By.ID, "country")

    # drop down list option India element locator
    list_option_india = (By.LINK_TEXT, "India")

    # Terms & conditions checkbox (tnc_checkbox) locator
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    tnc_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # Purchase button locator
    # self.driver.find_element_by_css_selector("[type='submit']").click()
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")

    # Purchase Success message locator
    # self.driver.find_element_by_css_selector("[class*='alert-success']")
    success_msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def find_location_txt_bx(self):
        return self.driver.find_element(*ConfirmationPage.location_txt_bx)

    def find_tnc_checkbox(self):
        return self.driver.find_element(*ConfirmationPage.tnc_checkbox)

    def find_list_option_india(self):
        return self.driver.find_element(*ConfirmationPage.list_option_india)

    def find_purchase_btn(self):
        return self.driver.find_element(*ConfirmationPage.purchase_btn)

    def find_success_msg(self):
        return self.driver.find_element(*ConfirmationPage.success_msg)




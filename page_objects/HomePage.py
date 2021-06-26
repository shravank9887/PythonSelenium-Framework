from selenium.webdriver.common.by import By


class HomePage:

    #Variables for all object in
    shop_link = (By.CSS_SELECTOR,"a[href*='shop']")

    def __init__(self,driver):
        self.driver = driver

    def shop_link(self):
        return self.driver.find_element(*HomePage.shop_link)
        #driver.find_element_by_css_selector("a[href*='shop']").
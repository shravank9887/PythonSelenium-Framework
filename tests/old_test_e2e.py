from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.CheckoutPage import CheckoutPage
from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestMod1(BaseClass):

    def test_TC1(self):
        home_page = HomePage(self.driver)
        home_page.shop_link().click()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        checkout_page = CheckoutPage(self.driver)
        cards = checkout_page.get_card_titles()
        #cards = self.driver.find_elements_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkout_page.get_card_footer_add_btn()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert("Success! Thank you!" in textMatch)


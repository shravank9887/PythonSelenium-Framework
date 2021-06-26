from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.CheckoutPage import CheckoutPage
from page_objects.HomePage import HomePage
from page_objects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestMod1(BaseClass):

    def test_tc1_place_order_blackberry(self):

        # Click on the shop link top level menu
        home_page = HomePage(self.driver)
        home_page.shop_link().click()

        # Get the list of card titles present it shop page
        shop_page = ShopPage(self.driver)
        cards = shop_page.find_card_titles()

        # Find the Item card with Blackberry title and click the add button on card footer
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            print(card_text)
            if card_text == "Blackberry":
                shop_page.find_card_footer_add_btn()[i].click()

        # Click on the Checkout Button on top right corner of shop page
        shop_page.find_checkout_btn().click()

        # After above step, user will be navigated from shop page to checkout page
        # Click checkout button in the Checkout page
        checkout_page = CheckoutPage(self.driver)
        checkout_page.find_checkout_btn().click()


        self.driver.find_element_by_id("country").send_keys("ind")

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        text_match = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert("Success! Thank you!" in text_match)


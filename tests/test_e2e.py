from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.CheckoutPage import CheckoutPage
from page_objects.ConfirmPage import ConfirmationPage
from page_objects.HomePage import HomePage
from page_objects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestMod1(BaseClass):

    def test_tc1_place_order_blackberry(self):

        # Create Homepage object
        home_page = HomePage(self.driver)

        # Click on the shop link top level menu
        # Returns the shop page object, where next interaction happens
        shop_page = home_page.get_shop_page()

        # Get the list of card titles present in shop page
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
        # this will open the checkout page and return checkout_page object
        checkout_page = shop_page.get_checkout_page()

        # After above step, user will be navigated from shop page to checkout page
        # Click checkout button in the Checkout page
        # Now the user will be navigate to Confirmation page.
        confirmation_page = checkout_page.get_confirmation_page()

        # Now user will on confirmation page, where he needs to enter shipping location.
        # Enter the keyword 'ind' to load the India location in the text box
        confirmation_page.find_location_txt_bx().send_keys("ind")

        # wait for the drop down list option to appear
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(confirmation_page.list_option_india))
        # click on the drop down list option India
        confirmation_page.find_list_option_india().click()

        # click on the checkbox for terms & conditions
        confirmation_page.find_tnc_checkbox().click()

        # Click on the Purchase button
        confirmation_page.find_purchase_btn().click()

        # Read Purchase success message
        text_match = confirmation_page.find_success_msg().text

        # Asserting if Success Message matches the expected Text
        assert("Success! Thank you!" in text_match)


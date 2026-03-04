from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text

    def get_basket_total_message_price(self):
        return self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE_PRICE
        ).text

    def should_be_correct_product_name_in_message(self, expected_name):
        actual_name = self.get_success_message_product_name()
        assert (
            actual_name == expected_name
        ), f"Wrong product name in message: expected {expected_name!r}, got {actual_name!r}"

    def should_be_correct_price_in_basket_message(self, expected_price):
        actual_price = self.get_basket_total_message_price()
        assert (
            actual_price == expected_price
        ), f"Wrong basket total: expected {expected_price!r}, got {actual_price!r}"

    def add_to_basket_and_solve_quiz(self):
        name = self.get_product_name()
        price = self.get_product_price()

        self.add_product_to_basket()
        self.solve_quiz_and_get_code()

        self.should_be_correct_product_name_in_message(name)
        self.should_be_correct_price_in_basket_message(price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ), "Success message is presented, but should not be"

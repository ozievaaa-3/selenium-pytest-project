from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    BASKET_TOTAL_MESSAGE_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")


# ✅ ДОБАВЬ ЭТО
class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    # иногда можно так: ".basket-mini a" — но btn обычно надёжнее


class BasketPageLocators:
    # товары в корзине (если есть)
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    # текст "Your basket is empty"
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.processors_catalog_page import low_price
from pages.processors_catalog_page import hight_price
import re


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:
    price_current = "//div[@class='price summary__price']"
    product_name = "//div[@class='cart-items__product-name']"
    buy_btn_main = "//button[@id='buy-btn-main']"
    first_step_buy = "//div[normalize-space()='1']"

    # Getters:
    def get_price_current(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_current)))
        element_text = element.text
        price = int(re.sub(r'[^\d]', '', element_text))
        return price

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name))).text

    print("Название продукта найдено")

    def get_buy_btn_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_btn_main)))

    def get_first_step_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_step_buy))).text

    # Actions:

    def click_buy_btn_main(self):
        self.get_buy_btn_main().click()
        print("Итоговая кнопка покупки нажата")

    def assert_price(self):
        assert low_price <= self.get_price_current() <= hight_price, f"Число 1 ({self.get_price_current()}) должно быть больше или равно числу 2 и меньше или равно числу 3"

    def assert_checkout(self):
        assert self.get_first_step_buy() == "1", f"Значение:({self.get_first_step_buy()}) должно быть равно 1"
        print("Осталось заполнить заявку")

        # Methods:

    def buy_select_processor(self):
        self.assert_price()
        print(f"Название процессора - {self.get_product_name()}\nЦена процессора - {self.get_price_current()}")
        self.click_buy_btn_main()
        self.assert_checkout()

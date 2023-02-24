from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

low_price = "10000"
hight_price = "20000"


class ProcessorCatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:

    rating = "//div[@data-id='rating']//label[@class='ui-checkbox']"
    lower_price_input = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]"
    hight_price_input = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[2]/input[1]"
    intel_developer = "(//label[@class='ui-checkbox ui-checkbox_list'])[8]"
    good_model = "//div[@data-id='rely']//label[@class='ui-checkbox']"
    for_gaming_pc_tray = "(//a[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list'])[5]"
    for_gaming_pc_checkbox = "(//label[@class='ui-checkbox ui-checkbox_list'])[9]"
    accept = "//button[contains(text(),'Применить')]"

    # Getters:

    def get_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rating)))

    def get_lower_price_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lower_price_input)))

    def get_hight_price_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hight_price_input)))

    def get_intel_developer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.intel_developer)))

    def get_good_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.good_model)))

    def get_for_gaming_pc_tray(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_gaming_pc_tray)))

    def get_for_gaming_pc_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_gaming_pc_checkbox)))

    def get_accept(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept)))

    # Actions:

    def click_rating(self):
        self.get_rating().click()
        print('Выбрано рейтинг 4 и выше')

    def set_low_price(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.lower_price_input))
        self.get_lower_price_input().send_keys(low_price)
        print("Минимальная цена установлена")

    def set_hight_price(self):
        self.scroll_to_element((By.XPATH, self.hight_price_input))
        self.get_hight_price_input().send_keys(hight_price)
        print("Максимальная цена установлена")

    def set_intel_developer(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.intel_developer))
        self.get_intel_developer().click()
        print("Выбран производитель intel")

    def set_good_model(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.good_model))
        self.get_good_model().click()
        print("Выбраны надежные модели")

    def open_for_gaming_pc_tray(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.for_gaming_pc_tray))
        self.get_for_gaming_pc_tray().click()
        print("Открыта вкладка для игрового ПК")

    def set_for_gaming_pc_checkbox(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.for_gaming_pc_checkbox))
        self.get_for_gaming_pc_checkbox().click()
        print("Выбраны процессоры для игрового ПК")

    def click_accept(self):
        time.sleep(3)
        self.scroll_to_element((By.XPATH, self.accept))
        self.get_accept().click()
        print("Изменения в фильтре приняты")

    # Methods

    def choose_intel_gaming_processor(self):
        self.click_rating()
        self.set_low_price()
        self.set_hight_price()
        self.set_intel_developer()
        self.set_good_model()
        self.open_for_gaming_pc_tray()
        self.set_for_gaming_pc_checkbox()
        self.click_accept()
        time.sleep(3)

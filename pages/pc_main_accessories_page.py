from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPCAccessoriesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:

    processors = "//div[@class='subcategory']//a[1]"

    # Getters:

    def get_processors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processors)))

    # Actions:

    def click_processors(self):
        self.get_processors().click()
        print('Переход в процессоры для ПК')

    # Methods

    def go_processors(self):
        self.click_processors()
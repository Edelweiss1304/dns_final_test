from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PCAccessoriesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:

    main_accessories = "//div[@class='subcategory__item-container ']//a[1]"

    # Getters:

    def get_main_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_accessories)))

    # Actions:

    def click_main_accessories(self):
        self.get_main_accessories().click()
        print('Переход в основные комплектующие для ПК')

    # Methods

    def go_pc_main_accessories(self):
        self.click_main_accessories()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Base:
    def __init__(self, driver):
        self.driver = driver

    """Сравнения слова на странице"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        try:
            # прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            # дожидаемся, пока элемент станет видимым
            WebDriverWait(self.driver, 30).until(EC.visibility_of(element))
        except TimeoutException:
            # если элемент не загрузился за 30 секунд, то начинаем прокручивать страницу вниз
            while True:
                # прокручиваем страницу вниз на одну страницу
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                # проверяем, виден ли элемент
                if element.is_displayed():
                    break
            else:
                # если элемент не загрузился за 30 секунд, то возникает TimeoutException
                print(f"Элемент {locator} не загрузился за 30 секунд")
        return element

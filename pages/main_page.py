from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

user_email = "smiledmitriev@gmail.com"
password_user = "S786tBX*&^F*(A)WD"


class MainPage(Base):
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:
    """Локатор кнопки меню"""
    login_menu = "//div[@class='user-menu']"

    """Локатор кнопки меню, когда пользователь вошел"""
    login_menu_logged = "//div[@class='user-menu user-menu_logged']"

    """Кнопка войти"""
    login_button_1 = "//button[@class='base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"

    """Кнопка войти с паролем"""
    login_with_password_button = "//div[@class='base-button-container base-button-container_blue']"

    """Поле с почтой или телефоном"""
    login_email = "input[autocomplete='username']"

    """Поле с паролем"""
    login_password = "input[autocomplete='current-password']"
    """Итоговая кнопка войти"""
    finally_login_button = "//button[@class='base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"

    """Имя вошедшего пользователя в меню"""
    user_mane_on_site = "//div[@class='user-profile__username']"

    """Кнопка комплектующие для пк"""
    pc_accessories = "//a[contains(text(),'Комплектующие для ПК')]"

    # Комплектующие для пк

    """Текст на странице комплектующие для пк"""
    successful_transition = "//h1[contains(text(),'Комплектующие для ПК')]"

    # Getters:

    def get_pc_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pc_accessories)))

    def get_successful_transition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.successful_transition)))

    def get_login_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_menu)))

    def get_login_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_1)))

    def get_login_with_password_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_with_password_button)))

    def get_login_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_email)))

    def get_login_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_password)))

    def get_finally_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finally_login_button)))

    def get_user_name_on_site(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_mane_on_site)))

    def get_login_menu_logged(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_menu_logged)))

    # Actions:

    def click_pc_accessories(self):
        self.get_pc_accessories().click()
        print('Переход в комплектующие для ПК')

    def open_login_menu(self):
        login_menu = self.get_login_menu()
        actions = ActionChains(self.driver)
        actions.move_to_element(login_menu).perform()

    def click_login_button_1(self):
        self.get_login_button_1().click()

    def click_login_with_password_button(self):
        self.get_login_with_password_button().click()

    def click_login_field(self):
        self.get_login_email().click()

    def click_password_field(self):
        self.get_login_password().click()

    def fill_login_info(self):
        self.get_login_email().send_keys(user_email)

    def fill_password_info(self):
        self.get_login_password().send_keys(password_user)

    def click_finally_login_button(self):
        self.get_finally_login_button().click()

    def open_login_menu_logged(self):
        login_menu_logged = self.get_login_menu_logged()
        actions = ActionChains(self.driver)
        actions.move_to_element(login_menu_logged).perform()

    # Methods

    def open_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login_on_site(self):
        self.open_login_menu()
        self.click_login_button_1()
        self.click_login_with_password_button()
        self.click_login_field()
        self.fill_login_info()
        self.click_password_field()
        self.fill_password_info()
        self.click_finally_login_button()
        time.sleep(5)
        self.driver.refresh()
        self.open_login_menu_logged()
        self.assert_word(self.get_user_name_on_site(), 'Алексей Дмитриев')
        print("Вход выполнен, имя пользователя совпадает")

    def go_pc_accessories(self):
        self.click_pc_accessories()
        self.assert_word(self.get_successful_transition(), 'Комплектующие для ПК')

from pages.main_page import MainPage
from pages.pc_accessories_page import PCAccessoriesPage
from pages.pc_main_accessories_page import MainPCAccessoriesPage
from pages.processors_catalog_page import ProcessorCatalogPage
from pages.cart_page import CartPage
from utilities.Conftest import driver


def test_select_intel_gaming_processor(driver):
    mp = MainPage(driver)
    mp.open_site()
    capture_path = 'your_desired_filename.png'
    driver.save_screenshot(capture_path)

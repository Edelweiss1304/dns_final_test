from pages.main_page import MainPage
from pages.pc_accessories_page import PCAccessoriesPage
from pages.pc_main_accessories_page import MainPCAccessoriesPage
from pages.processors_catalog_page import ProcessorCatalogPage
from pages.cart_page import CartPage
from utilities.Conftest import driver


def test_select_intel_gaming_processor(driver):
    mp = MainPage(driver)
    mp.open_site()
    mp.login_on_site()
    mp.go_pc_accessories()

    ap = PCAccessoriesPage(driver)
    ap.go_pc_main_accessories()

    pma = MainPCAccessoriesPage(driver)
    pma.go_processors()

    pc = ProcessorCatalogPage(driver)
    pc.choose_intel_gaming_processor()

    cp = CartPage(driver)
    cp.buy_select_processor()


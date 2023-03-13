import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    yield driver
    driver.quit()
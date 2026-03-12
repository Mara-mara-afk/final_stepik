import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nStarting browser for test...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    print("\nQuitting browser...")
    driver.quit()
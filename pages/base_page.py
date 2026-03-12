from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    # Пример универсального метода для BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.locators.LOGIN_LINK)
        login_link.click()
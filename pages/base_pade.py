from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_clickable(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_changing_url(self, url):
        return WebDriverWait(self.driver, 20).until(expected_conditions.url_changes(url))

    def wait_for_invisible(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def waiting_for_text_changed(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

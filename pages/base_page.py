import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


from conftest import driver

import allure
from selenium import webdriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Перетащить элемент {drag_element} на место {drop_element}')
    def drag_and_drop_element(self, drag_element, drop_element):
        drag = self.find_element(drag_element)
        drop = self.find_element(drop_element)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()

    @allure.step('Открыть страницу: {url}')
    def open_url(self, url: str):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator: tuple, timeout: int = None):
        try:
            if timeout:
                wait = WebDriverWait(self.driver, timeout)
            else:
                wait = self.wait
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(
                f"Элемент {locator} не найден после {timeout if timeout else 10} секунд")


    @allure.step("Нажать на элемент {locator}")
    def click_element(self, locator: tuple):
        try:
            time.sleep(3)
            element = self.find_element(locator)
            wait = self.wait
            wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            time.sleep(5)
            element = self.find_element(locator)
            element.click()

    @allure.step("Ввести текст {text} в элемент {locator}")
    def send_keys(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Открываем браузер Firefox')
    def init_driver(self):
        return webdriver.Firefox()

    @allure.step('Открываем страницу {page}')
    def open_page(self, driver, page):
        driver.get(page)

    @allure.step('Получаем URL открытой страницы')
    def get_current_url(self, driver):
        current_url = driver.current_url
        return current_url

    @allure.step('Закрываем браузер')
    def quit_driver(self, driver):
        driver.quit()


    @allure.step('Проверить, что текст в элементе {locator} соответствует {expected_text}')
    def assert_text(self, locator: tuple, expected_text: str, timeout: int = None):

        element = self.find_element(locator, timeout)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}' for {locator}"
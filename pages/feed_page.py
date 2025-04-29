import allure
import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import Locators

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Поиск заказа с ID: {order_id} в ленте")
    def find_order_in_feed(self, order_id):
        dynamic_locator = (By.XPATH, f"//*[text()='{order_id}']")
        return self.find_element(dynamic_locator)

    @allure.step("Получить текущее значение счётчика заказов")
    def get_total_orders(self):
        total_orders_text = self.find_element(Locators.TOTAL_ORDERS).text
        return int(re.sub(r'\D', '', total_orders_text))

    @allure.step("Ожидание увеличения счётчика заказов")
    def wait_for_total_orders_to_increase(self, initial_total):
        WebDriverWait(self.driver, 10).until(
            lambda d: int(re.sub(r'\D', '', self.find_element(Locators.TOTAL_ORDERS).text)) > initial_total
        )

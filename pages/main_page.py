import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Поиск заказа с ID: {order_id} в ленте заказов")
    def find_order_by_id(self, order_id):
        locator = (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderList')]//*[text()='{order_id}']")
        return self.find_element(locator)
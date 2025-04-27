import allure

from pages.base_pade import BasePage
from locators import OrdersPageLocators


class OrdersPage(BasePage):
    @allure.step('Дождаться загрузки страницы с лентой заказов')
    def loading_order_page(self):
        return self.find_element_located(OrdersPageLocators.ORDER_FEED_HEADER)

    @allure.step('Нажать на заказ')
    def click_on_order(self):
        return self.find_element_clickable(OrdersPageLocators.ORDER)

    @allure.step('Дождаться открытия модального окна с информацией о заказе')
    def opening_order_details_window(self):
        return self.find_element_located(OrdersPageLocators.MODAL_WINDOW_ORDER_DETAILS)

    @allure.step('Получить список заказов')
    def get_orders_list(self):
        return self.find_element_located(OrdersPageLocators.ORDER_FEED)

    @allure.step('Получить количество всех заказов')
    def get_all_orders_number(self):
        number = self.find_element_located(OrdersPageLocators.ALL_ORDERS_NUMBER).text
        return int(number)

    @allure.step('Получить количество всех заказов на сегодня')
    def get_today_orders_number(self):
        number = self.find_element_located(OrdersPageLocators.TODAY_ORDER_NUMBER).text
        return int(number)

    @allure.step('Получить заказы в статусе "В работе"')
    def get_list_preparing_orders(self):
        return self.find_element_located(OrdersPageLocators.PREPARING_ORDERS_FEED).text

    @allure.step('Дождаться появления заказа в блоке "В работе"')
    def wait_changing_preparing_orders_list(self, order_number):
        self.waiting_for_text_changed(OrdersPageLocators.PREPARING_ORDERS_FEED, order_number)


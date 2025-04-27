import allure

from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.profile_page import ProfilePage
from constants import Urls


class TestOrdersFeed:

    @allure.title('Открытие модального окна с инфо о заказе')
    @allure.description('Открытие модального окна с инфо о заказе при нажатии на заказ в ленте заказов')
    def test_model_window_with_order_details_is_opening(self, driver):
        page = OrdersPage(driver)
        page.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)
        page.loading_order_page()
        page.click_on_order()

        assert page.opening_order_details_window().is_displayed()

    @allure.title('Отображение заказа из истории заказов в ленте заказов')
    def test_order_from_history_showing_in_order_feed(self, driver, order):
        page = MainPage(driver)
        page.click_on_order_button()
        page.click_close_modal_window_button()
        page.wait_for_modal_window_closing()
        page.click_on_personal_cabinet_button()
        profile_page = ProfilePage(driver)
        profile_page.loading_profile_page()
        profile_page.click_on_history_link()
        order_number = profile_page.get_order_number_from_history()
        page = MainPage(driver)
        page.click_on_order_feed_button()
        order_feed = OrdersPage(driver)
        orders_list = order_feed.get_orders_list().text

        assert order_number in orders_list

    @allure.title('Увеличение счетчика "Выполнено за всё время" при создании заказа')
    def test_all_orders_counter_incrementing(self, driver, user_login):
        order_page = OrdersPage(driver)
        order_page.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)
        all_orders_number_before = order_page.get_all_orders_number()
        order_page.open_page(Urls.BASE_URL)
        page = MainPage(driver)
        page.make_an_order()
        page.click_on_order_feed_button()
        order_page = OrdersPage(driver)
        order_page.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)
        all_orders_number_after = order_page.get_all_orders_number()

        assert all_orders_number_after > all_orders_number_before

    @allure.title('Увеличение счетчика "Выполнено за сегодня" при создании заказа')
    def test_today_orders_counter_incrementing(self, driver, user_login):
        order_page = OrdersPage(driver)
        order_page.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)
        today_orders_number_before = order_page.get_today_orders_number()
        order_page.open_page(Urls.BASE_URL)
        page = MainPage(driver)
        page.make_an_order()
        page.click_on_order_feed_button()
        order_page = OrdersPage(driver)
        order_page.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)
        today_orders_number_after = order_page.get_today_orders_number()

        assert today_orders_number_after > today_orders_number_before

    @allure.title('Появление номера заказа в блоке "В работе"')
    def test_order_in_preparing_list(self, driver, order):
        page = MainPage(driver)
        page.click_on_order_button()
        page.opening_order_model_window()
        page.wait_changing_order_number()
        number = page.get_order_number()
        page.click_close_modal_window_button()
        page.click_on_order_feed_button()
        order_page = OrdersPage(driver)
        order_page.wait_changing_preparing_orders_list(number)
        preparing_orders_list = order_page.get_list_preparing_orders()

        assert number in preparing_orders_list






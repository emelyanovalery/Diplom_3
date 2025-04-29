from selenium.webdriver.common.by import By
from conftest import driver
from constants import Constants
from locators.feed_page_locators import Locators
import allure
from conftest import user_login
from pages.feed_page import FeedPage


class TestsFeedPage:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_sostav(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page(driver, Constants.URL)
        feed_page.click_element(Locators.ORDERS)
        feed_page.click_element(Locators.FIRST_ORDER_SELECTION)
        popup = feed_page.find_element(Locators.SOSTAV)
        assert popup.is_displayed()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_feed_check(self, driver, user_login):
        feed_page = FeedPage(driver)
        feed_page.open_page(driver, Constants.URL)
        feed_page.click_element(Locators.LK_BUTTON)
        feed_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        feed_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        feed_page.click_element(Locators.ENTER_BUTTON)
        feed_page.drag_and_drop_element(Locators.SHINE_BULKA, Locators.ORDER_PLACE)
        feed_page.click_element(Locators.MAKE_ORDER)
        feed_page.click_element(Locators.CLOSE_DETAILS)
        feed_page.click_element(Locators.LK_BUTTON)
        feed_page.click_element(Locators.ORDERS_HISTORY)
        order_id = feed_page.find_element(Locators.ORDER_ID).text
        feed_page.click_element(Locators.ORDERS)
        assert feed_page.find_order_in_feed(order_id)

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_feed_total(self, driver, user_login):
        feed_page = FeedPage(driver)
        feed_page.open_page(driver, Constants.URL)
        feed_page.click_element(Locators.LK_BUTTON)
        feed_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        feed_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        feed_page.click_element(Locators.ENTER_BUTTON)
        feed_page.click_element(Locators.ORDERS)
        total_orders = feed_page.get_total_orders()
        feed_page.click_element(Locators.CONSTRUCTOR)
        feed_page.drag_and_drop_element(Locators.SHINE_BULKA, Locators.ORDER_PLACE)
        feed_page.click_element(Locators.MAKE_ORDER)
        feed_page.click_element(Locators.CLOSE_DETAILS)
        feed_page.click_element(Locators.ORDERS)
        feed_page.wait_for_total_orders_to_increase(total_orders)
        new_total = feed_page.get_total_orders()
        assert new_total == total_orders + 1, f"Ожидали {total_orders + 1}, но получили {new_total}"

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_feed_today(self, driver, user_login):
        feed_page = FeedPage(driver)
        feed_page.open_page(driver, Constants.URL)
        feed_page.click_element(Locators.LK_BUTTON)
        feed_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        feed_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        feed_page.click_element(Locators.ENTER_BUTTON)
        feed_page.click_element(Locators.ORDERS)
        total_orders = feed_page.find_element(Locators.TODAY_ORDERS).text
        feed_page.click_element(Locators.CONSTRUCTOR)
        feed_page.drag_and_drop_element(Locators.SHINE_BULKA, Locators.ORDER_PLACE)
        feed_page.click_element(Locators.MAKE_ORDER)
        feed_page.click_element(Locators.CLOSE_DETAILS)
        feed_page.click_element(Locators.ORDERS)
        assert feed_page.find_element(Locators.TODAY_ORDERS).text == str(int(total_orders)+1)
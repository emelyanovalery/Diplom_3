from conftest import driver
from locators.main_page_locators import Locators
from constants import Constants
from selenium.webdriver.common.by import By
from helpers import Helpers

import allure

from pages.main_page import MainPage

from conftest import user_login

class TestsMainPage:
    @allure.title('переход по клику на «Конструктор»')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.click_element(Locators.ORDERS)
        main_page.click_element(Locators.CONSTRUCTOR)
        assert main_page.find_element(Locators.COMBINE_BURGER)

    @allure.title('переход по клику на «Лента заказов»')
    def test_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.click_element(Locators.ORDERS)
        assert main_page.get_current_url(driver) == Constants.FEED_URL

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.click_element(Locators.SHINE_BULKA)
        assert main_page.find_element(Locators.INGREDIENT_DETAILS)

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.click_element(Locators.SHINE_BULKA)
        main_page.click_element(Locators.CLOSE_DETAILS)
        assert not main_page.find_element(Locators.INGREDIENT_DETAILS)

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.drag_and_drop_element(Locators.SHINE_BULKA, Locators.ORDER_PLACE)
        assert main_page.find_element(Locators.PRICE).text != '0'

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_constructor_button(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.open_page(driver, Constants.URL)
        main_page.click_element(Locators.LK_BUTTON)
        main_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        main_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        main_page.click_element(Locators.ENTER_BUTTON)
        main_page.click_element(Locators.ORDERS)
        helpers = Helpers(driver)
        order_id = helpers.get_order_id(access_token=user_login[2])
        assert main_page.find_element(locator=(By.XPATH, f"//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/ *[text() = '{order_id}']"))
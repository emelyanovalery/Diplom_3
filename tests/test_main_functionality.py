import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from constants import Urls


class TestMainFunctionality:

    @allure.title('Переход к конструктору')
    @allure.description('Переход к конструктору при нажатии на кнопку «Конструктор» в хедере')
    def test_redirect_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN_URL)
        login_page.loading_login_page()
        page = MainPage(driver)
        page.click_on_constructor_button()

        assert page.make_order_is_showing().is_displayed()

    @allure.title('Переход в ленту заказов')
    @allure.description('Переход к ленту заказов при нажатии на кнопку «Лента заказов» в хедере')
    def test_redirect_to_order_feed(self, driver):
        page = MainPage(driver)
        page.loading_main_page()
        page.click_on_order_feed_button()
        order_page = OrdersPage(driver)

        assert order_page.loading_order_page().is_displayed()

    @allure.title('Открытие модального окна с инфо об ингредиенте')
    @allure.description('Открытие модального окна с инфо об ингредиенте при нажатии на ингредиент на странице '
                        'конструктора')
    def test_modal_window_with_ingredient_details(self, driver):
        page = MainPage(driver)
        page.loading_main_page()
        page.click_on_ingredient()

        assert page.opening_ingredient_details_window().is_displayed()

    @allure.title('Закрытие модального окна с инфо об ингредиенте')
    @allure.description('Закрытие модального окна с инфо об ингредиенте при нажатии на крестик')
    def test_closing_modal_window_with_ingredient_details(self, driver):
        page = MainPage(driver)
        page.loading_main_page()
        page.click_on_ingredient()
        page.opening_ingredient_details_window()
        page.click_close_modal_window_button()
        page.wait_for_modal_window_closing()

        assert not page.wait_for_modal_window_closing().is_displayed()

    @allure.title('Увеличение числа в счетчике ингредиентов')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_counting_ingredients(self, driver):
        page = MainPage(driver)
        page.loading_main_page()
        count_ingredients_before = page.get_ingredients_number()
        page.put_sauce_into_basket()
        count_ingredients_after = page.get_ingredients_number()

        assert count_ingredients_before + 1 == count_ingredients_after

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_make_order_with_auth(self, driver, user, order):
        page = MainPage(driver)
        page.click_on_order_button()

        assert page.opening_order_model_window().is_displayed()


import allure

from pages.base_pade import BasePage
from locators import MainPageLocators
from seletools.actions import drag_and_drop
from constants import Urls


class MainPage(BasePage):

    @allure.step('Дождаться загрузки главной страницы')
    def loading_main_page(self):
        return self.find_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step('Перейти в личный кабинет')
    def click_on_personal_cabinet_button(self):
        return self.find_element_clickable(MainPageLocators.PERSONAL_ACC_BUTTON)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        return self.find_element_clickable(MainPageLocators.ORDER_BUTTON)

    @allure.step('Перейти к конструктору')
    def click_on_constructor_button(self):
        return self.find_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Найти хедер "Соберите бургер"')
    def make_order_is_showing(self):
        return self.find_element_located(MainPageLocators.MAKE_ORDER_HEADER)

    @allure.step('Перейти к ленте заказов')
    def click_on_order_feed_button(self):
        return self.find_element_clickable(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажать на ингредиент')
    def click_on_ingredient(self):
        return self.find_element_clickable(MainPageLocators.BURGER_NAME)

    @allure.step('Дождаться открытия модального окна с информацией об ингредиенте')
    def opening_ingredient_details_window(self):
        return self.find_element_located(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Закрыть модальное окна с информацией об ингредиенте')
    def click_close_modal_window_button(self):
        return self.find_element_clickable(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Дождаться закрытия модального окна с информацией об ингредиенте')
    def wait_for_modal_window_closing(self):
        return self.wait_for_invisible(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Добавить соус в корзину')
    def put_sauce_into_basket(self):
        ingredient = self.find_element_located(MainPageLocators.SAUCE_NAME)
        basket = self.find_element_located(MainPageLocators.BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Добавить булку в корзину')
    def put_bun_into_basket(self):
        ingredient = self.find_element_located(MainPageLocators.BURGER_NAME)
        basket = self.find_element_located(MainPageLocators.BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Получить кол-во ингредиента в корзине')
    def get_ingredients_number(self):
        num = self.find_element_located(MainPageLocators.INGREDIENT_COUNTER).text
        return int(num)

    @allure.step('Дождаться открытия модального окна с информацией о заказе')
    def opening_order_model_window(self):
        return self.find_element_located(MainPageLocators.ORDER_MODAL_WINDOW)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.find_element_located(MainPageLocators.ORDER_NUMBER).text

    @allure.step('Сделать заказ')
    def make_an_order(self):
        self.put_bun_into_basket()
        self.put_sauce_into_basket()
        self.click_on_order_button()
        self.opening_order_model_window()
        order_number = self.get_order_number()
        self.click_close_modal_window_button()
        return order_number

    @allure.step('Дождаться появления номера заказа в модальном окне')
    def wait_changing_order_number(self):
        self.waiting_for_text_changed(MainPageLocators.ORDER_NUMBER, '7')

    @allure.step('Дождаться смены урла на урл главной страницы')
    def changing_url_main(self):
        self.wait_changing_url(Urls.BASE_URL)

    @allure.step('Дождаться смены урла на урл страницы профиля')
    def changing_url_profile(self):
        self.wait_changing_url(Urls.BASE_URL + Urls.PROFILE_URL)

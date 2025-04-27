import allure

from pages.base_pade import BasePage
from locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step('Дождаться загрузки страницы с профилем')
    def loading_profile_page(self):
        return self.find_element_located(ProfilePageLocators.PROFILE_LINK)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_on_history_link(self):
        return self.find_element_clickable(ProfilePageLocators.HISTORY_LINK)

    @allure.step('Нажать на кнопку "Выход"')
    def click_on_logout_link(self):
        return self.find_element_clickable(ProfilePageLocators.LOGOUT_LINK)

    @allure.step('Получить номер заказа')
    def get_order_number_from_history(self):
        num = self.find_element_located(ProfilePageLocators.NUMBER_OF_ORDER_IN_HISTORY_DETAILS).text
        return num[1:]

import allure

from pages.base_pade import BasePage
from locators import LoginPageLocators
from constants import Urls


class LoginPage(BasePage):

    @allure.step('Дождаться загрузки страницы авторизации')
    def loading_login_page(self):
        return self.find_element_located(LoginPageLocators.LOGIN_EMAIL)

    @allure.step('Нажать на "Восстановить пароль')
    def click_on_forgot_password_link(self):
        return self.find_element_clickable(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Ввести почту')
    def set_email(self, email):
        return self.find_element_located(LoginPageLocators.LOGIN_EMAIL).send_keys(email)

    @allure.step('Ввести пароль')
    def set_password(self, password):
        return self.find_element_located(LoginPageLocators.LOGIN_PASSWORD).send_keys(password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_on_login_button(self):
        return self.find_element_clickable(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Дождаться смены урла на урл страницы авторизации')
    def changing_url_login(self):
        return self.wait_changing_url(Urls.BASE_URL + Urls.LOGIN_URL)

    @allure.step('Дождаться появления кнопки войти')
    def wait_for_login_button(self):
        return self.find_element_located(LoginPageLocators.LOGIN_BUTTON)

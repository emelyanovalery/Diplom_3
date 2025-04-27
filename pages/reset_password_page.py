import allure

from pages.base_pade import BasePage
from locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    @allure.step('Дождаться загрузки страницы со сбросом пароля')
    def loading_reset_password_page(self):
        return self.find_element_located(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Нажать на кнопку "скрыть/показать" пароль')
    def click_on_eye_button(self):
        return self.find_element_clickable(ResetPasswordPageLocators.EYE_BUTTON)

    @allure.step('Дождаться перемещения курсора в поле для пароля')
    def password_field_is_active(self):
        return self.find_element_located(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
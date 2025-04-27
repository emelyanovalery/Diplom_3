from conftest import driver
from constants import Constants
from locators.login_page_locators import Locators
import allure
from pages.login_page import LoginPage

class TestsLoginPage:
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_reset_login_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(driver, Constants.LOGIN_PAGE_URL)
        login_page.click_element(Locators.RESET_PASSWORD)
        assert login_page.get_current_url(driver) == Constants.FORGOT_URL

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_mail_and_reset_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(driver, Constants.LOGIN_PAGE_URL)
        login_page.click_element(Locators.RESET_PASSWORD)
        login_page.send_keys(Locators.EMAIL_FIELD, 'test@mail.com')
        login_page.click_element(Locators.RESET_PASSWORD_WITH_EMAIL)
        assert login_page.get_current_url(driver) == Constants.FORGOT_URL

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_field_active(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(driver, Constants.LOGIN_PAGE_URL)
        login_page.click_element(Locators.SHOW_PASSWORD)
        assert Locators.ACTIVE_PASSWORD_FIELD
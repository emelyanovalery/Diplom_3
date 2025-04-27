import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from constants import Urls


class TestPersonalAccount:

    @allure.title('Переход в личный кабинет')
    def test_redirect_to_personal_account(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.BASE_URL)
        page.loading_main_page()
        page.click_on_personal_cabinet_button()

        assert page.get_current_url() == Urls.BASE_URL + Urls.LOGIN_URL

    @allure.title('Переход в историю заказов')
    def test_order_history(self, driver, user_login):
        profile_page = ProfilePage(driver)
        profile_page.loading_profile_page()
        profile_page.click_on_history_link()

        assert profile_page.get_current_url() == Urls.BASE_URL + Urls.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, user_login):
        profile_page = ProfilePage(driver)
        profile_page.loading_profile_page()
        profile_page.click_on_logout_link()
        login_page = LoginPage(driver)

        assert login_page.wait_for_login_button().is_displayed()

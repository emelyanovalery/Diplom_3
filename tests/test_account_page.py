from conftest import driver
from constants import Constants
from locators.account_page_locators import Locators
import allure
from conftest import user_login
from pages.account_page import AccountPage


class TestsAccountPage:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_logging_in(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(driver, Constants.URL)
        account_page.click_element(Locators.LK_BUTTON)
        assert account_page.get_current_url(driver) == Constants.LOGIN_PAGE_URL

    @allure.title('переход в раздел «История заказов»')
    def test_order_history(self, driver, user_login):
        account_page = AccountPage(driver)
        account_page.open_page(driver, Constants.URL)
        account_page.click_element(Locators.LK_BUTTON)
        account_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        account_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        account_page.click_element(Locators.ENTER_BUTTON)
        account_page.click_element(Locators.LK_BUTTON)
        account_page.click_element(Locators.ORDERS_HISTORY)
        assert account_page.find_element(Locators.ORDERS_HISTORY_HIGHLIGHTED)


    @allure.title('выход из аккаунта')
    def test_logout(self, driver, user_login):
        account_page = AccountPage(driver)
        account_page.open_page(driver, Constants.URL)
        account_page.click_element(Locators.LK_BUTTON)
        account_page.send_keys(Locators.EMAIL_FIELD, user_login[0])
        account_page.send_keys(Locators.PASSWORD_FIELD, user_login[1])
        account_page.click_element(Locators.ENTER_BUTTON)
        account_page.click_element(Locators.LK_BUTTON)
        account_page.click_element(Locators.LOGOUT_BUTTON)
        assert account_page.find_element(Locators.ENTER_LABEL)
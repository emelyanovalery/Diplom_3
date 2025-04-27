import allure
from faker import Faker
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.reset_password_page import ResetPasswordPage
from constants import Urls


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_redirect_to_recovery_password_page(self, driver):
        page = LoginPage(driver)
        page.open_page(Urls.BASE_URL + Urls.LOGIN_URL)
        page.loading_login_page()
        page.click_on_forgot_password_link()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.loading_rec_password_page()

        assert recovery_page.get_current_url() == Urls.BASE_URL + Urls.RECOVERY_PASSWORD_URL

    @allure.title('Восстановление пароля: ввод почты и клик по кнопке «Восстановить»')
    def test_set_email_for_password_recovery(self, driver):
        email = Faker().email()
        page = RecoveryPasswordPage(driver)
        page.open_page(Urls.BASE_URL + Urls.RECOVERY_PASSWORD_URL)
        page.loading_rec_password_page()
        page.set_email(email)
        page.click_on_recovery_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.loading_reset_password_page()

        assert reset_page.get_current_url() == Urls.BASE_URL + Urls.RESET_PASSWORD_URL

    @allure.title('Восстановление пароля: поле с паролем активно при нажатии на показ пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_active_password_field(self, driver):
        email = Faker().email()
        page = RecoveryPasswordPage(driver)
        page.open_page(Urls.BASE_URL + Urls.RECOVERY_PASSWORD_URL)
        page.loading_rec_password_page()
        page.set_email(email)
        page.click_on_recovery_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.loading_reset_password_page()
        reset_page.click_on_eye_button()

        assert reset_page.password_field_is_active().is_displayed()



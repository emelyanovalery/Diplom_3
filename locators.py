from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.XPATH, './/a[@href="/"]')
    PERSONAL_ACC_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    MAKE_ORDER_HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')

    BURGER_NAME = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS_HEADER = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    CLOSE_MODAL_WINDOW_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK')

    SAUCE_NAME = (By.XPATH, './/p[text()="Соус Spicy-X"]')
    BASKET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
    INGREDIENT_COUNTER = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p['
                                    '@class="counter_counter__num__3nue1"]')

    ORDER_MODAL_WINDOW = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]')
    ORDER_NUMBER = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text '
                              'text_type_digits-large mb-8"]')


class LoginPageLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]')
    LOGIN_EMAIL = (By.XPATH, './/input[@name = "name"]')
    LOGIN_PASSWORD = (By.XPATH, './/input[@name = "Пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')


class RecoveryPasswordPageLocators:
    HEADER_RECOVERY_PASSWORD = (By.XPATH, './/h2[text()="Восстановление пароля"]')
    RECOVERY_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::*')
    RECOVERY_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')


class ResetPasswordPageLocators:
    SAVE_BUTTON = (By.XPATH, './/button[text()="Сохранить"]')
    EYE_BUTTON = (By.CSS_SELECTOR, '.input__icon.input__icon-action')
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, '.input.input_status_active')


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, './/a[text()="Профиль"]')
    HISTORY_LINK = (By.XPATH, './/a[text()="История заказов"]')
    LOGOUT_LINK = (By.XPATH, './/button[text()="Выход"]')
    ORDER_IN_HISTORY_DETAILS = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][last()]/a['
                                          '@class="OrderHistory_link__1iNby"]')
    NUMBER_OF_ORDER_IN_HISTORY_DETAILS = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][last()]//p['
                                                    '@class="text text_type_digits-default"]')


class OrdersPageLocators:
    ORDER_FEED_HEADER = (By.XPATH, './/h1[text()="Лента заказов"]') # это заголовок с лентой заказов, а не кнопка из хедера
    ORDER = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][1]/a[@class="OrderHistory_link__1iNby"]')
    MODAL_WINDOW_ORDER_DETAILS = (By.XPATH, './/p[text()="Cостав"]')
    ORDER_FEED = (By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]')
    ALL_ORDERS_NUMBER = (By.XPATH, './/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text '
                                   'text_type_digits-large"]')
    TODAY_ORDER_NUMBER = (By.XPATH, '(.//div/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[2]')
    PREPARING_ORDERS_FEED = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')

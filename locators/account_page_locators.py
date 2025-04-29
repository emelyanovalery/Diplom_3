from selenium.webdriver.common.by import By

class Locators:

    LK_BUTTON = (By.XPATH, "// *[text() = 'Личный Кабинет']")
    EMAIL_FIELD = (By.XPATH, "//input[@class ='text input__textfield text_type_main-default' and @name = 'name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class ='text input__textfield text_type_main-default' and @name = 'Пароль']")
    ENTER_BUTTON = (By.XPATH, "// *[text() = 'Войти']")
    ORDERS_HISTORY = (By.XPATH, "// *[text() = 'История заказов']")
    ORDERS_HISTORY_HIGHLIGHTED = (By.XPATH, "//a[@class ='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
    LOGOUT_BUTTON = (By.XPATH, "// *[text() = 'Выход']")
    ENTER_LABEL = (By.XPATH, "// *[text() = 'Вход']")
from selenium.webdriver.common.by import By

class Locators:
    RESET_PASSWORD = (By.XPATH, "// *[text() = 'Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, "//input[@class ='text input__textfield text_type_main-default']")
    RESET_PASSWORD_WITH_EMAIL = (By.XPATH, "// *[text() = 'Восстановить']")
    SHOW_PASSWORD = (By.XPATH, "//div[@class ='input__icon input__icon-action']")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[@class ='input pr-6 pl-6 input_type_password input_size_default input_status_active']")
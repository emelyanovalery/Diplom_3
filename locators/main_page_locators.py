from selenium.webdriver.common.by import By

class Locators:
    ORDERS = (By.XPATH, "// *[text() = 'Лента Заказов']")
    CONSTRUCTOR = (By.XPATH, "// *[text() = 'Конструктор']")
    COMBINE_BURGER = (By.XPATH, "// *[text() = 'Соберите бургер']")
    INGREDIENT_DETAILS = (By.XPATH, "// *[text() = 'Детали ингредиента']")
    SHINE_BULKA = (By.XPATH, "// *[text() = 'Флюоресцентная булка R2-D3']")
    MAKE_ORDER = (By.XPATH, "// *[text() = 'Оформить заказ']")
    ORDER_CREATED = (By.XPATH, "// *[text() = 'идентификатор заказа']")
    ORDER_PLACE = (By.XPATH, "//div[@class ='constructor-element constructor-element_pos_top']")
    PRICE = (By.XPATH, "//p[@class ='text text_type_digits-medium mr-3']")
    CLOSE_DETAILS = (By.XPATH, "//button[@class ='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    LK_BUTTON = (By.XPATH, "// *[text() = 'Личный Кабинет']")
    EMAIL_FIELD = (By.XPATH, "//input[@class ='text input__textfield text_type_main-default' and @name = 'name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class ='text input__textfield text_type_main-default' and @name = 'Пароль']")
    ENTER_BUTTON = (By.XPATH, "// *[text() = 'Войти']")
    PREPARE_ORDER = (By.XPATH, "//ul[@class ='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class ='text text_type_digits-default mb-2']")
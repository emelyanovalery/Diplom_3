import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from helper import AuthResponses
from helper import UserData
from constants import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        chrome_driver = ChromeDriverManager().install()
        service = CS(chrome_driver)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = UserData.generate_fake_user_data()
    response = AuthResponses.create_user(user)
    yield user

    AuthResponses.delete_user(response)


@pytest.fixture
def user_login(driver, user):
    main_page = MainPage(driver)
    main_page.click_on_personal_cabinet_button()
    login_page = LoginPage(driver)
    login_page.set_email(user['email'])
    login_page.set_password(user['password'])
    login_page.click_on_login_button()
    login_page.changing_url_login()
    main_page = MainPage(driver)
    main_page.click_on_personal_cabinet_button()
    main_page.changing_url_main()
    main_page.changing_url_profile()


@pytest.fixture
def order(driver, user):
    login_page = LoginPage(driver)
    login_page.open_page(Urls.BASE_URL + Urls.LOGIN_URL)
    login_page.set_email(user['email'])
    login_page.set_password(user['password'])
    login_page.click_on_login_button()
    login_page.changing_url_login()
    page = MainPage(driver)
    page.put_bun_into_basket()
    page.put_sauce_into_basket()

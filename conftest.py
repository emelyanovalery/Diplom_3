import pytest
from selenium import webdriver
from constants import Constants
from faker import Faker
import requests
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        options = FirefoxOptions()
        options.set_preference("signon.rememberSignons", False)  # отключает сохранение паролей
        options.set_preference("credentials_enable_service", False)
        browser = webdriver.Firefox(options=options)

    elif request.param == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,  # отключает службу учётных данных
            "profile.password_manager_enabled": False  # отключает менеджер паролей
        })
        browser = webdriver.Chrome(options=options)

    else:
        raise ValueError('Unknown browser type')

    yield browser
    browser.quit()

@pytest.fixture
def user_login():
    fake = Faker()
    email = fake.email()
    user_name = fake.user_name()

    response = requests.post(Constants.URL + Constants.UserCreateUrl,
                             data={"email": email,
                                   "password": 'password',
                                   "name": user_name})

    json_data = response.json()
    access_token = json_data.get("accessToken")

    return [email, 'password', access_token]

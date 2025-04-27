
import pytest
from selenium import webdriver

from constants import Constants
from faker import Faker
import requests

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
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

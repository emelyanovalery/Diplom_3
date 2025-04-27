import allure
import requests
from faker import Faker
from constants import Urls


class UserData:

    @staticmethod
    @allure.step('Сгенерировать данные для пользователя')
    def generate_fake_user_data():
        fake = Faker()
        user_body = {
            "email": fake.email(),
            "password": fake.passport_number(),
            "name": fake.user_name()
        }
        return user_body


class AuthResponses:
    @staticmethod
    @allure.step('Отправить запрос на создание пользователя')
    def create_user(user_body):
        user = requests.post(Urls.BASE_URL + Urls.AUTH_URL, user_body)
        return user

    @staticmethod
    @allure.step('Отправить запрос на удаление пользователя')
    def delete_user(user_response):
        access_token = user_response.json()["accessToken"]
        delete = requests.delete(Urls.BASE_URL + Urls.DELETE_USER_URL, headers={'Authorization': access_token})
        return delete

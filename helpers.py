import pytest
import allure
import requests
from pages.base_page import BasePage


class Helpers(BasePage):
    @allure.description('Создание заказа')
    def order_creation(self, access_token):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                                 headers={'Authorization': access_token},
                                 data={"ingredients": ["61c0c5a71d1f82001bdaaa6d"]})

        return response

    def get_order_id(self, access_token):
        response = self.order_creation(access_token)
        json_data = response.json()

        message = json_data['order']['number']
        return message
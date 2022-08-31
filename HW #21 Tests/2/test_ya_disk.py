import unittest
from parameterized import parameterized
import requests
import os


TOKEN = os.getenv('TOKEN')

fixture = [
    ('netology', 201),  # ОК
    ('netology', 409),  # По указанному пути уже существует папка с таким именем.'
    (':::::::', 400),  # Указанный формат ресурса Диска не корректен.'
    ('netology'+'x'*1000, 404),  # Не удалось найти запрошенный ресурс.
    ('netology/test/1/2/3', 409)  # Указанного пути не существует.
]


class TestYandex(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp ===> START TEST')
        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(TOKEN)
    }

    @parameterized.expand(fixture)
    def test_create_folder(self, catalog_path, result):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": catalog_path, "overwrite": "true"}
        response = requests.put(url, headers=self.headers, params=params).status_code
        self.assertEqual(response, result)

    def tearDown(self) -> None:
        print('tearDown ===> STOP TEST')

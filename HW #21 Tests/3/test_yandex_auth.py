import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class TestYandexAuth(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp ===> START TEST')

    def test_login(self):
        self.browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.browser.get('https://passport.yandex.ru/auth/')
        self.browser.find_element(
            By.XPATH, '//input[@data-t="field:input-login"]'
        ).send_keys('', LOGIN)
        self.browser.find_element(
            By.XPATH, '//button[@data-t="button:action:passp:sign-in"]'
        ).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@data-t="field:input-passwd"]')
            )
        )
        self.browser.find_element(
            By.XPATH, '//input[@data-t="field:input-passwd"]'
        ).send_keys('', PASSWORD)
        self.browser.find_element(
            By.XPATH, '//button[@data-t="button:action:passp:sign-in"]'
        ).click()
        url = self.browser.current_url
        self.assertEqual(url, 'https://passport.yandex.ru/auth/welcome')

    def tearDown(self) -> None:
        self.browser.close()
        print('tearDown ===> STOP TEST')

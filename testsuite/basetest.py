from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from testsuite.login.login import Login
from unittest import TestCase
from uuid import uuid4
import logging


class BaseTest(TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://hexa-a.xyz/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.login = Login(driver=self.driver)
        self.login.id('hamada')
        self.login.password('123456')
        self.login.submit()

    def tearDown(self):
        self.driver.close()

    def log(self, msg):
        logging.info(msg)

    def random_string(self):
        return str(uuid4())[:10]

from testsuite.basetest import BaseTest
from testsuite.login.login import Login
from testsuite.settings.settings import Settings


class SettingsTest(BaseTest):

    def test001_login(self):
        self.log('After logging in check the email is in its location')
        email = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/div[1]')
        self.assertEqual(email.text, 'hamada@gmail.com')

    def test002_change_passwd(self):
        self.log('Go to settings and change password')
        settings = Settings(driver=self.driver)
        settings.change_password('123456', '1234567')

        self.log('Logout and sign in again with the new password')
        self.login.logout()
        self.login.id('hamada')
        self.login.password('1234567')
        self.login.submit_after_logout()

        self.log('check that it logged in')
        email = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/div[1]')
        self.assertEqual(email.text, 'hamada@gmail.com')

        self.log('Retrieve the old password')
        settings.go_to_settings_page()
        settings.change_password('1234567', '123456')

    def test003_change_email(self):
        self.log('Go to settings and change email')
        new_email = 'hamada_725@gmail.com'
        settings = Settings(driver=self.driver)
        settings.change_email(new_email)

        self.log('Logout and sign in again with the new email')
        self.login.logout()
        self.login.id(new_email)
        self.login.password('123456')
        self.login.submit_after_logout()

        self.log('check that it logged in')
        email = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/div[1]')
        self.assertEqual(email.text, new_email)

        self.log('Retrieve the old email')
        settings.go_to_settings_page()
        settings.change_email('hamada@gmail.com')

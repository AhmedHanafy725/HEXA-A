class Settings:

    def __init__(self, driver):
        self.driver = driver
        self.go_to_settings_page()

    def go_to_settings_page(self):
        settings = self.driver.find_element_by_link_text('Settings')
        settings.click()

    def change_password(self, old_passwd, new_passwd):
        old_pass = self.driver.find_element_by_name('old_password')
        old_pass.send_keys(old_passwd)
        new_pass = self.driver.find_element_by_name('new_password')
        new_pass.send_keys(new_passwd)
        submit = self.driver.find_element_by_xpath('//*[@id="edit-user-password"]/button')
        submit.click()

    def change_email(self, new_email):
        email = self.driver.find_element_by_name('email')
        email.clear()
        email.send_keys(new_email)
        submit = self.driver.find_element_by_xpath('//*[@id="edit-user-email"]/div[2]/button')
        submit.click()

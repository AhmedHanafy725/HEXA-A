class Settings:

    def __init__(self, driver):
        self.driver = driver
        self.go_to_settings_page()

    def go_to_settings_page(self):
        settings = self.driver.find_element_by_link_text('Settings')
        settings.click()
        self.user_mail = self.driver.find_element_by_id('edit-user-email')
        self.user_password = self.driver.find_element_by_id('edit-user-password')

    def change_password(self, old_passwd, new_passwd):
        old_pass = self.user_password.find_element_by_name('old_password')
        old_pass.send_keys(old_passwd)
        new_pass = self.user_password.find_element_by_name('new_password')
        new_pass.send_keys(new_passwd)
        submit = self.user_password.find_element_by_tag_name('button')
        submit.click()

    def change_email(self, new_email):
        email = self.user_mail.find_element_by_name('email')
        email.clear()
        email.send_keys(new_email)
        submit = self.user_mail.find_element_by_tag_name('button')
        submit.click()

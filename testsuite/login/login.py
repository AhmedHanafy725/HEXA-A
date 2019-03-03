class Login:
    def __init__(self, driver):
        self.driver = driver

    def id(self, id):
        identifier = self.driver.find_element_by_name('identifier')
        identifier.send_keys(id)

    def password(self, password):
        passwd = self.driver.find_element_by_name('password')
        passwd.send_keys(password)

    def submit(self):
        submit = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/form/button')
        submit.click()

    def submit_after_logout(self):
        submit = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/form/button')
        submit.click()

    def logout(self):
        logout = self.driver.find_element_by_link_text('Logout')
        logout.click()

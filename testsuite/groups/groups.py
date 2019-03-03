class Groups:

    def __init__(self, driver):
        self.driver = driver
        self.go_to_groups_page()

    def go_to_groups_page(self):
        settings = self.driver.find_element_by_link_text('HEXA-A')
        settings.click()

    def create(self, group_name):
        create = self.driver.find_element_by_xpath('//*[@id="create-group-button"]')
        create.click()
        name = self.driver.find_element_by_name('name')
        name.send_keys(group_name)
        submit = self.driver.find_element_by_xpath('//*[@id="create-group-modal"]/div[3]/button[2]')
        submit.click()

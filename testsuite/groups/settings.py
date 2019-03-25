import time


class Settings:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        time.sleep(1)
        gsettings = self.driver.find_element_by_link_text('Settings')
        gsettings.click()

    def update_info(self, new_name=None, new_desc=None):
        self.go_to()
        if new_name:
            name = self.driver.find_element_by_name('name')
            name.clear()
            name.send_keys(new_name)
        if new_desc:
            desc = self.driver.find_element_by_name('description')
            desc.clear()
            desc.send_keys(new_desc)
        update = self.driver.find_element_by_class_name('green')
        update.click()

    def description_update(self, new_desc):
        self.go_to()
        desc = self.driver.find_element_by_name('description')
        desc.clear()
        desc.send_keys(new_desc)

    def remove(self):
        self.go_to()
        remove = self.driver.find_element_by_id('delete-group-button')
        remove.click()
        remove_button = self.driver.find_element_by_xpath('//*[@id="delete-group-modal"]/div[3]/button[2]')
        remove_button.click()

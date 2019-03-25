class Settings:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        window = self.driver.find_element_by_class_name('clearing')
        settings = window.find_element_by_link_text('Settings')
        settings.click()

    def update_info(self, new_name=None, new_deadline=None, new_desc=None):
        self.go_to()
        if new_name:
            name = self.driver.find_element_by_name('name')
            name.clear()
            name.send_keys(new_name)
        if new_deadline:
            dead = self.driver.find_element_by_name('deadline')
            dead.clear()
            dead.send_keys(new_deadline)
        if new_desc:
            desc = self.driver.find_element_by_name('description')
            desc.clear()
            desc.send_keys(new_desc)
        update = self.driver.find_element_by_id('edit-assignment-form')
        button = update.find_element_by_tag_name('button')
        button.click()

    def remove(self):
        self.go_to()
        delete_button = self.driver.find_element_by_id('delete-assignment-button')
        delete_button.click()
        transition = self.driver.find_element_by_class_name('transition')
        delete = transition.find_element_by_class_name('red')
        delete.click()

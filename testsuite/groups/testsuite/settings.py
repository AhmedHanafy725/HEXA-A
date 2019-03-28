class Settings:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        window = self.driver.find_element_by_class_name('clearing')
        settings = window.find_element_by_link_text('Settings')
        settings.click()

    def remove(self):
        self.go_to()
        delete_button = self.driver.find_element_by_id('delete-testsuite-button')
        delete_button.click()
        model = self.driver.find_element_by_id('delete-testsuite-modal')
        delete = model.find_element_by_class_name('red')
        delete.click()
        
    def update_info(self, new_name=None, new_level=None, new_attempts=None, new_attachment_path=None, new_public=None, new_suggest_enable=None):
        self.go_to()
        if new_name is not None:
            name = self.driver.find_element_by_name('name')
            name.send_keys(new_name)
        if new_level is not None:
            level = self.driver.find_element_by_name('level')
            level.send_keys(new_level)
        if new_attempts is not None:
            attempts = self.driver.find_element_by_name('attempts')
            attempts.send_keys(new_attempts)
        if new_public is not None:
            public = self.driver.find_element_by_name('public')
            public.send_keys(new_public)
        if new_suggest_enable is not None:
            suggest = self.driver.find_element_by_name('enable_suggestions')
            suggest.send_keys(new_suggest_enable)
        if new_attachment_path is not None:
            attachments = self.driver.find_element_by_name('attachments')
            attachments.send_keys(new_attachment_path)
        testsuite = self.driver.find_element_by_id('edit-testsuite-form')
        save = testsuite.find_element_by_tag_name('button')
        save.click()

    def remove_attachment(self, name):
        self.go_to()
        attachments_list = self.driver.find_element_by_class_name('list')
        items  = attachments_list.find_elements_by_class_name('item')
        for item in items:
            header = item.find_element_by_class_name('header')
            if header.text == name:
                remove_button = item.find_element_by_tag_name('button')
                remove_button.click()

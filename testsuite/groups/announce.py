import time

class Announcement:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        time.sleep(1)
        announcement = self.driver.find_element_by_link_text('Announcements')
        announcement.click()

    def add(self, text):
        self.go_to()
        add = self.driver.find_element_by_id('create-announcement-button')
        add.click()
        model = self.driver.find_element_by_id('create-announcement-modal')
        content = model.find_element_by_name('content')
        content.send_keys(text)
        submit = model.find_element_by_class_name('green')
        submit.click()

    def remove(self, announce_number=1):
        self.go_to()
        total_num = self.get_total_number()
        drops = self.driver.find_elements_by_class_name('dropdown')
        delete_drop = drops[total_num - announce_number]
        delete_drop.click()
        delete_button = delete_drop.find_element_by_name('removeAnnouncement')
        delete_button.click()

    def get_text(self, announce_number=1):
        self.go_to()
        total_num = self.get_total_number()
        announce = self.driver.find_elements_by_class_name('extra')
        return announce[total_num - announce_number].text
    
    def get_total_number(self):
        self.go_to()
        announce = self.driver.find_elements_by_class_name('extra')
        return len(announce)

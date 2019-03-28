import time
from testsuite.groups.settings import Settings
from testsuite.groups.announce import Announcement
from testsuite.groups.assignment.assignment import Assignment
from testsuite.groups.testsuite.testsuite import Testsuite

class Groups:

    def __init__(self, driver):
        self.driver = driver
        self.settings = Settings(self.driver)
        self.announcement = Announcement(self.driver)
        self.assignment = Assignment(self.driver)
        self.testsuite = Testsuite(self.driver)

    def go_to(self):
        time.sleep(1)
        groups = self.driver.find_element_by_link_text('HEXA-A')
        groups.click()
        self.group_list = self.driver.find_elements_by_class_name('card')

    def create(self, group_name, description=''):
        self.go_to()
        create = self.driver.find_element_by_id('create-group-button')
        create.click()
        model = self.driver.find_element_by_id('create-group-modal')
        name = model.find_element_by_name('name')
        name.send_keys(group_name)
        desc = model.find_element_by_name('description')
        desc.send_keys(description)
        submit = model.find_element_by_class_name('green')
        submit.click()

    def get_name(self, group_number=1):
        self.go_to()
        group_name = self.group_list[group_number - 1].find_element_by_class_name('header')
        return group_name.text

    def get_description(self, group_number=1):
        self.go_to()
        group_desc = self.group_list[group_number - 1].find_element_by_class_name('description')
        return group_desc.text

    def get_group(self, name):
        self.go_to()
        for group in self.group_list:
            group_name = group.find_element_by_class_name('header')
            if group_name.text == name:
                return group

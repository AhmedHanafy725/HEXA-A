import time
from testsuite.groups.settings import Settings
from testsuite.groups.announce import Announcement
from testsuite.groups.assignment.assignment import Assignment

class Groups:

    def __init__(self, driver):
        self.driver = driver
        self.settings = Settings(self.driver)
        self.announcement = Announcement(self.driver)
        self.assignment = Assignment(self.driver)

    def go_to(self):
        time.sleep(1)
        groups = self.driver.find_element_by_link_text('HEXA-A')
        groups.click()

    def create(self, group_name, description=''):
        self.go_to()
        create = self.driver.find_element_by_id('create-group-button')
        create.click()
        transition = self.driver.find_element_by_class_name('transition')
        name = transition.find_element_by_name('name')
        name.send_keys(group_name)
        desc = transition.find_element_by_name('description')
        desc.send_keys(description)
        submit = transition.find_element_by_class_name('green')
        submit.click()

    def get_name(self, group_number=1):
        self.go_to()
        groups = self.driver.find_elements_by_class_name('card')
        group_name = groups[group_number - 1].find_element_by_class_name('header')
        return group_name.text

    def get_description(self, group_number=1):
        self.go_to()
        groups = self.driver.find_elements_by_class_name('card')
        group_desc = groups[group_number - 1].find_element_by_class_name('description')
        return group_desc.text

    def get_group(self, name):
        self.go_to()
        groups = self.driver.find_elements_by_class_name('card')
        for group in groups:
            group_name = group.find_element_by_class_name('header')
            if group_name.text == name:
                return group

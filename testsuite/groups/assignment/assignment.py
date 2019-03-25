from testsuite.groups.assignment.details import Details
from testsuite.groups.assignment.submissions import Submissions
from testsuite.groups.assignment.settings import Settings
import time

class Assignment:
    def __init__(self, driver):
        self.driver = driver
        self.settings = Settings(self.driver)
        self.details  = Details(self.driver)
        self.submissions = Submissions(self.driver)

    def go_to(self, name=None):
        time.sleep(1)
        assignment = self.driver.find_element_by_link_text('Assignments')
        assignment.click()
        if name:
            assign = self.get_by_name(name)
            select = assign.find_element_by_tag_name('a')
            select.click()

    def add(self, name, date, description=''):
        self.go_to()
        assgin = self.driver.find_element_by_id('create-assignment-button')
        assgin.click()
        assign_model = self.driver.find_element_by_id('create-assignment-modal')
        assign_name = assign_model.find_element_by_name('name')
        assign_name.send_keys(name)
        deadline = assign_model.find_element_by_name('deadline')
        deadline.send_keys(date)
        desc = assign_model.find_element_by_name('description')
        desc.send_keys(description)
        submit = assign_model.find_element_by_class_name('green')
        submit.click()

    def remove(self, name):
        self.go_to(name)
        self.settings.remove()

    def get_by_name(self, name):
        self.go_to()
        assignments = self.driver.find_element_by_class_name('items')
        items = assignments.find_elements_by_class_name('item')
        for item in items:
            if name in item.text:
                return item

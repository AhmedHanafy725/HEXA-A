import time
from selenium.webdriver.support.ui import Select
from testsuite.groups.testsuite.settings import Settings
from testsuite.groups.testsuite.testcases import Testcases
class Testsuite:

    def __init__(self, driver):
        self.driver = driver 
        self.settings = Settings(self.driver)
        self.testcases = Testcases(self.driver)
    
    def go_to(self):
        time.sleep(1)
        testsuite = self.driver.find_element_by_link_text('Testsuites')
        testsuite.click()

    def add(self, name, level='Basic', attempts=0, file_path=None, attachment_path=None, public=False, suggest_enable=False):
        self.go_to()
        testsuite = self.driver.find_element_by_id('create-testsuite-button')
        testsuite.click()
        model = self.driver.find_element_by_id('create-testsuite-modal')
        testsuite_name = model.find_element_by_name('name')
        testsuite_name.send_keys(name)
        testsuite_level = Select(model.find_element_by_name('level'))
        testsuite_level.select_by_visible_text(level)
        testsuite_attempts = model.find_element_by_name('attempts')
        testsuite_attempts.clear()
        testsuite_attempts.send_keys(attempts)
        if file_path:
            testsuite_file = model.find_element_by_name('file') 
            testsuite_file.send_keys(file_path)
        if attachment_path:
            testsuite_attachment = model.find_element_by_name('attachments') 
            testsuite_attachment.send_keys(attachment_path)
        if public:
            testsuite_public = model.find_element_by_name('public')
            testsuite_public.click()
        if suggest_enable:
            testsuite_suggest = model.find_element_by_name('enable_suggestions')
            testsuite_suggest.click()
        create = model.find_element_by_class_name('green')
        create.click()
        
    def get(self, name):
        self.go_to()
        testsuite_list = self.driver.find_element_by_class_name('divided')
        items = testsuite_list.find_elements_by_class_name('item')
        for item in items:
            testsuite_name = item.find_element_by_tag_name('h4')
            if testsuite_name.text == name:
                return item
        else:
            return None
    
    def select(self, name):
        self.go_to()
        testsuite = self.get(name)
        select = testsuite.find_element_by_tag_name('a')
        select.click()

    def get_level(self, name):
        self.go_to()
        testsuite = self.get(name)
        if testsuite:
            level = testsuite.find_elements_by_class_name('floated')[1]
            return level.text
        else:
            return None

    def get_state(self, name):
        # private or public
        self.go_to()
        testsuite = self.get(name)
        if testsuite:
            state = testsuite.find_elements_by_class_name('floated')[0]
            return state.text
        else:
            return None

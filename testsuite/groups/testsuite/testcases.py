class Testcases:
    
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        window = self.driver.find_element_by_class_name('clearing')
        testcases = window.find_element_by_link_text('Testcases')
        testcases.click()

    def add_testcase(self, stdin, stdout):
        self.go_to()
        testcase_button = self.driver.find_element_by_id('add-testcase-button')
        testcase_button.click()
        model = self.driver.find_element_by_class_name('add-testcase-modal')
        testcase_stdin = model.find_element_by_name('stdin')
        testcase_stdin.send_keys(stdin)
        testcase_stdout = model.find_element_by_name('expected_stdout')
        testcase_stdout.send_keys(stdout)
        add_button = model.find_element_by_class_name('green')
        add_button.click()
    
    def remove_testcase(self, testcase_number):
        self.go_to()
        testcases_list = self.driver.find_element_by_class_name('divided')
        items = testcases_list.find_elements_by_class_name('item')
        if testcase_number <= len(items):
            item = items[testcase_number - 1]
            delete = item.find_element_by_name('deleteTestcase')
            delete.click()
            return True
        else:
            return False

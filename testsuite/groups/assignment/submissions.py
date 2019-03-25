class Submissions:
    
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        window = self.driver.find_element_by_class_name('clearing')
        submissions = window.find_element_by_link_text('Submissions')
        submissions.click()

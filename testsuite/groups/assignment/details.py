class Details:
    
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        window = self.driver.find_element_by_class_name('clearing')
        details = window.find_element_by_link_text('Details')
        details.click()

    def get_description(self):
        self.go_to()
        desc = self.driver.find_element_by_class_name('markdown-body')
        text = desc.text
        return text

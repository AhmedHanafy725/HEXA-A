from testsuite.basetest import BaseTest
from testsuite.login.login import Login
from testsuite.groups.groups import Groups


class GroupsTest(BaseTest):
    
    def setUp(self):
        super().setUp()
        self.log('Create group')
        self.group_name = self.random_string()
        self.groups = Groups(self.driver)
        self.groups.create(self.group_name)
    
    def tearDown(self):
        self.log('Remove created group')
        group = self.groups.get_group(name=self.group_name)
        group.click()
        self.groups.settings.remove()
        super().tearDown()

    def test001_create_group(self):
        self.log('Check that group has been created')
        group = self.groups.get_group(name=self.group_name)
        self.assertTrue(group)

    def test002_update_group_info(self):
        self.log('Change group name and description')
        new_name = self.random_string()
        new_desc = self.random_string()
        self.groups.settings.update_info(new_name=new_name, new_desc=new_desc)

        self.log('Check that group info has been updated')
        group = self.groups.get_group(new_name)
        name = group.find_element_by_class_name('header')
        desc = group.find_element_by_class_name('description')
        self.assertEquals(name.text, new_name)
        self.assertEquals(desc.text, new_desc)

        self.log('Update group name to be removed')
        self.group_name = new_name

    def test003_add_announcement(self):        
        self.log('Add announcement')
        announce_text = self.random_string()
        self.groups.announcement.add(announce_text)

        self.log('Check that content of the announcement is same as created')
        text = self.groups.announcement.get_text()
        self.assertEquals(text, announce_text)

        self.log('Remove announcement')
        self.groups.announcement.remove()
    
    def test004_add_more_announcement(self):
        self.log('Add first announcement')
        announce_text_1 = self.random_string()
        self.groups.announcement.add(announce_text_1)

        self.log('Add second announcement')
        announce_text_2 = self.random_string()
        self.groups.announcement.add(announce_text_2)

        self.log('Check that content of the announcement is same as created')
        text = self.groups.announcement.get_text(announce_number=1)
        self.assertEquals(text, announce_text_1)
        text = self.groups.announcement.get_text(announce_number=2)
        self.assertEquals(text, announce_text_2)

        self.log('Remove announcement')
        self.groups.announcement.remove(announce_number=1)
        self.groups.announcement.remove(announce_number=2)

    def test005_add_assignment(self):
        self.log('Create assginment')
        assign_name = self.random_string()
        date = '3/25/201900 11:59PM'
        self.groups.assignment.add(assign_name, date)

        self.log('Check that assignment has been created')
        assignment = self.groups.assignment.get_by_name(assign_name)
        self.assertTrue(assignment)

        self.log('Remove the assignment that has been created')
        self.groups.assignment.remove(assign_name)

    def test006_add_more_assignment(self):
        self.log('Create assginment')
        assign_name_1 = self.random_string()
        date_1 = '3/25/201900 11:59PM'
        self.groups.assignment.add(assign_name_1, date_1)

        self.log('Create another assginment')
        assign_name_2 = self.random_string()
        date_2 = '3/25/201900 11:59PM'
        self.groups.assignment.add(assign_name_2, date_2)

        self.log('Check that assignments has been created')
        assignment = self.groups.assignment.get_by_name(assign_name_1)
        self.assertTrue(assignment)
        assignment = self.groups.assignment.get_by_name(assign_name_2)
        self.assertTrue(assignment)

        self.log('Remove the assignments that has been created')
        self.groups.assignment.remove(assign_name_1)
        self.groups.assignment.remove(assign_name_2)

    def test007_update_assignment_info(self):
        self.log('Create assignment')
        assign_name_2 = self.random_string()
        date_2 = '3/25/201900 11:59PM'
        self.groups.assignment.add(name=assign_name_2, date=date_2)

        self.log('Update assignment info')
        new_name = self.random_string()
        new_desc = self.random_string()
        self.groups.assignment.settings.update_info(new_name=new_name, new_desc=new_desc)

        self.log('Check that info has been updated')
        assignment = self.groups.assignment.get_by_name(name=new_name)
        self.assertTrue(assignment)
        self.groups.assignment.go_to(name=new_name)
        desc = self.groups.assignment.details.get_description()
        self.assertAlmostEquals(desc, new_desc)

        self.log('remove assignment')
        self.groups.assignment.remove(new_name)

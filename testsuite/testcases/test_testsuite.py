
from testsuite.basetest import BaseTest
from testsuite.groups.groups import Groups
import unittest
from parameterized import parameterized

class TestsuiteTest(BaseTest):
    
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

    def test001_add_testsuite(self):
        self.log('Create testsuite')
        testsuite_name = self.random_string()
        self.groups.testsuite.add(name=testsuite_name)

        self.log('Check that testsuite has been created')
        testsuite = self.groups.testsuite.get(name=testsuite_name)
        self.assertTrue(testsuite)

        self.log('Remove testsuite')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.remove()

    @unittest.skip('https://github.com/ahmedelsayed-93/hexa-a/issues/10')
    def test002_update_testsuite_name(self):
        self.log('Create testsuite')
        testsuite_name = self.random_string()
        self.groups.testsuite.add(name=testsuite_name)

        self.log('Update testsuite name')
        name = self.random_string()
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.update_info(new_name=name)

        self.log('Check that name has been updated')
        testsuite = self.groups.testsuite.get(name=name)
        self.assertTrue(testsuite)

        self.log('Remove testsuite')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.remove()

    @parameterized.expand(['Basic', 'Extended', 'Advanced'])
    @unittest.skip('https://github.com/ahmedelsayed-93/hexa-a/issues/10')
    def test003_update_testsuite_level(self, level):
        self.log('Create testsuite')
        testsuite_name = self.random_string()
        self.groups.testsuite.add(name=testsuite_name)

        self.log('Update testsuite level')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.update_info(new_level=level)

        self.log('Check that name has been updated')
        testsuite_level = self.groups.testsuite.get_level(name=testsuite_name)
        self.assertEqual(testsuite_level, level)

        self.log('Remove testsuite')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.remove()
    
    @unittest.skip('https://github.com/ahmedelsayed-93/hexa-a/issues/10')
    def test004_update_testsuite_state(self):
        self.log('Create testsuite')
        testsuite_name = self.random_string()
        self.groups.testsuite.add(name=testsuite_name)

        self.log('Update testsuite state')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.update_info(new_public=True)

        self.log('Check that name has been updated')
        testsuite_state = self.groups.testsuite.get_state(name=testsuite_name)
        self.assertEqual(testsuite_state, 'Public')

        self.log('Remove testsuite')
        self.groups.testsuite.select(name=testsuite_name)
        self.groups.testsuite.settings.remove()

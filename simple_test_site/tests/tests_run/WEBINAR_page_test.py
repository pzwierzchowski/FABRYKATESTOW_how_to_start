import unittest
from selenium import webdriver

from simple_test_site.config.test_settings import TestSettings
from simple_test_site.tests.page_objects import main_page, users_page, inputs_page, hovers_page, dropdown_page,\
    checkboxes_page, add_remove_page, date_picker_page, basic_auth_page, form_page, key_presses_page,\
    drag_and_drop_page, status_codes_page, iframe_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_xxx(self):
        print(1)


if __name__ == '__main__':
    unittest.main()
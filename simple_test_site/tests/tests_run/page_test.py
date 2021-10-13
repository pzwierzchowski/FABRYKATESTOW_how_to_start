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

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_datepicker_visibility(self):
        date_picker_page.click_datepicker_tab(self.driver)
        self.assertTrue(date_picker_page.datepicker_content_visible(self.driver))

    def test11_datepicker_correct_input(self):
        date_picker_page.click_datepicker_tab(self.driver)
        self.assertTrue(date_picker_page.datepicker_send_correct_keys(self.driver))

    def test12_inputs_incorrect_input(self):
        date_picker_page.click_datepicker_tab(self.driver)
        self.assertTrue(date_picker_page.datepicker_send_incorrect_keys(self.driver))

    def test13_inputs_outofscope_input(self):
        date_picker_page.click_datepicker_tab(self.driver)
        self.assertTrue(date_picker_page.datepicker_send_outofscope_keys(self.driver))

    def test14_auth_visibility(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.auth_content_visible(self.driver))

    def test15_auth_correct_credentials(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_correct_credentials(self.driver))

    def test16_auth_incorrect_credentials(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_incorrect_credentials(self.driver))

    def test17_auth_empty_credentials(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_empty_credentials(self.driver))

    def test18_form_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    def test19_form_correct_name(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.send_correct_name(self.driver))

    def test20_form_empty_name(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.send_empty_name(self.driver))

    def test21_keypress_visibility(self):
        key_presses_page.click_keypress_tab(self.driver)
        self.assertTrue(key_presses_page.keypress_content_visible(self.driver))

    def test22_keypress_send_keys(self):
        key_presses_page.click_keypress_tab(self.driver)
        self.assertTrue(key_presses_page.send_enter_to_input(self.driver) and (key_presses_page.send_escape_to_input(self.driver)))

    def test23_drag_and_drop_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))

    def test24_drag_and_drop_changed(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.check_drag_and_drop(self.driver))

    def test25_status_codes_visibility(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.codes_content_visible(self.driver))

    def test26_status_code_200(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.code_200(self.driver))

    def test27_status_code_305(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.code_305(self.driver))

    def test28_status_code_404(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.code_404(self.driver))

    def test29_status_code_500(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.code_500(self.driver))

    def test30_iframe_visibility(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test31_iframe_click_first_button(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe(self.driver))

    def test32_iframe_click_second_button(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe(self.driver))


if __name__ == '__main__':
    unittest.main()

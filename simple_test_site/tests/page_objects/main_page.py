from simple_test_site.tests.helpers.support_functions import *


main_page_header = 'test-header'
main_page_content = 'test-content'

def content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, main_page_content)
    return elem.is_displayed()

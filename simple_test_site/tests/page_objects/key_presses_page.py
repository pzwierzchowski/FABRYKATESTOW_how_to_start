from simple_test_site.tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys


keypress_tab = 'keypresses-header'
keypress_content = 'keypresses-content'
keypress_input = 'target'
keypress_result = 'keyPressResult'


def click_keypress_tab(driver_instance):
    elem = driver_instance.find_element_by_id(keypress_tab)
    elem.click()


def keypress_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, keypress_content)
    return elem.is_displayed()


def send_enter_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, keypress_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(keypress_input)
    elem.send_keys(Keys.ENTER)
    output = driver_instance.find_element_by_id(keypress_result).text
    if output == 'You entered: ENTER':
        return True
    else:
        return False


def send_escape_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, keypress_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(keypress_input)
    elem.send_keys(Keys.ESCAPE)
    output = driver_instance.find_element_by_id(keypress_result).text
    if output == 'You entered: ESCAPE':
        return True
    else:
        return False
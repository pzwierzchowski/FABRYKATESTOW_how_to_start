from simple_test_site.tests.helpers.support_functions import *

input_tab = 'inputs-header'
input_content = 'inputs-content'
input_field = '//*[@id="inputs-content"]/div/input'


def click_input_tab(driver_instance):
    elem = driver_instance.find_element_by_id(input_tab)
    elem.click()


def input_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, input_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_field, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('123456')
    value = 123456
    if value == int(elem.get_attribute("value")):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_field, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True


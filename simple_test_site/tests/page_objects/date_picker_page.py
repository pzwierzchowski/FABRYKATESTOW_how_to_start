from simple_test_site.tests.helpers.support_functions import *


datepicker_header = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_input = 'start'


def click_datepicker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(datepicker_header)
    elem.click()


def datepicker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, datepicker_content)
    return elem.is_displayed()


def datepicker_send_correct_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_input)
    elem.send_keys('2010')
    value = '2020-10-20'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def datepicker_send_incorrect_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_input)
    elem.send_keys('abcde')
    value = 'abcde'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True


def datepicker_send_outofscope_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_input)
    elem.send_keys('20102021')
    value = '2021-10-20'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True
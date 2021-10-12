from simple_test_site.tests.helpers.support_functions import *


form_tab = 'form-header'
form_content = 'form-content'
first_name_input = 'fname'
last_name_input = 'lname'
submit_btn = 'formSubmitButton'
focus = 'focus-visible'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()


def send_correct_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(first_name_input)
    elem.send_keys('Katarzyna')
    wait_for_visibility_of_element(driver_instance, last_name_input, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(last_name_input)
    elem1.send_keys('Java')
    wait_for_visibility_of_element(driver_instance, submit_btn, time_to_wait=1)
    btn = driver_instance.find_element_by_id(submit_btn)
    btn.click()
    try:
        alert = driver_instance.switch_to.alert
        alert.accept()
        return True
    except NoAlertPresentException:
        return False


def send_empty_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(first_name_input)
    elem.send_keys('')
    wait_for_visibility_of_element(driver_instance, last_name_input, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(last_name_input)
    elem1.send_keys('Java')
    wait_for_visibility_of_element(driver_instance, submit_btn, time_to_wait=1)
    btn = driver_instance.find_element_by_id(submit_btn)
    btn.click()
    try:
        alert = driver_instance.switch_to.alert
        alert.accept()
        return True
    except NoAlertPresentException:
        return False
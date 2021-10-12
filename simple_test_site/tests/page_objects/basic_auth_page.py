from simple_test_site.tests.helpers.support_functions import *

auth_header = 'basicauth-header'
auth_content = 'basicauth-content'
username_input = 'ba_username'
password_input = 'ba_password'
login_btn = '//*[@id="content"]/button'
message = 'loggedInMessage'
invalid_message = 'loginFormMessage'


def click_auth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(auth_header)
    elem.click()


def auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, auth_content)
    return elem.is_displayed()


def send_correct_credentials(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(username_input)
    elem.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, password_input, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(password_input)
    elem1.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, login_btn, time_to_wait=1)
    btn = driver_instance.find_element_by_xpath(login_btn)
    btn.click()
    login_message = wait_for_visibility_of_element(driver_instance, message)
    return login_message.is_displayed()


def send_incorrect_credentials(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(username_input)
    elem.send_keys('admin3')
    wait_for_visibility_of_element(driver_instance, password_input, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(password_input)
    elem1.send_keys('admin3')
    wait_for_visibility_of_element(driver_instance, login_btn, time_to_wait=1)
    btn = driver_instance.find_element_by_xpath(login_btn)
    btn.click()
    error = driver_instance.find_element_by_id(invalid_message).text
    if error == 'Invalid credentials':
        return True
    else:
        return False


def send_empty_credentials(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    elem = driver_instance.find_element_by_id(username_input)
    elem.send_keys('')
    wait_for_visibility_of_element(driver_instance, password_input, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(password_input)
    elem1.send_keys('')
    wait_for_visibility_of_element(driver_instance, login_btn, time_to_wait=1)
    btn = driver_instance.find_element_by_xpath(login_btn)
    btn.click()
    error = driver_instance.find_element_by_id(invalid_message).text
    if error == 'Invalid credentials':
        return True
    else:
        return False
from simple_test_site.tests.helpers.support_functions import *
from requests import api


codes_tab = 'statuscodes-header'
codes_content = 'statuscodes-content'
code200id = '200siteAnchor'
code305id = '305siteAnchor'
code404id = '404siteAnchor'
code500id = '500siteAnchor'


def click_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(codes_tab)
    elem.click()


def codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, codes_content)
    return elem.is_displayed()


def code_200(driver_instance):
    wait_for_visibility_of_element(driver_instance, code200id)
    code200 = driver_instance.find_element_by_id(code200id)
    link200 = code200.get_attribute('href')
    r = api.get(link200)
    if r.status_code == 200:
        return True
    else:
        return False


def code_305(driver_instance):
    wait_for_visibility_of_element(driver_instance, code305id)
    code305 = driver_instance.find_element_by_id(code305id)
    link305 = code305.get_attribute('href')
    r = api.get(link305)
    if r.status_code == 305:
        return True
    else:
        return False


def code_404(driver_instance):
    wait_for_visibility_of_element(driver_instance, code404id)
    code404 = driver_instance.find_element_by_id(code404id)
    link404 = code404.get_attribute('href')
    r = api.get(link404)
    if r.status_code == 404:
        return True
    else:
        return False


def code_500(driver_instance):
    wait_for_visibility_of_element(driver_instance, code500id)
    code500 = driver_instance.find_element_by_id(code500id)
    link500 = code500.get_attribute('href')
    r = api.get(link500)
    if r.status_code == 500:
        return True
    else:
        return False

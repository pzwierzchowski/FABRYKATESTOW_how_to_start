from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_inv(inv_driver_instance, xpath, time_to_wait=10):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem
from selenium.webdriver.common.action_chains import ActionChains


def scrolling_to_element(driver_instance, xpath):
    target = driver_instance.find_element_by_xpath(xpath)
    actions = ActionChains(driver_instance)
    actions.move_to_element(target)
    actions.perform()


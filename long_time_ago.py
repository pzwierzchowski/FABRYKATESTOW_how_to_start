from selenium import webdriver
from time import sleep
datepick = 'datepicker-header'

driver = webdriver.Chrome()
# test1
driver.get('http://simpletestsite.fabrykatestow.pl/')
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/h1')
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
driver.find_element_by_id(datepick).click()
driver.find_element_by_id('inputs-header').click()
driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/input').send_keys('123')
sleep(3)
# test2

driver.find_element_by_xpath('/html/body/div[1]/h1')
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
driver.find_element_by_id('datepicker-header').click()
driver.find_element_by_id('inputs-header').click()
driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/input').send_keys('123')
sleep(3)
# test3

driver.find_element_by_xpath('/html/body/div[1]/h1')
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
driver.find_element_by_id('datepicker-header').click()
driver.find_element_by_id('inputs-header').click()
driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/input').send_keys('123')
sleep(3)
# test4

driver.find_element_by_xpath('/html/body/div[1]/h1')
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
driver.find_element_by_id('datepicker-header').click()
driver.find_element_by_id('inputs-header').click()
driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/input').send_keys('123')
sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/h1')
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
driver.find_element_by_id('datepicker-header').click()
driver.find_element_by_id('inputs-header').click()
driver.find_element_by_xpath('/html/body/div[2]/div[10]/div/input').send_keys('123')

driver.close()

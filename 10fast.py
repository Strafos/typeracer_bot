from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(3)
for i in range(1,700):
    xpath = '//*[@id="row1"]/span[%s]' %(i)
    elem = driver.find_element_by_xpath(xpath)
    actions = ActionChains(driver)
    actions.send_keys(elem.text + ' ')
    actions.perform()

time.sleep(1000)
driver.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

def find(driver):
    elems = driver.find_elements_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span')
    if elems:
        return elems
    else:
        return False


driver = webdriver.Chrome()

driver.get('http://play.typeracer.com/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a').click()
time.sleep(1)
elem = driver.find_element_by_class_name('lightLabel')
while 'final' not in elem.text:
    elem = driver.find_element_by_class_name('lightLabel')
print 'COUNTDOWN'
time.sleep(5)
print 'time to start'
time.sleep(3)

# elems = driver.find_elements_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span')
# print elem.get_attribute('text')
elems = WebDriverWait(driver, 1).until(find)
actions = ActionChains(driver)
for elem in elems:
    print elem.text
    if len(elem.text) > 10:
        actions.send_keys(' ')
    actions.send_keys(elem.text)
actions.perform()

time.sleep(10)
driver.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import nltk

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

# elems = driver.find_elements_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span')
# print elem.get_attribute('text')
elems = WebDriverWait(driver, 1).until(find)
text = ''
for elem in elems:
    if len(elem.text) > 10:
        text += ' '
    text += elem.text
print text

# driver.find_element_by_xpath('//*[@id="tstats-edit"]/table/tbody/tr/td[1]/a').click()
# login = ActionChains(driver)
# login.send_keys('\' + Keys.ENTER)
# login.perform()

### ActionChains approach
# actions = ActionChains(driver)
# for elem in elems:
#     print elem.text
#     if len(elem.text) > 10:
#         actions.send_keys(' ')
#     actions.send_keys(elem.text)
# actions.perform()

text_input = driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
while text.find(' ') != -1:
    idx = text.index(' ')
    text_input.send_keys(text[:idx] + ' ')
    text = text[idx+1:]
    time.sleep(.4)
text_input.send_keys(text)
    
PUNCTUATION = [',', ':', '.', '(', ')', '!', '"', "'"]
# for token in tokens:
#     if token in PUNCTUATION:
#         text_input.send_keys(Keys.BACKSPACE)
#     text_input.send_keys(token + ' ')
#     time.sleep(.2)

time.sleep(1000)
driver.quit()
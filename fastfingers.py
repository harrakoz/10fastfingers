from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver")
driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()
words = driver.execute_script('return word_string')
search = driver.find_element_by_class_name("form-control")
splitted = words.split("|")
search.click()

for words in splitted:
	search.send_keys(words)
	search.send_keys(Keys.SPACE)
	time.sleep(0.1)
	

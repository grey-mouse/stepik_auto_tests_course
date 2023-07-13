from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import math, pyperclip

def calc(x):
	return math.log(abs(12*math.sin(int(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
	browser.get(link)
	price = WebDriverWait(browser, 12).until(ES.text_to_be_present_in_element((By.ID, "price"), "100"))
	book_button = browser.find_element(By.ID, "book")
	book_button.click()
	
	# pass robo-captcha and copy code
	x = browser.find_element(By.ID, "input_value").text
	y = calc(x)
	browser.find_element(By.ID, "answer").send_keys(y)
	browser.find_element(By.ID, "solve").click()
	code = browser.switch_to.alert.text.split(" ")[-1]
	pyperclip.copy(code)
	
finally:
    browser.quit()

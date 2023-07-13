from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    text_input_field = browser.find_element(By.ID, "answer")
    text_input_field.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

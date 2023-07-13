from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    text_input_field = browser.find_element(By.ID, "answer")
    text_input_field.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    robots_radiobutton = browser.find_element(By.ID, "robotsRule")
    robots_radiobutton.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

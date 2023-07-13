from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    # find x and calculate function
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    # scroll down and insert values
    text_field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()

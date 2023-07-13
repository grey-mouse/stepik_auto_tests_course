from selenium import webdriver
from selenium.webdriver.common.by import By
import math, pyperclip

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
    code = browser.switch_to.alert.text.split(" ")[-1]
    pyperclip.copy(code)
finally:
    browser.quit()

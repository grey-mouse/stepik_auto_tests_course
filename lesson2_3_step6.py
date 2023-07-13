from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip, math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # click button
    flying_button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    flying_button.click()
    
    # switch to a new tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # pass through robo-captcha
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

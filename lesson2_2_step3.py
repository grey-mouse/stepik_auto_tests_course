from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # find sum of two numbers
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum = int(num1) + int(num2)
    
    # select sum value from the list
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))
    
    # click Submit button
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(20)
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("Dumba")
    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("Jumba")
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("Dumba.Jumba@tumba.bum")
    file_upload_field = browser.find_element(By.ID, "file")
    file_upload_field.send_keys(file_path)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(20)
    browser.quit()

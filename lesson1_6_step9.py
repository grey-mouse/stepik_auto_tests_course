from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = "Harry"
    last_name = "Potter"
    email = "harry.potter@hogwarts.scot"

    first_name_field = browser.find_element(By.CSS_SELECTOR, ".first:required")
    first_name_field.send_keys(first_name)
    last_name_field = browser.find_element(By.CSS_SELECTOR, ".second:required")
    last_name_field.send_keys(last_name)
    email_field = browser.find_element(By.CSS_SELECTOR, ".third:required")
    email_field.send_keys(email)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

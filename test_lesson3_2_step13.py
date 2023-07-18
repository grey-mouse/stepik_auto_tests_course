from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

first_name = "Harry"
last_name = "Potter"
email = "harry.potter@hogwarts.scot"

class TestRegistration(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
	
	def fill_form(self, link):
		browser = self.driver
		browser.get(link)
		
		browser.find_element(By.CSS_SELECTOR, ".first:required").send_keys(first_name)
		browser.find_element(By.CSS_SELECTOR, ".second:required").send_keys(last_name)
		browser.find_element(By.CSS_SELECTOR, ".third:required").send_keys(email)
		
		browser.find_element(By.CSS_SELECTOR, "button.btn").click()
		
		welcome_text = browser.find_element(By.TAG_NAME, "h1").text
		return welcome_text
		
	def test_registration1(self):
		link = "http://suninjuly.github.io/registration1.html"
		registration_result = self.fill_form(link)

		self.assertEqual(registration_result, "Congratulations! You have successfully registered!", "Should be successfully registered")
    	
	def test_registration2(self):
		link = "http://suninjuly.github.io/registration2.html"
		registration_result = self.fill_form(link)

		self.assertEqual(registration_result, "Congratulations! You have successfully registered!", "Should be successfully registered")
    	
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

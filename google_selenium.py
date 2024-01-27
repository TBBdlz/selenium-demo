from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setup WebDriver using Firefox
driver = webdriver.Firefox()

# Open Google and perform a search
driver.get("http://www.google.com")
# ... name="q" is the search box
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("KFC Fry Chicken")
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for results to load
try:
	title_elements = driver.find_elements(By.XPATH, '//h3')
except Exception as e:
	print(e)
	title_elements = []
	
for title in title_elements:
	print(f"Title: {title.text}")

driver.quit()

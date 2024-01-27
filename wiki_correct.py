from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Replace with the URL of the webpage containing the search input
url = 'https://www.wikipedia.org/'
driver.get(url)

# Locate the element using the CSS selector
search_input = driver.find_element(By.CSS_SELECTOR, '#searchInput')

# Enter text into the input form
search_input.send_keys('python programming language')
search_input.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()

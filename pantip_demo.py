from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://pantip.com/")

# Wait for the page to load (adjust time as needed)
time.sleep(2)

# Locate the search button and click it
search_button = driver.find_element(By.XPATH, '//*[@id="search-box"]')
search_button.click()

search_button.send_keys('เที่ยวภูเก็ต')
search_button.send_keys(Keys.RETURN)

# Wait for search input to appear (adjust time as needed)
time.sleep(2)

# Close the browser when done (optional)
driver.quit()

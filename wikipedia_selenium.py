from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setup WebDriver using Chrome
driver = webdriver.Chrome()

# Open Wikipedia and search for an article
driver.get("https://www.wikipedia.org/")
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python (programming language)")
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for page to loadfile.write(html.encode('utf-8'))
# get html page

html = driver.page_source
# Write HTML content to file
with open("python_wiki.html", "w", encoding='utf-8') as file:
    file.write(html)
    print(f"Page saved to {file.name}")

driver.quit()

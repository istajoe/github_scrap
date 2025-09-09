from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()   # Selenium Manager handles ChromeDriver automatically
driver.get("https://github.com/istajoe")
time.sleep(1)
resources = driver.find_elements(By.CLASS_NAME, "repo")
time.sleep(1)

for i in resources:
    print(i.text)

driver.quit()
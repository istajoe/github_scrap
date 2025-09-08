
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Start Chrome with explicit Service
service = Service()
driver = webdriver.Chrome(service=service)

# Print driver path
print("Driver Path:", service.path)

# Print driver version (what you already saw)
print("Driver Version:", driver.capabilities["chrome"]["chromedriverVersion"])

driver.quit()

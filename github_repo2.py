from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://github.com/istajoe")
repo ="https://github.com/istajoe"
resources = driver.find_elements(By.CLASS_NAME, "repo")

links = []
flink =[]

for i in resources:
    links.append(i.text)
#print(i.text)

## this will loop through all our repo link and give us a new url
for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
print(flink)

driver.quit()
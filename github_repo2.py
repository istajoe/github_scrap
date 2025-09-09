from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver (using Selenium Manager or webdriver_manager)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your GitHub profile
driver.get("https://github.com/istajoe")

# Find repo links (they are <a> with itemprop="name codeRepository")

repos = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/istajoe/")]'))
)

links = []
flink = []

def loop(next_page):
    global a
    driver.get(next_page)
    repos2 = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    for a in repos2:
        pass
    if "py" in a.text:
        print("it worked py is in the text")

for repo in repos:
    repo_name = repo.text.strip()
    repo_link = repo.get_attribute("href")
    links.append((repo_name, repo_link))

# Print results
for name, link in links:
    next_page = f"{name} -> {link}"
    flink.append(next_page)
    loop(next_page)


driver.quit()

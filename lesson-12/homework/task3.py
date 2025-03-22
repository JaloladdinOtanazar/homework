import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com")
time.sleep(3)
# Reach to laptop and click
search_input = driver.find_element(By.LINK_TEXT, "Laptops")
search_input.click()
time.sleep(3)

# Function to extract laptop data from a page

def scrape_laptops():
    laptops = []
    items = driver.find_elements(By.CLASS_NAME, 'card-block')
    for item in items:
        name = item.find_element(By.CLASS_NAME, 'card-title').text
        price = item.find_element(By.CSS_SELECTOR, 'h5').text
        description = item.find_element(By.CLASS_NAME, 'card-text').text

        laptops.append({
            'name': name,
            'price': price,
            'description': description
        })
    return laptops
# Scraping data from multiple pages

all_laptops = []
while True:
    all_laptops.extend(scrape_laptops())
    try:
        # Reach to the Next Page and click
        next = driver.find_element(By.ID, 'next2')
        if "disabled" in next.get_attribute("class"):
            break 
        next.click()
        time.sleep(3)
    except:
        break
with open('laptops.json', 'w') as f:
    json.dump(all_laptops, f, indent=4)

driver.quit()
print("Scraping complete. Data saved to laptops.json.")




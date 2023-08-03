import requests
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Navigate to the website
driver.get("https://www.jlpt.jp/tw/samples/sampleindex.html")

samples = ["sample01", "sample02"]
years = ["2012", "2018"]
for i in range(0, 2):

    sample_div = driver.find_element(By.ID, samples[i])
    sample_links = sample_div.find_elements(By.TAG_NAME, "a")

    for link in sample_links:
        href = str(link.get_attribute("href"))
        if "pdf" in href or "mp3" in href:

            filename = re.search(r"/([^/]+)$", href).group(1)
            print(href + ", " + filename)

            response = requests.get(href)
            with open(filename, "wb") as f:
                f.write(response.content)
            os.rename(filename, "JLPT-Workbook-" + years[i] + "_" + filename)
            print("Downloaded", "JLPT-Workbook-" + years[i] + "_" + filename)



# Close the browser window
driver.quit()
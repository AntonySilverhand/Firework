from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os
import time

# Set up Edge options
edge_options = Options()
edge_options.add_argument('--start-maximized')  # Start browser maximized

# Get the absolute path of the HTML file
html_file_path = os.path.abspath('ultimate.html')
file_url = f'file:///{html_file_path}'

# Create Edge driver instance
driver = webdriver.Edge(options=edge_options)

# Open the HTML file
driver.get(file_url)

# Keep the browser window open (you can adjust the time or use input() to wait for user input)
try:
    while True:
        time.sleep(1)  # Keep the browser open
except KeyboardInterrupt:
    print("Closing the browser...")
    driver.quit()
import time

from selenium import webdriver
import requests
from PIL import Image
from io import BytesIO

# The URL we want to browse to
url = "http://deadendthrills.com/"

# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get(url)

#Scroll page and wait 5 seconds
driver.execute_script("window.scrollTo(0,2000);")
time.sleep(5)
image_elements = driver.find_elements_by_css_selector(".jig-loaded img")
i = 0

#Seclect image elements and point their URLs

for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("image" + str(i) + "." + image.format)
    i += 1
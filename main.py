import time

from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("your_website_link")
zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, "lxml")

a_tag_list = soup.select("div.StyledPropertyCardPhotoBody a")

links = []
for link in a_tag_list:
    links.append(link.get('href'))

pricing_tags_list = soup.select("div.PropertyCardWrapper span.PropertyCardWrapper__StyledPriceLine")

price_list = []

for price in pricing_tags_list:
    price_list.append(re.sub(r'[^0-9,$]', '', str(price.text)))

address_tag_list = soup.find_all(name="address")

address_list = []

for address in address_tag_list:
    address_list.append(re.sub(r'[^a-zA-Z0-9\s]', '', str(address.text).strip()))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for address, price, link in zip(address_list, price_list, links):
    driver.get("your forms link")
    time.sleep(1)
    form_text_boxes = driver.find_elements(By.CSS_SELECTOR, "div.Xb9hP input")
    form_text_boxes[0].send_keys(address)
    form_text_boxes[1].send_keys(price)
    form_text_boxes[2].send_keys(link)
    submit_button = driver.find_element(By.CSS_SELECTOR, "span.l4V7wb")
    submit_button.click()

driver.quit()

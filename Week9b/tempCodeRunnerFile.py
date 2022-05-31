from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.youtube.com/')
driver.find_element_by_name("search_query").click()
driver.find_element_by_name("search_query").send_keys("python")
driver.find_element_by_id("search-icon-legacy").click()
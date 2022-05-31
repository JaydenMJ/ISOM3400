

# wait = WebDriverWait(driver, 10)
# visible = EC.visibility_of_element_located

# wait.until(visible((By.NAME, "search_query")))
# driver.find_element_by_name("search_query").click()
# driver.find_element_by_name("search_query").send_keys("python")
# driver.find_element_by_id("search-icon-legacy").click()

# a = driver.find_element_by_tag_name("ytd-video-renderer")
# head=a.find_element_by_id('video-title')
# des=a.find_element_by_id('description-text')
# link=a.find_element_by_tag_name("a").get_attribute("href")
# print(link)
# print(des.text)
# print(head.text)
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get('https://www.youtube.com/')
driver.find_element_by_name("search_query").click()
driver.find_element_by_name("search_query").send_keys("python")
driver.find_element_by_id("search-icon-legacy").click()



# %%
if __name__="__name__":
    while(!=-1)
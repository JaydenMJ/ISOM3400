#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://finance.yahoo.com/quote/0700.HK?p=0700.HK&.tsrc=fin-srch')

#%%
element = driver.find_elements_by_tag_name('ul')

for item in element:
    link=item.
    print(item.text)

# %%
element = driver.find_elements_by_tag_name('ul')
for item in element:
    b=item.find_elements_by_tag_name('li')
    for item in b:
        try:
            a=item.find_element_by_tag_name('a').get_attribute("href")
        except:
            pass
        if "sustainability" in a:
            link=a.text
            break
        else:
            continue

# %%
link.text
# %%

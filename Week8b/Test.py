from selenium.webdriver import Chrome

driver =Chrome()
driver.get('http://www.python.org')

print(driver.page_source)
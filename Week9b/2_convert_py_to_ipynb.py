

#%%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://finance.yahoo.com/quote/9988.HK?p=9988.HK&.tsrc=fin-srch-v1")


# %%
# by_xpath

'''
<div class="D(ib) Mend(20px)" data-reactid="31">

<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" 
data-reactid="32">294.600
</span>

<span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)" data-reactid="33">+17.400 (+6.28%)</span>
<div id="quote-market-notice" 
class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm" data-reactid="34">
<span data-reactid="35">At close:  4:08PM HKT</span>
</div></div>
'''

classname='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'
xpath_name = "//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']"


try:
    element = driver.find_element_by_xpath(xpath_name)
    
except:
    print("Cannot find the xpath name")    

print(element.text)
# %%

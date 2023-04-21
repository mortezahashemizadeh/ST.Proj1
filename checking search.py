## codes for checking search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = 'chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
site=driver.get("https://www.digikala.com/search/?q=یاتبیایبتیاااب")  ### must connect to dash codes

time.sleep(1)  ### for loading page

def notfound(): 
    element=driver.find_elements(By.CSS_SELECTOR,".product-list_ProductList__emptyWrapper__Hh8Ij")
    if len(element)==1:
        return True 
if notfound():
    print('Product Not Found!!!')
else :
    print('found')
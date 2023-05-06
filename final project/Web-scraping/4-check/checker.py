'''
   Check the product list after searching and loading page
   If the product doesn't found after the search return True
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
def notfound():
        time.sleep(2) 
        '''
        Check the product list after searching and load the page
        If the product doesn't found after the search return True
        '''
        element=driver.find_elements(By.CSS_SELECTOR,".product-list_ProductList__emptyWrapper__Hh8Ij")
        if len(element)==1:
            return True

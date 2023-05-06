
'''
    scroll page for get and load data from server.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
def scroll():
    '''
    scroll page for get and load data from server.
    '''
    time.sleep(1)
    i,k=0,500
    while len(driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI'))<80:  #For Scroll and load page for get complete data.
        i+=500
        k+=500
        time.sleep(0.6)
        driver.execute_script("window.scrollTo({},{});".format(i,k))
        time.sleep(0.2)
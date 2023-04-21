
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains # For scrolling web page 
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import time

path = 'chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
site=driver.get("https://www.digikala.com/search/?q=دوچرخه")

time.sleep(5)
i,k=0,500
while len(driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI'))<80:  #For Scroll and load page for get complete data.
    i+=500
    k+=500
    time.sleep(0.1)
    driver.execute_script("window.scrollTo({},{});".format(i,k))
    time.sleep(0.5)
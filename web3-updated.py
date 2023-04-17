
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

# scrolling down
while True :
    ActionChains(driver).send_keys(Keys.PAGE_UP)
    ActionChains(driver).send_keys(Keys.PAGE_UP)
    element = driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
    if len (element) < 50 :
        try :          
            footer = driver.find_element(By.TAG_NAME, 'footer')
            ActionChains(driver).scroll_to_element(footer).perform()
        except:
            print("Scrolling Done.")
            
            time.sleep(2.5)
    else:
         break
    
element = driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
print (len (element))
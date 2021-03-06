from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
options = webdriver.ChromeOptions()
options.add_argument("--lang=fr-FR")
driver = webdriver.Chrome(executable_path="D:/Desktop/selenium/chromedriver.exe",chrome_options=options)
driver.get('https://www.google.com/')
search_input = driver.find_element_by_name('q')
x=search_input.send_keys('search query')
search_input.send_keys(Keys.RETURN)
results = []
next=True
pagenum=0
while next==True:
    pagenum+=1
    print(pagenum)
    for link in range(20):
        try:
            href=driver.find_element_by_xpath('//*[@id="rso"]/div['+str(link)+']/div/div[1]/a').get_attribute("href")
            print(href)
            results.append(href)
        except:
            print("e")
    try:
        driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Suivant')]").click()
        next=True
    except:
        next=False
try:
    file=pd.DataFrame(results)
    file.drop_duplicates(inplace=True)
    file=file[~file[file.columns[0]].str.contains('google.com')]
    #file.columns=file.columns.astype(str)
    #file.columns=file.columns.str.strip()
    #file.sort_values("0", inplace = True) 
    file.to_csv("links.csv",index = False,header=False)
except:
    print("something went wrong")
driver.quit()

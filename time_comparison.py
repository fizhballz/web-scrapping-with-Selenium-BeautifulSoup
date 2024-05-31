import time 
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd 
 
d = { 
	"selenium": [], 
	"bs4": [] 
} 
 
N = 25 
import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://en.wikipedia.org/wiki/CSS_Baltic" 

def zrbs4():
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, "html.parser") 
    main_div = soup.find("div", {"class": "mw-content-ltr mw-parser-output"}) 
    second_p = main_div.find_all("p")[1] 


def zrslm():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    firstp = driver.find_element(By.CSS_SELECTOR,value="div.mw-content-ltr.mw-parser-output")
    secondp = firstp.find_elements(By.CSS_SELECTOR,"p")[1]
    driver.quit()

for i in range(N): 
	print("-"*10, f"Experiment {i+1}", "-"*10) 
	t0 = time.time() 
	zrbs4()
	t1 = time.time() 
	zrslm()
	t2 = time.time() 
	d["selenium"].append(t2-t1) 
	d["bs4"].append(t1-t0) 
 
df = pd.DataFrame(d) 
'''df.to_csv("data.csv", index=False)'''

bars = ("selenium","bs4")
ypos=np.arange(len(bars))
time = [df["selenium"].mean(),df["bs4"].mean()]

plt.bar(ypos,time,align="center",alpha=0.5)
plt.xticks(ypos, bars)
plt.show()

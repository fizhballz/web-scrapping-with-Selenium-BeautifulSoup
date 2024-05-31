from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome__options)
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME , value='q')
button = driver.find_element(By.ID , value="submit")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder")
driver.quit()

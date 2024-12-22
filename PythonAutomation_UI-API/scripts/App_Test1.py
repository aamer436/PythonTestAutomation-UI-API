from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\maame\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("http://amazon.in")
print('title is ', driver.title)
driver.quit()

driver = webdriver.Firefox(executable_path='C:\\Users\\maame\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe')
driver.get("http://amazon.in")
print('title is ', driver.title)
driver.quit()
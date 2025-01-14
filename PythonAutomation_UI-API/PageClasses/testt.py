from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common_selenium_functions import CommonSeleniumFunctions
driver = webdriver.Chrome()
driver.get("https://www.dezlearn.com/webtable-example/")
c = CommonSeleniumFunctions(driver)
#c.take_full_page_screenshot("full.jpg")
elements = c.get_elements(By.XPATH,"//tr//td[1]/following-sibling::td[1]")
print('Length of elements ',len(elements))
[print(i.text) for i in elements]
c.get_elements_text(By.XPATH,"//tr//td[1]/following-sibling::td[1]")

#Get email based on name supplied
mailid = c.get_element_text(By.XPATH,"//tr//td[1][text()='Tim Watson']/following-sibling::td[1]")
print("mailid value for Tim is {}".format(mailid))


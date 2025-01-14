import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common_selenium_functions import CommonSeleniumFunctions
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
c = CommonSeleniumFunctions(driver)
sign_in_section="//*[@id='nav-link-accountList']"
sign_in_btn="//*[@class='nav-action-inner']"
email="//*[@type='email']"
continue_btn="//span[@id='continue']"
pwd="//*[@type='password']"
sign_in_submit="//*[@id='signInSubmit']"
otp="//*[@type='tel']"
otp_submit="//*[@id='auth-signin-button']"
user_name="//*[@id='nav-link-accountList']//span[contains(@id,'nav-link-accountList')]" #text should not contain "sign in"
sign_out="//span[text()='Sign Out']"

ActionChains(driver).move_to_element(c.get_element(By.XPATH,sign_in_section)).move_to_element(c.get_element(By.XPATH,sign_in_btn)).click().perform()
c.fn_set_value_by_xpath(email,"946124")
c.fn_click_by_xpath(continue_btn)
c.fn_set_value_by_xpath(pwd,"HJAsdjshcjhjhjh")
c.fn_click_by_xpath(sign_in_submit)
#c.fn_set_value_by_xpath(otp,"")
time.sleep(5)
c.fn_click_by_xpath(otp_submit)
c.fn_get_text_by_xpath(user_name)
c.fn_click_by_xpath(sign_out)

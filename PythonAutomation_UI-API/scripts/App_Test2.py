from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://amazon.in")
print('title is ', driver.title)
driver.quit()

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://amazon.in")
print('title is ', driver.title)
driver.quit()

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("http://amazon.in")
print('title is ', driver.title)
driver.quit()
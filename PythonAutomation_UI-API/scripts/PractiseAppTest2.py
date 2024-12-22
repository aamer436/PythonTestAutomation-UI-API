from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from Utils.BasePage import BasePage


class PractiseAppTest2:
    driver = None
    select_city_dropdown = (By.XPATH, "//*[@class='col-md-4 col-sm-12'][2]")

    def initiate_driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)

    def test_element_enabled(self):
        #self.base_page.do_click(self.return_orders_link)
        self.base_page.check_element_is_enabled(self.select_city_dropdown)

    def tear_down(self):
        self.driver.quit()


c = PractiseAppTest2()
c.initiate_driver()
c.test_element_enabled()
c.tear_down()

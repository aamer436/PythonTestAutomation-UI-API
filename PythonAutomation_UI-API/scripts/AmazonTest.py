
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class AmazonTest:
    driver = None
    search_edit = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")
    result_header = (By.XPATH, "//div[contains(@class,'breadcrumb')]//span[3]")
    header_rail = (By.XPATH, "//div[@id='nav-xshop-container']//a")

    def initiate_driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://amazon.in")
        self.driver.maximize_window()

    def test_mobile_results_page(self):
        self.driver.find_element(self.search_edit[0], self.search_edit[1]).send_keys('mobiles')
        self.driver.find_element(self.search_btn[0], self.search_btn[1]).click()
        result_text = self.driver.find_element(self.result_header[0], self.result_header[1]).text
        print(result_text, len(result_text))
        assert str(result_text).strip('"') == 'mobiles', 'Test failed'

    def test_header_rail(self):
        self.driver.get("https://amazon.in")
        list_a = self.driver.find_elements(self.header_rail[0], self.header_rail[1])
        for i in list_a:
            print(i.text)
        assert len(list_a) == 29, ' Test2 Failed'

    def tear_down(self):
        self.driver.quit()


c = AmazonTest()
c.initiate_driver()
#c.verify_mobile_results_page()
c.verify_header_rail()
c.tear_down()
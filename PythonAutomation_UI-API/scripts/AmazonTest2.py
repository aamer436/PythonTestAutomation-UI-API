import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from Utils.BasePage import BasePage


class AmazonTest2:
    driver = None
    search_edit = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")
    result_header = (By.XPATH, "//div[contains(@class,'breadcrumb')]//span[3]")
    header_rail = (By.XPATH, "//div[@id='nav-xshop-container']//a")
    email_validation_text = (By.XPATH, "//*[@id='auth-email-missing-alert']//*[@class='a-alert-content']")
    return_orders_link = (By.XPATH, "//a[contains(@href,'nav_orders_first')]")
    continue_btn = (By.ID, "continue")
    #signIn_label = (By.XPATH, "//*[normalize-space(text())='Sign-In']")
    hello_link = (By.XPATH, "//*[contains(@id,'nav-link-accountList') and @href]")
    signIn_btn = (By.XPATH, "//a/span[text()='Sign in']")


    def initiate_driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://amazon.in")
        print(type(self.driver))
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)

    def test_mobile_results_page(self):
        self.base_page.do_normal_sendkeys(self.search_edit, 'mobiles')
        self.base_page.do_normal_click(self.search_btn)
        result_text = self.base_page.get_element_text(self.result_header)
        print(result_text, len(result_text))
        assert str(result_text).strip('"') == 'mobiles', 'Test failed'

    def test_header_rail(self):
        self.driver.get("https://amazon.in")
        list_a = self.base_page.get_elements_text(self.header_rail)
        assert len(list_a) == 29, ' Test2 Failed'

    def test_element_display(self):
        self.base_page.do_click(self.return_orders_link)
        self.base_page.do_click(self.continue_btn)
        self.base_page.check_for_presence_of_element(self.email_validation_text)

    def test_navigation_to_signIn(self):

        self.base_page.move_to_element_and_click(self.hello_link, self.signIn_btn)
        time.sleep(20)


    def tear_down(self):
        self.driver.quit()


c = AmazonTest2()
c.initiate_driver()
#c.test_mobile_results_page()
#c.test_header_rail()
c.test_navigation_to_signIn()
c.tear_down()
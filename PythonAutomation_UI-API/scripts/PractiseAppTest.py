import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from Utils.BasePage import BasePage


class PractiseAppTest:
    driver = None
    example_dropdown = (By.ID, "dropdown-class-example")
    alert_textBox = (By.NAME, "enter-name")
    alert_btn = (By.XPATH, "//*[@class='btn-style' and @value='Alert']")
    confirm_btn = (By.XPATH, "//*[@class='btn-style' and @value='Confirm']")
    radio_btn_label_list = (By.XPATH, "//*[@name='radioButton']/..")
    radio_btn_list = (By.XPATH, "//*[@name='radioButton']")
    iframe_widget = (By.XPATH, "//iframe[@id='courses-iframe']")
    login_frame = (By.XPATH, "//a[@class='theme-btn register-btn']")

    def initiate_driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)

    def test_select_dropdown_on_practise_app(self):
        selected_option = self.base_page.select_from_drodown(self.example_dropdown,'value', 'option3')
        assert selected_option == 'Option3', 'Desired option not selected'

    def test_submit_alert(self):
        self.base_page.do_send_keys(self.alert_textBox, 'ALL')
        self.base_page.do_click(self.confirm_btn)
        self.base_page.handle_alert()

    def test_element_selected(self):
        self.base_page.select_radio_btn(self.radio_btn_list, 'Radio2')
        time.sleep(5)
        self.base_page.check_element_selected(self.radio_btn_list, 'Radio2')

    def test_navigate_to_frame_login(self):
        self.base_page.switch_to_frame('frame_xpath', self.iframe_widget)
        self.base_page.do_click(self.login_frame)
        time.sleep(10)
        self.base_page.switch_to_default_view()


    def tear_down(self):
        self.driver.quit()


c = PractiseAppTest()
c.initiate_driver()
c.test_navigate_to_frame_login()
c.test_submit_alert()
c.tear_down()

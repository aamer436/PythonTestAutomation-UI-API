import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def do_normal_click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def do_normal_sendkeys(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)

    def do_normal_elements_present(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        return bool(elements)

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_elements_text(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        elements_text = []
        for i in elements:
            elements_text.append(i.text)
        return elements_text

    def are_elements_present(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return bool(elements)

    def select_from_drodown(self, by_locator, select_strategy, option_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        s = Select(element)
        if select_strategy == 'visible_text':
            s.select_by_visible_text(option_text)
            selected_option = s.first_selected_option
            return selected_option.text
        elif select_strategy == 'index':
            s.select_by_index(option_text)
            selected_option = s.first_selected_option
            return selected_option.text
        elif select_strategy == 'value':
            s.select_by_value(option_text)
            selected_option = s.first_selected_option
            return selected_option.text

    def select_radio_btn(self, by_locator, button_text):
        print('am here')
        if self.do_normal_elements_present(by_locator):
            elements = self.driver.find_elements(*by_locator)
            print('len is ', len(elements))
            for i in elements:
                #temp = str(i.text).strip(' ')
                #print('-- ', temp, button_text, 'len ', len(temp), len(button_text))
                temp = str(i.find_element(By.XPATH, './..').text).strip(' ')
                if temp == button_text:
                    i.click()


    def check_element_selected(self, by_locator, button_text):
        result = False
        if self.do_normal_elements_present(by_locator):
            elements = self.driver.find_elements(*by_locator)
            for i in elements:
                temp = str(i.find_element(By.XPATH, './..').text).strip(' ')
                print('temp ', temp)
                if temp == button_text and i.is_selected():
                    print('element is selected')
                    result = True
                else:
                    print('element is not selected')
        return result

    def handle_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        #alert = self.driver.switch_to.alert
        time.sleep(5)
        alert.accept()
        #alert.dismiss()

    def check_for_presence_of_element(self, by_locator):
        element = self.driver.find_element(*by_locator)
        if element.is_displayed():
            print('element is present')
            return True
        else:
            print('element not present')
            return False

    def check_element_is_enabled(self, by_locator):
        element = self.driver.find_element(*by_locator)
        if element.is_enabled():
            print('element is enabled')
            return True
        else:
            print('element is not enabled')
            return False

    def switch_to_frame(self, frame_strategy, frame_identifier):
        if frame_strategy == 'frame_name':
            self.driver.switch_to.frame(frame_identifier)
        elif frame_strategy == 'index':
            self.driver.switch_to.frame(frame_identifier)
        elif frame_strategy == 'frame_xpath':
            self.driver.switch_to.frame(self.driver.find_element(*frame_identifier))

    def switch_to_default_view(self):
        self.driver.switch_to.parent_frame()

    def move_to_element_and_click(self, by_locator, by_loc):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*by_locator)).click(self.driver.find_element(*by_loc)).perform()




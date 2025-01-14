import io
import time

from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException, \
    ElementNotVisibleException, NoSuchAttributeException, NoAlertPresentException, WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from constants.Generic import GenericConstants as gc
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app_enums.alert_strategy import AlertStrategy
from app_enums.click_strategy import ClickStrategy
from app_enums.select_strategy import SelectStrategy
from app_enums.edit_strategy import EditStrategy
from datetime import datetime
from PIL import Image


class CommonSeleniumFunctions:
    exception_list = [ElementClickInterceptedException, TimeoutException, NoSuchElementException]

    def __init__(self, driver):
        self.driver = driver

    def fn_click_by_xpath(self, obj_element):
        try:
            status = self.fn_verify_presence_of_element(obj_element)
            if status:
                element = WebDriverWait(self.driver, gc.wait_10, 5, ignored_exceptions=self.exception_list) \
                    .until(EC.element_to_be_clickable((By.XPATH, obj_element)))
                element.click()
                print(f"Clicked on element ,xpath = {obj_element}")
                return True
            else:
                print(f"Element not found, xpath={obj_element}")
                return False
        except tuple(self.exception_list) as e:
            print(f"Given Element not available for click, xpath = {obj_element}")
            print(f"Exception:---------- {e.__class__.__name__} Message: {e}")
            return False

    def fn_click_if_exist(self, obj_element):
        try:
            self.fn_verify_presence_of_element(obj_element)
            status = len(self.driver.find_elements(By.XPATH, obj_element))
            if status >= 1:
                s = self.fn_click_by_xpath(obj_element)
                print(f'Element available for click,xpath={obj_element}')
                return s
            else:
                return False
        except tuple(self.exception_list) as e:
            print(f"Given Element not available for click, xpath = {obj_element}")
            print(f"Exception:---------- {e.__class__.__name__} Message: {e}")
            return False

    def fn_verify_presence_of_element(self, obj_element):
        try:
            element = WebDriverWait(self.driver, gc.wait_10, 5,
                                    ignored_exceptions=[ElementNotVisibleException, NoSuchAttributeException,
                                                        ElementClickInterceptedException,
                                                        NoSuchElementException, TimeoutException]) \
                .until(EC.element_to_be_clickable((By.XPATH, obj_element)))
            print(f"Element located, xpath={obj_element}")
            return True
        except(
                ElementNotVisibleException, NoSuchElementException, NoSuchAttributeException,
                ElementClickInterceptedException,
                TimeoutException) as e:
            print(f"Given Element not available for click, xpath = {obj_element}")
            print(f"Exception:---------- {e.__class__.__name__} Message: {e}")
            return False
        except Exception as e:
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return False

    def fn_set_value_by_xpath(self, obj_element, str_value):
        try:
            element = WebDriverWait(self.driver, gc.wait_10, 5, ignored_exceptions=self.exception_list) \
                .until(EC.presence_of_element_located((By.XPATH, obj_element)))
            element.clear()
            element.send_keys(str_value)
            print(f"Entered value={str(str_value)} in xpath = {obj_element}")
            return True
        except tuple(self.exception_list) as e:
            print(f"Given Element not displayed on page, xpath = {obj_element}")
            print(f"Exception:---------- {e.__class__.__name__} Message: {e}")
            return False

    def fn_get_text_by_xpath(self, obj_element):
        str_value = ''
        try:
            element = WebDriverWait(self.driver, gc.wait_10, 2, ignored_exceptions=self.exception_list) \
                .until(EC.presence_of_element_located((By.XPATH, obj_element)))
            str_value = element.text
            print(f"Retrieved value={str(str_value)} from xpath = {obj_element}")
            return str_value
        except tuple(self.exception_list) as e:
            print(f"Given Element not displayed on page, xpath = {obj_element}")
            print(f"Exception:---------- {e.__class__.__name__} Message: {e}")
            return 'Error'

    def get_element(self, *by_locator):
        try:
            element = WebDriverWait(self.driver, gc.implicit_wait_value).until(
                EC.visibility_of_element_located(by_locator))
        except Exception as e:
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return None
        return element

    def get_elements(self, *by_locator):
        try:
            elements = WebDriverWait(self.driver, gc.implicit_wait_value).until(
                EC.visibility_of_all_elements_located(by_locator))
        except Exception as e:
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return None
        return elements

    def fn_get_table_row_count(self, obj_element):
        try:
            elements = WebDriverWait(self.driver, gc.implicit_wait_value - 5, ignored_exceptions=self.exception_list) \
                .until(EC.visibility_of_all_elements_located((By.XPATH, obj_element)))
            print(f'Table row count = {str(len(elements))} for table xpath={obj_element}')
            return len(elements)
        except tuple(self.exception_list) as e:
            print(f'Given table not displayed on page, xpath={obj_element}')
            print(f'Exception: -------{e.__class__.__name__} Message : {e}')
            return 0

    def do_click(self, click_strategy: ClickStrategy, *by_locator):
        if click_strategy == ClickStrategy.NORMAL_CLICK:
            self.get_element(*by_locator).click()
        elif click_strategy == ClickStrategy.ACTIONS_CLICK:
            ActionChains(self.driver).move_to_element(self.get_element(*by_locator)).click().perform()
        elif click_strategy == ClickStrategy.JAVASCRIPT_CLICK:
            self.driver.execute_script("arguments[0].click();", self.get_element(*by_locator))
        else:
            print('Incorrect click strategy is used, please revisit the calling method')

    def do_send_keys(self, text, edit_strategy: EditStrategy, *by_locator):
        if edit_strategy == EditStrategy.NORMAL_EDIT:
            self.get_element(*by_locator).clear()
            self.get_element(*by_locator).send_keys()
        elif edit_strategy == EditStrategy.ACTIONS_EDIT:
            ActionChains(self.driver).move_to_element(self.get_element(*by_locator)).send_keys(text).perform()
        elif edit_strategy == EditStrategy.JAVASCRIPT_EDIT:
            self.driver.execute_script("arguments[0].value='{}';".format(text), self.get_element(*by_locator))
        else:
            print('Incorrect edit strategy is used, please revisit the calling method')

    def get_element_text(self, *by_locator):  # actually by_locator
        return self.get_element(*by_locator).text

    def get_elements_text(self, *by_locator):
        elements = self.get_elements(*by_locator)
        textlist = []
        for i in elements:
            textlist.append(i.text)
        print(f'Elements text {textlist}')
        return textlist

    def is_visible(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        print(f'Page title ={self.driver.title}')
        return self.driver.title

    def select_from_dropdown(self, select_strategy: SelectStrategy, option_to_be_selected, *by_locator):
        select = Select(self.get_element(*by_locator))
        if select_strategy == SelectStrategy.SELECT_BY_VISIBLE_TEXT:
            select.select_by_visible_text(option_to_be_selected)
        elif select_strategy == SelectStrategy.SELECT_BY_VALUE:
            select.select_by_value(option_to_be_selected)
        elif select_strategy == SelectStrategy.SELECT_BY_INDEX:
            select.select_by_index(option_to_be_selected)
        else:
            print('incorrect select strategy is used, please revisit calling method')

    def get_all_dropdown_options(self, *by_locator):
        all_options = [i.text for i in self.get_elements(*by_locator)]
        return all_options

    def handle_alert_box(self, alert_strategy: AlertStrategy, input_text=None):
        a = ''
        try:
            a = WebDriverWait(self.driver, gc.implicit_wait_value).until(EC.alert_is_present())
        except NoAlertPresentException as e:
            print(f'No alert present {type(e)}')

        if alert_strategy == AlertStrategy.ACCEPT:
            a.accept()
        elif alert_strategy == AlertStrategy.DISMISS:
            a.dismiss()
        elif alert_strategy == AlertStrategy.GET_TEXT:
            return a.text
        elif alert_strategy == AlertStrategy.SEND_KEYS:
            a.send_keys(input_text)
        else:
            print('incorrect alert strategy is used, please revisit calling method')

    def fn_do_scroll(self):
        try:
            time.sleep(1)
            height = str(self.driver.get_window_size()).split(":")[-1].strip()
            height = height[:-1]
            for i in range(0, int(height), 300):
                self.driver.execute_script("document.getElementById('mainContent').scrollTo(0," + str(i) + ");")
                time.sleep(2)
            print('Scroll succesful')
        except Exception as e:
            print(f'Unable to scroll! Error: {e}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')

    def fn_scroll_to_bottom(self):
        try:
            # Get scroll height
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down to bottom
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                # calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            print("Scrolled successfully to bottom of the page")
        except Exception as e:
            print(f'Unable to scroll! Error: {e}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')

    def fn_scroll_to_particular_element(self, *by_locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(*by_locator))
            print('Scrolled successfully until particular element is visible')
        except Exception as e:
            print(f'Unable to scroll!Error: {e}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')

    def fn_verify_visibility_of_element(self, xpath):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print(f'Visibility of element located,xpath={xpath}')
            return True
        except tuple(self.exception_list) as e:
            print(f'Given element not visible on page, xpath={xpath}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return False
        except WebDriverException as e:
            print(f'WebDriverException occurred for element with xpath={xpath}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return False
        except Exception as e:
            print(f'An unexpected error occurred for element with xpath={xpath}')
            print(f'Exception: {e.__class__.__name__} Message: {e}')
            return False

    def fn_find_elements(self, xpath):
        stat = self.driver.find_elements(By.XPATH, xpath)
        print(f'Elements count = {str(len(stat))}')
        return stat

    def wait_for_clickable_element(self,
                                   *by_locator):  # given just 'locator' element to be clickable needs just xpath or WebElement
        '''
        waits for element to be fully loaded, visible and clickable within the given timeout
        '''
        try:
            wait = WebDriverWait(self.driver, gc.wait_10)
            element = wait.until(EC.element_to_be_clickable((by_locator)))
            print(f'Element is clickable xpath = {str(by_locator)}')
            return element
        except TimeoutException:
            print(f'Element located by {by_locator} not clickable within {gc.wait_10} seconds.')

    def wait_until_page_load(self, locator):
        date1 = datetime.now()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, locator)))
        date2 = datetime.now()
        duration = date2 - date1
        total_seconds = duration.total_seconds()
        print(f'Waited for {str(total_seconds)} seconds until element is visible. xpath = {locator}')

    def get_table_column_names(self, obj_tbl):
        row_count = len(self.driver.find_elements(By.XPATH, obj_tbl))
        column_name_list = []
        for i in range(row_count):
            temp_xpath = obj_tbl + "[" + str(i + 1) + "]"
            name = self.driver.find_element(By.XPATH, temp_xpath).text
            column_name_list.append(name)
        return column_name_list

    def take_full_page_screenshot(self,output_file):
        try:
            total_height = 0
            window_height = self.driver.execute_script("return window.innerHeight")
            print('Total Height ',total_height)
            print('Window Height ',window_height)
            screenshots=[]
            for i in range(0,3000,651):
                if i<=651:
                    self.driver.execute_script(f'window.scrollTo(0,{i});')
                else:
                    self.driver.execute_script(f'window.scrollTo({i},{i+651});')
            self.driver.execute_script(f'window.scrollTo(0,0);')
            time.sleep(3)
            #scroll and take screenshots
            for i in range(0,3000,651):
                self.driver.execute_script(f'window.scrollTo(0,{i});')
                time.sleep(10)
                screenshot = self.driver.get_screenshot_as_png()
                screenshots.append(Image.open(io.BytesIO(screenshot)))

            #stitch images together
            total_width = max(img.width for img in screenshots)
            total_height = sum(img.height for img in screenshots)
            stitched_image = Image.new('RGB',(total_width,total_height))

            current_height = 0
            for img in screenshots:
                stitched_image.paste(img,(0,current_height))
                current_height += img.height

            #save the stitched image
            stitched_image.save(output_file)
            print(f'Screenshot saved to {output_file}')
        finally:
            self.driver.quit()
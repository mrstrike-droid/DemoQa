from datetime import time
import logging
import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

logger = logging.getLogger("log_event")
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoQA:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(10)
        self._url = "http://demoqa.com/"

    def open_page(self):
        self._driver.get(self._url)
        self._driver.maximize_window()

    def text_box(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        text_box = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Text Box')]")))
        text_box.click()
        time.sleep(1)
        full_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userName')]")))
        full_name.send_keys("<NAME>")
        time.sleep(1)
        email = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userEmail')]")))
        email.send_keys("123@gmail.com")
        time.sleep(1)
        current_address = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'currentAddress')]")))
        current_address.send_keys("123 Main St")
        time.sleep(1)
        permanent_address = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'permanentAddress')]")))
        permanent_address.send_keys("33 West St")
        time.sleep(1)
        submit_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn btn-primary')]")))
        submit_button.click()
        time.sleep(1)
        result = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'output')]")))
        logger.info(result.text)
        self._driver.switch_to.new_window('tab')


    def check_box(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        check_box = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Check Box')]")))
        check_box.click()
        time.sleep(1)
        button_collapse_1 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/span/button")))
        button_collapse_1.click()
        time.sleep(1)
        button_collapse_2 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/span/button")))
        button_collapse_2.click()
        time.sleep(1)
        button_collapse_3 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[2]/span/button")))
        button_collapse_3.click()
        time.sleep(1)
        button_collapse_4 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[2]/ol/li[1]/span/button")))
        button_collapse_4.click()
        time.sleep(1)
        button_collapse_5 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[2]/ol/li[2]/span/button")))
        button_collapse_5.click()
        time.sleep(1)
        button_collapse_6 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/ol/li/ol/li[3]/span/button")))
        button_collapse_6.click()
        time.sleep(1)
        button_click_1 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/ol/li/ol/li[3]/span/label/span[1]")))
        button_click_1.click()
        time.sleep(1)
        result = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@id, 'result')]")))
        logger.info(result.text)
        button_click_2 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]")))
        button_click_2.click()
        time.sleep(1)
        logger.info(result.text)
        button_click_1.click()
        time.sleep(1)
        logger.info(result.text)
        button_click_3 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/ol/li/span/label/span[1]")))
        button_click_3.click()
        time.sleep(1)
        logger.info(result.text)
        self._driver.switch_to.new_window('tab')

    def radio_button(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        radio_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Radio Button')]")))
        radio_button.click()
        time.sleep(1)
        yes = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'yesRadio')]")))
        yes.click()
        time.sleep(1)
        text = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-success')]")))
        logger.info(text.text)
        impressive = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'impressiveRadio')]")))
        impressive.click()
        time.sleep(1)
        logger.info(text.text)
        no = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'noRadio')]")))
        if "disabled" in no.get_attribute("class"):
            logger.error('Button is disabled')
        else:
            no.click()
        self._driver.switch_to.new_window('tab')

    def web_tables_check_vega(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        web_tables = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Web Tables')]")))
        web_tables.click()
        time.sleep(1)
        search = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'searchBox')]")))
        search.click()
        search.send_keys("Vega")
        time.sleep(1)
        first_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]")))
        logger.info(first_name.text)
        last_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[2]")))
        logger.info(last_name.text)
        age = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[3]")))
        logger.info(age.text)
        email = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[4]")))
        logger.info(email.text)
        salary = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[5]")))
        logger.info(salary.text)
        department = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[6]")))
        logger.info(department.text)
        self._driver.switch_to.new_window('tab')

    def web_tables_create_new_employee(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        web_tables = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Web Tables')]")))
        web_tables.click()
        time.sleep(1)
        add = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'addNewRecordButton')]")))
        add.click()
        time.sleep(1)
        first_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'firstName')]")))
        first_name.click()
        first_name.send_keys("Alex")
        last_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'lastName')]")))
        last_name.click()
        last_name.send_keys("PC")
        email = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userEmail')]")))
        email.click()
        email.send_keys("qweewq@gmail.com")
        age = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'age')]")))
        age.click()
        age.send_keys("42")
        salary = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'salary')]")))
        salary.click()
        salary.send_keys("20000")
        department = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'department')]")))
        department.click()
        department.send_keys("IT")
        submit = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'submit')]")))
        submit.click()
        time.sleep(1)

        search = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'searchBox')]")))
        search.click()
        search.send_keys("PC")
        time.sleep(1)
        first_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]")))
        logger.info(first_name.text)
        last_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]")))
        logger.info(last_name.text)
        age = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[3]")))
        logger.info(age.text)
        email = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[4]")))
        logger.info(email.text)
        salary = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[5]")))
        logger.info(salary.text)
        department = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[6]")))
        logger.info(department.text)
        self._driver.switch_to.new_window('tab')

    def create_ten_web_tables_account(self):
        count = 0
        first_name_list = ['Alex', 'Rebbecca', 'John', 'Sam', 'Jane', 'Anna', 'Tom', 'Jerry', 'Margo', 'Terry', 'Goward', 'Andrzey', 'Yulia', 'Ezra', 'Andy']
        last_name_list = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson']


        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/a[1]/div/div/div[3]")))
        first_clickable_object.click()
        time.sleep(1)
        web_tables = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Web Tables')]")))
        web_tables.click()
        time.sleep(1)
        while count < 15:
            add = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'addNewRecordButton')]")))
            add.click()
            time.sleep(1)
            first_name = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'firstName')]")))
            first_name.click()
            first_name.send_keys(random.choice(first_name_list))
            last_name = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'lastName')]")))
            last_name.click()
            last_name.send_keys(random.choice(last_name_list))
            email = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userEmail')]")))
            email.click()
            email.send_keys("qweewq@gmail.com")
            age = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'age')]")))
            age.click()
            random_age = str(random.randint(18, 65))
            age.send_keys(random_age)
            salary = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'salary')]")))
            salary.click()
            random_salary = str(random.randint(1000, 9999))
            salary.send_keys(random_salary)
            department = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'department')]")))
            department.click()
            department.send_keys("IT")
            submit = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'submit')]")))
            submit.click()
            time.sleep(1)
            count = count + 1
        time.sleep(1)
        select_option = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/select")))
        select_option.click()
        time.sleep(1)
        option = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//option[contains(@value, '20')]")))
        option.click()
        time.sleep(10)

if __name__ == "__main__":
    test1 = DemoQA()
    #test1.open_page()
    #test1.text_box()
    #time.sleep(1)
    #test1.open_page()
    #test1.check_box()
    #time.sleep(1)
    #test1.open_page()
    #test1.radio_button()
    #time.sleep(1)
    #test1.open_page()
    #test1.web_tables_check_vega()
    #time.sleep(1)
    #test1.open_page()
    #test1.web_tables_create_new_employee()
    #time.sleep(1)
    test1.open_page()
    test1.create_ten_web_tables_account()
    time.sleep(1)



